#  return a new list with the first element removed, and the "num" argument added to the end

def next_in_line(lst, num):
    
    lst.pop(0)
    lst.append(num)
    return lst


print(next_in_line([1, 2, 3, 4], 5))