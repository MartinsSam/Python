'''
PRIMEIRA FORMA DE UTILIZAR O MÓDULO
import <libraryName> --> importar todas as funcionalidades da biblioteca
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz do número {0} é {1}'.format(num, raiz))
print('O resultado inteiro (arredondado para cima) do número {} é {:.2f}'.format(num, math.ceil(raiz)))
'''

'''
SEGUNDA FORMA DE UTILIZAR O MÓDULO

'''
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz do número {0} é {1}'.format(num, raiz))
print('O resultado inteiro (arredondado para cima) do número {} é {:.2f}'.format(num, floor(raiz)))
