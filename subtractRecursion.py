
def subtractTo10(num):
    #check if i am in base case
    if num==10:
        return 0
    return subtractTo10(num-1)
    
print("Number of Recursions:{0}".format(subtractTo10(50)))