#SFM 05/2019
# A versão 3.7 do Python utiliza uma nova forma de formatação
# Python sempre recebe o valor como String. É necessário conversão para poder realizar a soma.
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
s = n1+n2
print('Versão 3.6 - A soma entre {0} e {1} é: {2}' .format(n1, n2, s))
print(f'Versão 3.7 - A soma entre {n1} e {n2} é: {s}')
