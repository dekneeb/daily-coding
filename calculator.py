# method 1
def calculator(num1, operator, num2):
    if operator == "/" and num2 == 0:
        return "Can't divide by 0!"
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        num1 / num2
    elif operator == '*':
        num1 * num2
print(calculator(2, '+', 3))

# method 2

def calculator(num1: int, operator: str, num2: int) -> int:

    if num2 == 0 and operator == '/':
        return "Can't divide by 0"

    funcs = {
        "+" : int.__add__,
        "-" : int.__sub__,
        "*" : int.__mul__,
        "/" : int.__floordiv__,
    }

    return funcs[operator](num1, num2)

print(calculator(5, '-', 4))