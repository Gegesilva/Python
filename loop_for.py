
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)
"""
for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in numeros:
    print(numero)


print(nome[0:5])
print(nome[5:17])

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, valor in enumerate(nome):
    print(indice)
    
    
quantidade = int(input("Ate quando este loop vai rodar?"))

for contador in range(1, quantidade + 1):
    pri nt(f'imprimindo {contador}', end='')
"""

emoji = 'U0001F60D'

for x in range(3):
    for num in range(1, 11):
        print(f'\U0001F60D' * num)
