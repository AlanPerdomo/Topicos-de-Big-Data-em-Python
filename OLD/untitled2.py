# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mea-lhyCe-8HZBMZWzF8ARKa-PLlOHn7
"""

from collections import Counter
print(Counter("mississippi"))

palavra = "mississipi"
contador = {}
for i in palavra:
  if not contador.get(i):
    contador[i] = palavra.count(i)

print(contador)

from collections import Counter

itens = Counter("mississippi")
itens = Counter(itens)
print(itens)

itens.update("missouri")
print(itens)

from collections import Counter

#with sequence of items 
print(Counter(['B','B','A','B','C','A','B','B','A','C']))

#with dictionary
print(Counter({'A':3,'B':5,'C':2}))

#with keyword arguments
print(Counter(A=3,B=5,C=2))

from collections import Counter

lista = Counter(['B','B','A','B','C','A','B','B','A','C'])

frequente = lista.most_common(2)
print("Elemento + comum ", frequente)