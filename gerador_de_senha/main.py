#geredor de senhas seguras
import random

letra_maiuscula = chr(random.randint(65,90))
letra_minuscula = chr(random.randint(97,122))
char_especial = chr(33)
lista_numero = []

for i in range(5):
    numeros = random.randrange(9)
    lista_numero.append(numeros)

random.shuffle(lista_numero)
lista_numero = str(lista_numero) [1:-1]
lista_numero = lista_numero.replace(',','')

print(letra_maiuscula,letra_minuscula,lista_numero,char_especial)
