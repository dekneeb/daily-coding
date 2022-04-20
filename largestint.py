# method 1 recurion
# given an array, find the largest integer

def largestint(arr):
    if len(arr) == 1:
        return arr[0]
    if arr[0] > arr [1]:
            arr.remove(arr[1])
    else:
        arr.remove(arr[0])

    return largestint(arr)

print(largestint([1, 8, 5, 3]))


# method 2 - easy
def largestint(arr):
    return max(arr)
print(largestint([1, 4, 5, 9]))


# method 3 - algorithmic
def largestint(arr):

    for i in arr:
        for j in arr:
            if i > j:
                result = i

    return result
print(largestint([1, 4, 5, 3]))