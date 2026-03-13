lista = []

for i in range(1,11):
    if i <= 10:
        lista.append(i)
        
#a)
print(lista[0:4])

#b)
print(lista[7:10])

#c) 
posicoes_pares = lista[::2]
print(posicoes_pares)