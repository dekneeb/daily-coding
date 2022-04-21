# method 1
def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
print(palindrome('abba'))
# method 2 - algorithm
def palindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
print(palindrome('abba'))

# method 3 recursive
def palindrome(str):
    if len(str) < 1:
        return True
    for i in range(0, int(len(str))):
        if str[i] != str[len(str) -1]:
            return False
        else:
            return palindrome(str[1: len(str)-1])
print(palindrome('racecar'))






