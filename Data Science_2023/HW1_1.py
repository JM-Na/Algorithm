import math


def main():
    num = int(input("Type your number:"))
    if num < 2 or num > 32767:
        print("Number out of bound, Type your number again")
    result = isPrime(num)
    if result == 1:
        print(num, "is prime number")
    else:
        print(num, "is not Prime Number")


def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            print(i)
            return i
            break
    return 1


if __name__ == "__main__":
    main()
