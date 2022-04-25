def filter_list(lst):

    for i in lst:
        if str(i).isdigit():
            return i

print(filter_list([1, 2, 3, 'a', 'b', 'c']))