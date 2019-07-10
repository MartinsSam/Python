numero = float(input('Digite um valor(em metros):'))
#print('O valor {}, convertido para centimetros é {:.0f} ' .format(numero, numero*100))
# km hm dam m dc cm mm

km = numero/1000
hm = numero/100
dam = numero/10
dc = numero*10
cm = numero*100
mm = numero*1000
print('O valor {}, corresponde a \n {}km, \n {}hm \n {}dam \n {:.0f}cm, \n {:.0f}mm \n {}dc'.format(numero, km, hm, dam, cm, mm, dc))

