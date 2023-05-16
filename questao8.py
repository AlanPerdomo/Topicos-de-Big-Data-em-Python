from collections import defaultdict

with open('nomes_alunos.txt', 'r') as file:
    nomes_alunos = file.readlines()

frequencia_nomes = defaultdict(int)

for nome_completo in nomes_alunos:
    nome = nome_completo.strip().split()[0].lower() 
    frequencia_nomes[nome] += 1

print(frequencia_nomes)