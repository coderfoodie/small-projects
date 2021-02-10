FibArray = [0, 1]

# Method 1
# def Fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     elif n <= len(FibArray):
#         return FibArray[n-1]
#     else:
#         temp_fib = Fibonacci(n-1) + Fibonacci(n-2)
#         FibArray.append(temp_fib)
#         return temp_fib

# Mthod 2
# def Fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#         return b

# Method 3
def Fibonacci(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

    if __name__ == "__main__":
        print(Fibonacci(int(input("Enter the term: "))))

# print(Fibonacci(9))