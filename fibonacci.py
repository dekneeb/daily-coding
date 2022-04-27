def fibonacci(n):

    if n == 0:
        return 0
    else:
        return n + fibonacci(n-1) 

print(fibonacci(5))