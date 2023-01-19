"""
var = 'e'
lista = lista5

if var in lista:
    print(f'esta aqui {var}')
else:
    print(f'não {var}')

lista5.sort()
print(lista5)

print(lista5.count('e'))

lista1.append(42)

lista1.append([1, 2, 3, 4, 50])

lista1.extend([12, 99, 32])

print(lista1)

if [1, 2, 3, 4, 50] in lista1:
    print('tem')
else:
    print('não tem')

    lista1.extend([12, 99, 32])


lista2.insert(2, 'novo valor')

lista6 = lista1 + lista2

lista5 += 'Curso legal'

lista1.reverse()

lista2.insert(2, 'novo valor')

lista6 = lista1 + lista2

lista5 += 'Curso legal'

lista1.reverse()


lista1 = [1, 55, 54, 15, 12, 3]

lista2 = ['a', 'f', 't', 'gee', 'gege', 'mm', 'uu']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek university')

print(lista5.pop(3))

print(lista5)

print(lista1 * 3)


curso = 'Programação em python essencial'

curso = curso.split()

print(curso)



lista6 = ['Programação', 'em', 'python', 'essencial']

curso = ' '.join(lista6)

print(curso)


lista = [1, 2.32, 'd', 'opa', 121232132, [123]]

for elem in lista:
    print(elem)


carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto ou digite sair')
    produto = input('Digite: ')
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
num1 = 1
num2 = 2
num3 = 3
num4 = 4

numeros = [num1, num2, num3, num4]

print(numeros)

print(numeros[0])
print(numeros[-2])


for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1


cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
    print(indice, cor)
"""


numeros = [6, 5, 9, 10, 5]

print(numeros.index(5))
print(numeros.index(5, 2))

