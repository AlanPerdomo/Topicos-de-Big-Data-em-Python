import re
#   1 se a função lambda para mapear (map) elementos de uma lista e calcular o dobro de cada um
#   desses elementos. Exemplo:
#   Entrada: [2, 3, 4, 5, 18]
#   Saída: [4, 6, 8, 10, 36]

lista = [2, 3, 4, 5, 18]
print(list(map(lambda x: x*2,lista)))


#   2 Use a função lambda para filtrar (filter) os números pares dos elementos de uma lista. Exemplo:
#   Entrada: [1, 2, 3, 7, 5, 18]
#   Saída: [2, 18]

lista2 = [1, 2, 3, 7, 5, 18]
print(list(filter(lambda x: (x % 2 ==0),lista2)))

#   3 Gere uma lista de 1 até 20 que filtre (filter) juntamente com o lambda os números múltiplos de 3.
#   Entrada: lista de 1 até 20
#   Saída: [3, 6, 9, 12, 15, 18]

lista3 = range(1,21)
print(list(filter(lambda x: (x % 3 == 0),lista3)))

#   4 Expressões Regulares: Leia um arquivo txt com as palavras abaixo e imprima quantas palavras com
#   as seguintes regras no texto lido:
#   Texto: a ab ba baa bab bba baa bbb aaa bab baaa abbb baabaa bbbbab
#   baa
#   Regras:
#   a. Tem uma (1) letra “b” no início da string e nenhuma ou várias letras “b”.
#   b. A string inicia com nenhuma ou várias letras “a” e termina com um (1) b.

texto = open("Tópicos de Big Data em Python/texto.txt","r")
palavras = texto.read().split()
padraoA = '^b(b*)$'
padraoB = '(a*)b$'
a = 0
b = 0
for i in palavras:
    resultA = re.search(padraoA, i)
    if resultA:
        a += 1
    resultB = re.search(padraoB, i)
    if resultB:
        b += 1
print("seguindo as regras 'a' foram", a ,"palavras.")
print("seguindo as regras 'b' foram", b ,"palavras.")

#   5 Expressões Regulares: Leia um arquivo txt com os e-mails abaixo e imprima os gmails e a
#   quantidade desses e-mails.
#   Email’s:
#   zacarias@gmail.com
#   fulano.oli@yahoo.com
#   jose.costa@gmail.com
#   juca@gmail.com
#   feliciana@outlook.com

email = open("Tópicos de Big Data em Python/emails.txt","r").read().split()
sum_emails = 0
for i in email:
    resultado = re.search('@gmail', i)
    if resultado:
        sum_emails += 1
print(sum_emails, "e-mails com gmail.")

