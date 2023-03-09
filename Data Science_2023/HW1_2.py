def main():
    K = list(input("Type your Keys : ").split())
    V = list(input("Type your Values : ").split())
    if len(K) != len(V):
        print("Inappropriate input, try again")
        return 0
    D = makeDict(K, V)
    for k, v in D.items():
        print(k, v)


def makeDict(K, V):
    D = dict(zip(K, V))
    return D


if __name__ == "__main__":
    main()