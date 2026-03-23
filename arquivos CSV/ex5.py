with open("turma.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("nome,nota1,nota2\n")
    
    for i in range(3):
        print(f"\n--- Dados do Aluno {i+1} ---")
        nome = input("Digite o nome: ")
        nota1 = input("Digite a primeira nota: ")
        nota2 = input("Digite a segunda nota: ")
        
        arquivo.write(f"{nome},{nota1},{nota2}\n")

print("\nArquivo 'turma.csv' criado com sucesso!")