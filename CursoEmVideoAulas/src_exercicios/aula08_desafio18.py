from math import cos, sin, tan, radians

ang = float(input('Digite um ângulo:'))
angRadian = radians(ang)
coseno = cos(angRadian)
seno = sin(angRadian)
tangente = tan(angRadian)

print('Ângulo: {:.2f} \n SEN: {:.2f} \n COS: {:.2f} \n TAN: {:.2f}' .format(ang, seno, coseno, tangente))
