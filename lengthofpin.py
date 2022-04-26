def length_pin(str):
    if len(str) != 4 and len(str) != 6:
        return False
    else:
        if str.isdigit() == False:
            return False
    return True


print(length_pin("1235"))

# you do not need to loop over items in a str for is digit because it returns true or false based on if all items in a str are digits
