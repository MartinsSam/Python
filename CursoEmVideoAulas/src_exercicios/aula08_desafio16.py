#Desafio 16
#Pode utilizar int() ao invés de trunc
from math import trunc

num = float(input('Digite um número real: '))
intNum = trunc(num)
print('O valor inteiro de {}, é {}'.format(num, intNum))
