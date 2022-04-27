def tribonacci(sig, n):
    if n == 0:
        return []
    else:
        while len(sig) < n:
            sig.append(sum(sig[-3:]))
    
    return sig[:n]
        
   
print(tribonacci([1, 1, 1], 10))
