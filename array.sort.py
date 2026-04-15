numeros = [45, 12, 89, 3, 67, 21, 90, 34, 56, 1, 78, 23, 9, 100, 15]

print("Array original de números:")
print(numeros)

numeros.sort()
print("\nNúmeros em ordem crescente:")
print(numeros)

numeros.sort(key=None, reverse=True)
print("\nNúmeros em ordem decrescente:")
print(numeros)

strings = ["nome", "dataNascimento", "cpf", "rg", "endereco", "telefone"]

print("\nArray original de strings:")
print(strings)

strings.sort()
print("\nStrings em ordem crescente:")
print(strings)

strings.sort(key=None, reverse=True)
print("\nStrings em ordem decrescente:")
print(strings)