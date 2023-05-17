import pandas as pd
import random

array = []
for num in range(5):
    index = random.randint(0, 1000)
    array.append(index)

serie = pd.Series(array)
serie_ordenada = serie.sort_values()

print(serie_ordenada)
