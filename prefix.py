def longestCommonPrefix(lst):
    for i in lst:
        if lst[i][0] == lst[i+1][0]:
            print(i)


longestCommonPrefix(["flower", "flow", "flight"])

    
