def doubleTo100recursion(num):
    if num>100:
        return 0
    return doubleTo100recursion(2*num)+1
print(doubleTo100recursion(10))