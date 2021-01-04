def bubbleSort(dataset):
    for i in range(len(dataset)-1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j + 1]:
                temp = dataset[j]
                dataset[j] = dataset[j + 1]
                dataset[j + 1] = temp

            print("Current state: ", dataset)

def main():
    list1 = [4, 23, 9, 5, 12, 65, 72, 3, 91, 53]
    print("Starting state: ", list1)
    bubbleSort(list1)
    print("Final state: ", list1)

if __name__ == "__main__":
    main()