import csv

with open("notas.csv", "r", encoding="utf-8") as arquivo:
    
    # a)
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        
        # b)
        nota1 = float(linha["nota1"])
        nota2 = float(linha["nota2"])
        nota3 = float(linha["nota3"])
        media = (nota1 + nota2 + nota3) / 3
        
        # c)
        if media >= 6:
            status = "Aprovado(a)"
        else:
            status = "Reprovado(a)"
            
        print(f"{linha['nome']} - Média: {media:.2f} - {status}")