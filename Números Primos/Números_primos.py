# Números Compostos e Primos
# Se o número é composto ou primo
# Se composto, exibe todos os números que são múltiplos 

n = int(input("Verificar números primos até: "))
mult=0

print('-='*21)
for num in range(2,n):
    if (n % num == 0):
        print(" - Múltiplo de", num)
        mult += 1

if(mult==0):
    print("É um número PRIMO!")
else:
    print('-='*21)
    print("Número COMPOSTO que possui", mult, "múltiplos acima de 2 e abaixo de", n)

