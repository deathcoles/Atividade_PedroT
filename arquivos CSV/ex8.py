import csv
import os

pasta = os.path.dirname(os.path.abspath(__file__))
caminho_notas = os.path.join(pasta, "notas.csv")
caminho_aprovados = os.path.join(pasta, "aprovados.csv")
caminho_reprovados = os.path.join(pasta, "reprovados.csv")

with open(caminho_notas, "r", encoding="utf-8") as arquivo_entrada, \
     open(caminho_aprovados, "w", encoding="utf-8", newline="") as arq_aprovados, \
     open(caminho_reprovados, "w", encoding="utf-8", newline="") as arq_reprovados:
    
    leitor = csv.DictReader(arquivo_entrada)
    campos_saida = ["nome", "media", "situacao"]
    
    escritor_aprovados = csv.DictWriter(arq_aprovados, fieldnames=campos_saida)
    escritor_aprovados.writeheader()
    
    escritor_reprovados = csv.DictWriter(arq_reprovados, fieldnames=campos_saida)
    escritor_reprovados.writeheader()
    
    for linha in leitor:
        nota1 = float(linha["nota1"])
        nota2 = float(linha["nota2"])
        nota3 = float(linha["nota3"])
        media = (nota1 + nota2 + nota3) / 3
        
        dados_aluno = {
            "nome": linha["nome"],
            "media": f"{media:.2f}"
        }
        
        if media >= 6:
            dados_aluno["situacao"] = "Aprovado"
            escritor_aprovados.writerow(dados_aluno)
        else:
            dados_aluno["situacao"] = "Reprovado"
            escritor_reprovados.writerow(dados_aluno)