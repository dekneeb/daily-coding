def bracket_match(str):

    pair = {'}' : '{', ')':'(', ']': '['}
    close = set(')}]')
    open = set('({[')
    stack = []
    
    for i in str:
        if i in open:
            stack.append(i)
        if i in close:
            if stack.pop() != pair[i]:
                return False
            else:
                continue 
    return True

print(bracket_match("()[]([]])"))