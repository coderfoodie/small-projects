items = [4, 23, 9, 5, 12, 65, 72, 3, 91, 53]

def binarysearch(item, itemlist):
    listsize = len(itemlist) - 1
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        midPt = (lowerIdx + upperIdx) // 2
        if itemlist[midPt] == item:
            return midPt
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None

print(binarysearch(23, items))
print(binarysearch(65, items))
print(binarysearch(150, items))
