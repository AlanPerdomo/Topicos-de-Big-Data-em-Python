import pandas as pd

serie1 = pd.Series([1, 2, 3, 4])
serie2 = pd.Series([5, 6, 7, 8])

soma = serie1 + serie2
subtracao = serie1 - serie2
multiplicacao = serie1 * serie2 
divisao = serie1 / serie2

print("Soma: ",soma)
print("Subtração: ",subtracao)
print("Multiplicação: ",multiplicacao)
print("Divisão: ",divisao)