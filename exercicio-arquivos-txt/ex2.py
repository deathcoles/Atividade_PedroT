with open('compras.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        item = input("Digite um item (ou 'sair' para terminar): ")
        
        if item == 'sair':
            break
            
        arquivo.write(item + '\n')


with open('compras.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())