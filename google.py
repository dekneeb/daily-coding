

from multiprocessing.sharedctypes import Value


def call(arr):

    if len(arr) == 0:
        return 'null'

    else:
        
        return arr[0] + call(arr[0+1])

    
        




print(call([1, 2, 3, 4, 5]))








