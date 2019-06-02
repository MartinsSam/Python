nome = input('Qual é seu nome?')
#String Treat
#print('Prazer em te conhecer {}!' .format(nome))
#print('Prazer em te conhecer {:>20}!'.format(nome))
#print('Prazer em te conhecer {:<20}!'.format(nome))
#print('Prazer em te conhecer {:^20}!'.format(nome))
#print('Prazer em te conhecer {:=^20}!'.format(nome))

#Number Treat
n1 = int(input('Primeiro Valor:'))
n2 = int(input('Segundo Valor:'))
s = n1+n2
m = n1*n2
d = n1/n2
d1 = n1//n2
e = n1 ** n2
print('A soma vale {}' .format(n1+n2))
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}' .format(d1, e))