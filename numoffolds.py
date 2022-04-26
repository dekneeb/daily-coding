from tkinter import N


def layers(n):
    if n == 0:
        return "0.0005m"
    else:
        l = 2 ** n 
        x = l * 0.5
        y = x / 1000


    return str(y) + "m"

print(layers(4))