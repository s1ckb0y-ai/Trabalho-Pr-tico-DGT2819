def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


numeros = [45, 12, 89, 3, 67, 21, 90, 34, 56, 1, 78, 23, 9, 100, 15]

print("Array original:")
print(numeros)

bubbleSort(numeros)

print("\nArray ordenado com Bubble Sort:")
print(numeros)