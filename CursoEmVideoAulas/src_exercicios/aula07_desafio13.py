salario = float(input('Digite o salário do funcionário:'))
#Não definir o aumento como hard coded
aumento = 0.15
#1.0 representa 100 do salario já existente
novoSalario = salario * (1.0+aumento)
print('O novo salario reajustado é de {:.2f}' .format(novoSalario))
