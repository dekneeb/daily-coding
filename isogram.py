# return True if its an isogram: no duplicate letters, it is not case sensitive
# method 1
def isogram(str):
    y= str.lower()
    lst = []
    for i in y:
        lst.append(y.count(i))
    for j in lst:
        if j > 1:
            return False
    return True
    
print(isogram("happy"))

# method 2 - a set value in python does not allow duplicates 

def isogram(str):
    return len(str) == len(set(str.lower()))

print(isogram("star"))