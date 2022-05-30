# IMC

print('-='*21)
print('\tCalculador de IMC')
print('-='*21)

peso = float(input('Insira o peso: '))
altura = float(input('Insira a altura: '))
imc = peso/altura**2
print('-='*21)
print(f'O seu IMC é: {imc:.2f}')

if imc < 18.5: 
  print('Você está abaixo do peso.')
elif imc > 18.5 and imc < 24.9:
  print('Você está no peso normal - Eutrofia')
elif imc > 25 and imc < 29.9:
  print('Acima do peso - Sobre peso, pré-obesidade')
elif imc > 30 and imc < 34.9:
  print('Obesidade I - Moderada')
elif imc > 35 and imc < 39.9:
  print('Obesidade II - Severa')
else:
  print('Obesidade III - Muito Severa')

print('-='*21)