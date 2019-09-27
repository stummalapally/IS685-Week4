def fibRecursive(n):     #fib_n=fib_n-1+fib_n-2
    if n<2:              #base case
        return n 
    
    return fibRecursive(n-1)+fibRecursive(n-2)
   

print(fibRecursive(2))