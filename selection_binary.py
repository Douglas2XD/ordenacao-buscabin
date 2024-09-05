interacao = 0

def swap(array,i,menor):
    array[i], array[menor] = array[menor],array[i]
    return array

def SelectionSort(array):
    for i in range(0,len(array)):
        menor = i
        for j in range(i+1,len(array)):
            if array[j] < array[menor]:
                menor = j
        swap(array,i,menor)

    return array


def BinarySearch(array, busca, inicio, meio, fim):
    global interacao
    if busca > fim or busca < inicio:
        interacao +=1
        return f'O VALOR: {busca} NÃO FOI ENCONTRADO!'

    if busca == array[meio]:
        interacao += 1
        return f'valor encontrado: {array[meio]}'


    elif busca > array[meio]:
        inicio = meio + 1
        meio = (inicio + fim) // 2
        interacao += 1

    elif busca < array[meio]:
        fim = meio - 1
        meio = (inicio + fim) // 2
        interacao += 1

    return BinarySearch(array, busca, inicio, meio, fim)

arr = [11,10,9,8,7,6,5,4,3,2,1]
arr = SelectionSort(arr)

print("ARRAY ORGANIZADO: ")
print(arr)
print("-="*20)
meio = len(arr) // 2
ponteiro = 11
busca = BinarySearch(arr, ponteiro, 0, meio, len(arr))

print(busca)
print("-="*20)
print(f"TOTAL DE INTERAÇÕES: {interacao}")
