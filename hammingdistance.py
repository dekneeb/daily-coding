# count how many differences between two strings

# method 1

def hamming_distance(w, x):
    count = 0

    for i in w:
        for j in x:
            if i != j:
                count =+ 1

    return count


print(hamming_distance('abcde', 'abcdd'))