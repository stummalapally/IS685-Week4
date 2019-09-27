import sys

if len(sys.argv)!=2:
    print("Usage:python"+sys.argv[0]+"<first number>")
    sys.exit()
first = int(sys.argv[1])




def doubleThisNow(a):
    result=2*a
    print(result)
doubleThisNow(first)    