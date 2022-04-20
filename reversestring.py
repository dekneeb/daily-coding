#  method 1

def reverse_string(str):
    txt = str[::-1]
    new = txt.swapcase()
    print(new)

reverse_string('Hello World')


# method 2 - recursion

def revstring(str):

    if str == '':
        return ''

    else:
        return str[len(str) -1] + revstring(str[0:len(str)-1])

print(revstring('Green World'))