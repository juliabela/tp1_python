#1. Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive. 
# O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.

soma = 0
for i in range (10):
    n = int (input("Digite um número : "))

    if n % 2 != 0:
        soma += n
        
print (soma)