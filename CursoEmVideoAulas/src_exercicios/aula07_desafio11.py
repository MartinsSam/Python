largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = largura*altura
#2 em qtdeTinta significa quantos metros cada litro de tinta pinta
qtdeTinta = area/2;
print('Sua parede tem a dimensão de {}x{}, e sua área é de {:.2f}m²' .format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta' .format(qtdeTinta))
