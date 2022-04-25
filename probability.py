# return probability percentage a number is selected from a given list that is greater than or equal to a given n


def probability(lst, n):
    count = 0
    for i in lst:
        if i > n:
            count +=1

    return round(count*100/len(lst), 1)    


print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))

def probability(lst, n):
	return round(sum(1 for x in lst if x >= n) / len(lst) * 100, 1)