#  method 1 - recursive
# given an array and a number, write a recursive function to see if the array includes the given el


def includesnum(arr, num):

    if len(arr) == 0:
        return False
    elif arr[0] == num:
        return True
    else:
        if arr[0] != num:
            arr.remove(arr[0])
            return includesnum(arr, num)



print(includesnum([1, 2, 3, 4, 5], 5))