n= int(input("Enter Value: "))


def fact(n):
    if n<=1:
        return 1
    factorial = n*fact(n-1)
    return factorial

print(fact(n))
