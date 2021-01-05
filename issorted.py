items1 = [4, 23, 9, 5, 12, 65, 72, 3, 91, 53]
items2 = [3, 4, 5, 9, 12, 23, 53, 65, 72, 91]

def is_sorted(itemlist):
    return all(itemlist[i] <= itemlist[i + 1] for i in range(len(itemlist) - 1))

print(is_sorted(items1))
print(is_sorted(items2))