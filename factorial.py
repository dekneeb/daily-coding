# method 1
# find the product of factorial of n

# method 1
def factorial(n):

    pass 

factorial(5)


# method 2 recursive with multiplication

def factorial(n):

    if n < 0:
        return -1
    elif n <2:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# method 2 recursive with addition

def factorial(n):

    if n < 0:
        return -1
    elif n <2:
        return 1
    else:
        return n + factorial(n-1)

print(factorial(5))