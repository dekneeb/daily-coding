def simon_says(lst1, lst2):

    for i in lst1:
            if lst1[i] != lst2[i+1]:
                return False
            else:
                return True

print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))


# edabit solution
def simon_says(lst1, lst2):
	if len(lst1) != len(lst2):
		return False
	elif lst1[0] != lst2[1]:
		return False
	else:
		for i in range(0, len(lst1)-1):
			if lst1[i] != lst2[i+1]:
				return False
			else:
				return True

                # added range in for loop because with a 2 num list length the lst2[i+1] was out of range


# solution 3 - SO SIMPLE
def simon_says(lst1, lst2):
	return lst1[:-1] == lst2[1:]