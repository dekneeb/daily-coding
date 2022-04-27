def stringsplit(str):
    if len(str) % 2 ==0:
        n=2
        x = [str[i:i+n] for i in range(0, len(str), n)]
        return x
    elif len(str) %2 ==1:
        str = str + "_"
        n=2
        x = [str[i:i+n] for i in range(0, len(str), n)] 
        return x

print(stringsplit("heloott"))