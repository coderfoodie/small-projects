x = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

y = [[9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]

# using for loop

# result = [[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]]

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j] + y[i][j]
# for r in result:
#     print(r)

#using nested list

# result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]

# for r in result:
#     print(r)

# using zip() and sum

result = [map(sum, zip(*t)) for t in zip(x, y)]
print(result)