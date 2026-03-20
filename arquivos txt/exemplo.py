with open ("teste.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")
    
with open ("teste.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Terceira linha\n")

with open ("teste.txt", "r", encoding="utf-8") as arquivo:    
    conteudo = arquivo.read()
    print(conteudo)
    