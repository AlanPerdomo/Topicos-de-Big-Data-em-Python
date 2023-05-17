import pandas as pd

data = {
    'name': ["Anastasia", "Dimas", "Katherine", "James", "Emily", "Michael", "Matthew", "laura", "Kevin", "Jonas"],
    'score': [12.5, 9.0, 16.5, 10.3, 9.0, 20.0, 14.5, 8.2, 8.0, 19.0],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes",]
}
df = pd.DataFrame(data)

questao_A = df[df['attempts'] > 2]['name']
print("Pessoas que tiveram mais que 2 tentativas: \n", questao_A)

df['qualify'] = df['qualify'].apply(lambda x: 'Sim' if x == 'yes' else 'Não')

questao_C = df[df['score'] < 10.0]['name']
print("Pessoas com pontuação menor que 10.0: \n", questao_C)

questao_D = df[df["qualify"] == "Sim"]["name"]
print("Pessoas com Quelificação positiva: \n", questao_D)

questao_E = df[["name", "score"]]
print("Nome e pontuação das pessoas: \n", questao_E)

questao_Fmed = df["score"].mean()
questao_Fmod = df["score"].mode()
print("Média: ", questao_Fmed)
print("Moda: ", questao_Fmod)

questao_G = df.sort_values(by="score", ascending=False)
print("Dataframe ordenado por pontuação: \n", questao_G)

questao_H = df.describe()
print("Estatisticas: \n", questao_H)
