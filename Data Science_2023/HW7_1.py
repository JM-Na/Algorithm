import numpy as np
import pandas as pd

columns = ['District', 'House Type', 'Income', 'Previous Customer']


def main():
    # given data
    data = pd.read_excel("C://Users//-//Downloads//archive//exampleDataset.xlsx")
    target = data[['Outcome']]

    # calculate entropy before split
    entropy_root = calEntropy(target)
    # get root node by calculating the information gain
    root_node = infoGain(data)
    # if District = Rural, Outcome is all Responded, so split district into (Urban, Suburban), (Rural)
    data_rural = data.loc[data[root_node] == 'Rural']
    data.drop(data[data[root_node] == 'Rural'].index, inplace=True)
    # As Rural is already done, caculate the other one
    entropy = calEntropy(data[['Outcome']])
    node = infoGain(data)
    # split with Income
    data_high = data.loc[data[node] == 'High']
    data_low = data.loc[data[node] == 'Low']

    # calculate data_high first
    entropy = calEntropy(data_high[['Outcome']])
    node = infoGain(data_high)
    # selected node is House type, and split into
    # (Detached, Terrace), (Semi-detached) then this node is done
    data_high_semi = data_high.loc[data[node] == 'Semi-detached']
    data_high = data_high.loc[data[node] != 'Semi-detached']

    # calculate data_low next
    entropy = calEntropy(data_low[['Outcome']])
    node = infoGain(data_low)
    # split with previous customer
    data_low_yes = data_low.loc[data[node] == 'Yes']
    data_low_no = data_low.loc[data[node] != 'Yes']
    # data_low_no node is done, continue to data_low_yes
    entropy = calEntropy(data_low_yes[['Outcome']])
    node = infoGain(data_low_yes)
    # split with district, Urban and Suburban / after split each are done
    data_low_yes_urban = data_low_yes.loc[data[node] == 'Urban']
    data_low_yes_sub = data_low_yes.loc[data[node] != 'Urban']
    # structure of tree
    # data -> data || data_rural(Responded)
    # data
    # data_high                           || data_low
    # data_high(No) || data_high_semi(Re) || data_low_no(Re) || data_low_yes
    #                                     ||                 ||  data_low_yes_urban(No) || data_low_yes_sub(Re)
    print("*Basic Structure of Tree")
    print(' -Is Rural:Re', '\n', '-Not Rural - ''**Is High -', '*Not Semi:No /', '*Is Semi:Re', '\n', '            ',
          '**Is Low - *Is No:RE', '\n', '                       ', '*Is Yes -', 'Is Urban:No /', 'Is Suburban:Re')
    print("-----------------------------------------------------------------------------")
    print("*structure of tree in nested list")
    print("[['Is Rural', Re], ['Not Rural': ['Is High': ['Not Semi', No],['Is Semi', Re]], "
          "['Is Low': ['Is No', Re],['Is Yes': ['Is Urban', No]['Is Suburban', Yes]]]")
    print("-----------------------------------------------------------------------------")
    print("So when we predict new customer whose"
          "{district = suburban, house type = detached, income = low, previous cutomer = yes} with this tree")
    print("We can predict the marketing outcome for this customer will be 'Responded'")
    print("         ")


def proc(data):
    return data.index.values.tolist()


def calEntropy(label):
    elements, counts = np.unique(label, return_counts=True)
    # sum of calculation -nlogn, n is (num of particular rows)/(num of rows)
    entropy = -np.sum([(counts[i] / np.sum(counts)) * np.log2(counts[i] / np.sum(counts))
                       for i in range(len(elements))])
    return entropy


def infoGain(data):
    def calculate(attr):
        vals, counts = np.unique(data[attr], return_counts=True)
        weighted_Entropy = np.sum([(counts[i] / np.sum(counts)) *
                                   calEntropy(data.loc[data[attr] == vals[i], 'Outcome'])
                                   for i in range(len(vals))])
        return weighted_Entropy
    maxinfo = 1
    maxattr = ''
    for k in columns:
        temp = calculate(k)
        if maxinfo > temp:
            maxinfo = temp
            maxattr = k
    return maxattr


if __name__ == "__main__":
    main()
