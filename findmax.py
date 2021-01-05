items = [4, 23, 9, 5, 12, 65, 72, 3, 91, 53]

def find_max(items):
    if len(items) == 1:
        return items[0]
    
    
    op1 = items[0]
    print(op1)
    op2 = find_max(items[1:])
    print(op1, op2)
    
    if op1 > op2:
        return op1
    else:
        return op2
    
print(find_max(items))