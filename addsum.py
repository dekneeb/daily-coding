# method 1

def add_up(num):
    return sum(i for i in range(0, num + 1))


print(add_up(5))


# method 2 recursive

def add_up(num):
    
    if num == 0:
        return 0
    else:
        return num + add_up(num -1)


print(add_up(5))

# add numbers in an array up to specified index; recursive

def addingupto(a, b):

    sum = a[b]

    if b == 0:
        return sum
    else:
        return sum + addingupto(a, b-1)



print(addingupto([1, 2, 3, 4, 5], 2))