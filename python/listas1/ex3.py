numeros = [3, 17, 8, 42, 5, 100, 23, 66, 11, 99]
#a)
for num in numeros:
    if num % 2 == 0:
        print(num)
        
#b)
maior_q_20 = []

for numero in numeros:
    if numero > 20:
        maior_q_20.append(numero)
        
print(maior_q_20)

#c)
soma_total = sum(numeros)
print(soma_total)