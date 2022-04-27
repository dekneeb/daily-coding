# create a function that finds the mean of the array
# array can be integer or float - can be positive or negative
# within function - return mean and mode
# mode: most frequent element in list
# round to two decimal points
# return int, int

def mean_and_mode(lst):

    x = round((sum(lst)/ len(lst)), 2)

    dict = { lst.count(i) : i for i in lst}
    print(dict)
    y = max(dict.keys())
    z = dict.get(y)
    
    return x, z

print(mean_and_mode([4, 7.46, 1, 1, 1, 1, 3, 7.46, 7.46]))