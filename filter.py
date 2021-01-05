items = ["banana", "pear", "orange", "apple", "apple",
         "orange", "kiwi", "pear", "banana", "banana",
         "kiwi", "orange", "pear", "apple", "orange"]

filter = dict()

for item in items:
    filter[item] = 0

result = set(filter.keys())
print(result)