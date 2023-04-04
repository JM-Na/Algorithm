import pandas as pd
import featuretools as ft
from woodwork.logical_types import Categorical


def main():
    clients = pd.read_csv('C://Users//-//Downloads//archive//clients.csv', parse_dates=['joined'])
    loans = pd.read_csv('C://Users//-//Downloads//archive//loans.csv', parse_dates=['loan_start', 'loan_end'])
    payments = pd.read_csv('C://Users//-//Downloads//archive//payments.csv', parse_dates=['payment_date'])

    es = ft.EntitySet(id='clients')
    es = es.add_dataframe(dataframe_name='clients', dataframe=clients, index='client_id', time_index='joined')
    es = es.add_dataframe(dataframe_name='loans', dataframe=loans, index='loan_id', time_index='loan_start')
    es = es.add_dataframe(dataframe_name='payments', dataframe=payments,
                          logical_types={'missed': Categorical},
                          make_index=True, index='payment_id', time_index='payment_date')

    # Group loans by client id and calculate total value of loans
    stats = loans.groupby('client_id')['loan_amount'].agg(['sum'])
    stats.columns = ['total_loan_amount']
    stats = clients.merge(stats, left_on='client_id', right_index=True, how='left')
    print(stats.head(5))
    print('-----------------------------------------------------------')
    # Create relationships
    r_client_previous = ft.Relationship(entityset=es,
                                        parent_dataframe_name='clients', parent_column_name='client_id',
                                        child_dataframe_name='loans', child_column_name='client_id')
    es = es.add_relationship(relationship=r_client_previous)

    r_payments = ft.Relationship(entityset=es,
                                 parent_dataframe_name='loans', parent_column_name='loan_id',
                                 child_dataframe_name='payments', child_column_name='loan_id')
    es = es.add_relationship(relationship=r_payments)
    print(es)
    print('-----------------------------------------------------------')
    # Create new features using specified primitives
    features, feature_names = ft.dfs(entityset=es, target_dataframe_name='clients',
                                     agg_primitives=['mean', 'max', 'last'],
                                     trans_primitives=['year', 'month', 'subtract_numeric', 'divide_numeric'])
    print(features.head(5))


if __name__ == "__main__":
    main()
