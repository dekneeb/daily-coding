# method 1

def capitalize(str):
    x = str.capitalize()
    return x 

print(capitalize("hello"))

# method 2

def capitalize(str):

    return str[0].upper() + str[1::]

print(capitalize("hello"))
