import pandas as pd

serie1 = pd.Series([1,2,3,4,5])
serie2 = pd.Series([22,33,44,55,66])

soma = serie1 + serie2
subtracao = serie1 - serie2
multiplicacao = serie1 * serie2
divisao = serie1 / serie2

print("Soma: \n", soma)
print("Subtração: \n", subtracao)
print("Multiplicação: \n", multiplicacao)
print("Divisao: \n", divisao)