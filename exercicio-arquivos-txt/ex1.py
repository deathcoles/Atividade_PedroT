with open('frutas.txt', 'w', encoding='utf-8')as arquivo:
    arquivo.write("Maçã\n")
    arquivo.write("Peira\n")
    arquivo.write("Mamão\n")
    arquivo.write("Abacate\n")
    arquivo.write("Abacaxi\n")
    arquivo.write("Abil\n")

with open('frutas.txt', 'r', encoding='utf-8')as arquivo:
    conteudo = arquivo.read()
    print(conteudo)