lista = input("Digite os valores: ").split()
def bubble_sort(lista):
  fim = len(lista)
  while fim > 1:
    troca = False
    pos= 0
    while pos < (fim -1):
      if lista[pos] > lista[pos+1]:
        troca = True
        temp = lista[pos]
        lista[pos] = lista[pos+1]
        lista[pos+1] = temp
      pos +=1
    if not  troca:
      break
    return lista

#lista = 3 78 91 1 4 5 23 21 90 09 0
# Chamada da função: bubble_sort(lista)




