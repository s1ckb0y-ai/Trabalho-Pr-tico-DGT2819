array = [45, 12, 89, 3, 67, 21, 90, 34, 56, 1, 78, 23, 9, 100, 15]

print("Array original:")
print(array)

for i in range(len(array)):
    menor_indice = i

    for j in range(i + 1, len(array)):
        if array[menor_indice] > array[j]:
            menor_indice = j

    array[i], array[menor_indice] = array[menor_indice], array[i]

print("\nArray ordenado com Selection Sort:")
print(array)