items = ["banana", "pear", "orange", "apple", "apple",
         "orange", "kiwi", "pear", "banana", "banana",
         "kiwi", "orange", "pear", "apple", "kiwi"]

counter = dict()

for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1
        
print(counter)