import csv
import os

pasta = os.path.dirname(os.path.abspath(__file__))
caminho_notas = os.path.join(pasta, "notas.csv")
caminho_saida = os.path.join(pasta, "notas_com_media.csv")

with open(caminho_notas, "r", encoding="utf-8") as arquivo_entrada, \
     open(caminho_saida, "w", encoding="utf-8", newline="") as arquivo_saida:
    
    leitor = csv.DictReader(arquivo_entrada)
    campos = leitor.fieldnames + ["media"]
    
    escritor = csv.DictWriter(arquivo_saida, fieldnames=campos)
    escritor.writeheader()
    
    for linha in leitor:
        nota1 = float(linha["nota1"])
        nota2 = float(linha["nota2"])
        nota3 = float(linha["nota3"])
        
        linha["media"] = f"{(nota1 + nota2 + nota3) / 3:.2f}"
        escritor.writerow(linha)