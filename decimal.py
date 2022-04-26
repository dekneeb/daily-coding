def convert_to_decimal(perc):
    lst = []
    for i in perc:
        new = i[:-1]
        
        lst.append(int(new)/100)
    print(lst)


convert_to_decimal(["1%", "2%", "3%"])