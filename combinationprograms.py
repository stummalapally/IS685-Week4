import sys

if len(sys.argv)!=2:
    print("Usage:python"+sys.argv[0]+"<first number>")
    sys.exit()
first = int(sys.argv[1])


def doubleThisNow(a):
    result=2*a
    print(result)
    
def doubleThisgive(a):
    return 2*a

doubled=doubleThisgive(5)
print(doubled)



a=5
b=6
def multiplyThese(a,b):
    result=a*b
    print(a)
    print(b)
    
    return a*b
print(multiplyThese(a,b))




def isFrance(a):
    if a=="france":
        print("Oui")
        return True
    else:
        print("Non monsieur")
        return False
       
print("The result is: "+ str(isFrance("Germany")))    
   
   
   
def xTimes2y(a,b):
    return a*doubleThisgive(b)
print("The result is :{0}".format(xTimes2y(3,9)))



def doubleTo100(a):
    doubledValue=a
    n=0
    while doubledValue <= 100:
        n=n+1
        doubledValue=doubledValue*2
    return n
print("Number of doubling events:{0}".format(doubleTo100(80)))
