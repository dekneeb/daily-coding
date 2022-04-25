def color_invert(rgb):
    return tuple(255 - c for c in rgb)

color_invert((255, 145, 0))


def stringindx(str):

    return str.index("H")

print(stringindx("HeLLo"))