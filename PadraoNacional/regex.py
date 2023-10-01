import re

padrao1 = "[0-9][a-z][0-9]"
texto1 = "123 1a2 1cc aa1"
resposta1 = re.search(padrao1, texto1)

print(resposta1)


padrao2 = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto2 = "aaabbbcc rodrigo123@gmail.com.br"
resposta2 = re.search(padrao2, texto2)

print(resposta2.group())
