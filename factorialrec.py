def factorialRecursive(n):
    if n==1:
        return 1
    return n*factorialRecursive(n-1)


inputNumber=5
print("The factorial of {0} is {1}".format(inputNumber,factorialRecursive(inputNumber)))