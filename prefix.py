def longestCommonPrefix(lst):
    ans = ''
    
    n = len(min(lst))
        
    for i in range(n):
        if all(x[i] == lst[0][i] for x in lst):
            ans = ans + lst[0][i]
        else:
            break
    return ans
 


print(longestCommonPrefix(["flower", "flow", "flight", "foo", "fingerlicking"]))

    
