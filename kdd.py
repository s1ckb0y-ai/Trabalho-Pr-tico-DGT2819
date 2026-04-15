import time


def bubble_sort(lista):
    array = lista.copy()

    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def selection_sort(lista):
    array = lista.copy()

    for i in range(len(array)):
        menor_indice = i

        for j in range(i + 1, len(array)):
            if array[menor_indice] > array[j]:
                menor_indice = j

        array[i], array[menor_indice] = array[menor_indice], array[i]

    return array


def sort_nativo(lista):
    array = lista.copy()
    array.sort()
    return array


def ler_palavras(nome_arquivo):
    palavras = list()

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras_linha = linha.split()

            for palavra in palavras_linha:
                palavras.append(palavra)

    return palavras


def medir_tempo(funcao, lista):
    inicio = time.time()
    resultado = funcao(lista)
    fim = time.time()

    tempo_execucao = fim - inicio
    return resultado, tempo_execucao


def salvar_palavras(nome_arquivo, palavras):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")


palavras = ler_palavras("palavras.txt")

print("Palavras lidas do arquivo:")
print(palavras)
print("-" * 50)

resultado_bubble, tempo_bubble = medir_tempo(bubble_sort, palavras)
resultado_selection, tempo_selection = medir_tempo(selection_sort, palavras)
resultado_sort, tempo_sort = medir_tempo(sort_nativo, palavras)

print("Resultado Bubble Sort:")
print(resultado_bubble)
print(f"Tempo Bubble Sort: {tempo_bubble:.8f} segundos")
print("-" * 50)

print("Resultado Selection Sort:")
print(resultado_selection)
print(f"Tempo Selection Sort: {tempo_selection:.8f} segundos")
print("-" * 50)

print("Resultado sort() nativo:")
print(resultado_sort)
print(f"Tempo sort() nativo: {tempo_sort:.8f} segundos")
print("-" * 50)

tempos = {
    "Bubble Sort": tempo_bubble,
    "Selection Sort": tempo_selection,
    "sort() nativo": tempo_sort
}

melhor_metodo = min(tempos, key=tempos.get)

print(f"Melhor desempenho: {melhor_metodo}")

if melhor_metodo == "Bubble Sort":
    palavras_ordenadas = resultado_bubble
elif melhor_metodo == "Selection Sort":
    palavras_ordenadas = resultado_selection
else:
    palavras_ordenadas = resultado_sort

salvar_palavras("palavras_ordenadas.txt", palavras_ordenadas)

print("Arquivo palavras_ordenadas.txt criado com sucesso.")