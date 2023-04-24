import re
nomes = ['nadia','marcos','norman','nvidia']
padrao = '^n...a$'

for palavras in nomes:
    resultado = re.match(padrao, palavras)
    if resultado:
        print("ok!")
    else:
        print("not ok!")