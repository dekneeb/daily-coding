# method 1
# print sum of all numbers from a to b that are divisible by c

from re import I


def evenly_divisible(a, b,c):
    arr = []

    for num in range(a, b+1):
        if num % c == 0:
            arr.append(num)

    return sum(arr)

print(evenly_divisible(1, 10 ,2))
print(evenly_divisible(2, 16, 4))







