def fact(n):
    if n<=1:
        return 1
    else:
        return n * (fact(n-1))
k =int(input("Enter The number: "))
print("Factorial of",k,"is",fact(k))
