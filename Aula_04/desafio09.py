# Implementação do algoritmo de ordenação por seleção
lista = [64, 34, 25, 12, 22, 11, 90]

def ordenar_lista_numeros(numeros):
    nova_lista = numeros.copy()
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return nova_lista

# Ordenando a lista
ordenada = ordenar_lista_numeros(lista)
print("Lista original:", lista)