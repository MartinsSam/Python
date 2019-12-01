#Desafio 17
from math import pow, sqrt
catetoOp = float(input('Digite o comprimento do cateto oposto: '))
catetoAdj = float(input('Digite o comprimento do cateto adjacente: '))

#resHip = pow(pow(catetoOp, 2) + pow(catetoAdj, 2), 0.5)
resHip = sqrt(pow(catetoOp, 2) + pow(catetoAdj, 2))

print('A hipotenusa possui comprimento de {:.2f}' .format(resHip))