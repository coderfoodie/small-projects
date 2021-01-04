items = [4, 23, 9, 5, 12, 65, 72, 3, 91, 53]

def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i
    return None

print(find_item(65, items))
print(find_item(150, items))