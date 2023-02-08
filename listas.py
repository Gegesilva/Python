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


    numeros = [6, 5, 9, 10, 8, 5]

print(numeros.index(5))
print(numeros.index(5, 2))
print(numeros.index(5, 3))


print(numeros.index(8, 0, 5))
----------------------------------------------------------------------------------------------------------
#slicing
# lista [inicio:fim:passo] forma de utilização so slicing

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista[2:])
#podemos usar negativo

print(lista[-3:])

#trabalhando com o parametro de fim

print(lista[:4])

#utilizando o passo

print(lista[::-1])

nome = 'george da silva rodrigues'

print(nome[::2])

-----------------------------------------------------------------------------------------------------------------

#invertendo valores

nomes = ['George', 'Silva']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes.reverse()
print(nomes)
-------------------------------------------------------------------------------------------------------------------------------
#soma* valor maximo, valor minimo, tamanho
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

-----------------------------------------------------------------------------------------------------------------------------------
#transformar lista em tupla

lista = [1, 2, 3, 4, 5, 6]

print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
-------------------------------------------------------------------------------------------------------------------
#desenpacotamento de litas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

#OBS: não pode haver mais elementos que variaveis o mesmo acontece ao contrario
--------------------------------------------------------------------------------------------------------------------
#copiando uma lista para outra (Shalow Copy, Deep Copy)

#Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(nova)
#OBS: Uma copia de lista se torna outra lista não têm nenhuma relação podemos modificar uma e não afetará a outra
#chamamos isso de Deep Copy
_------------------------------------------------------------------------------------------------------------------------------------
"""



#Forma 2

lista = [1, 2, 3]

nova = lista

print(nova)

nova.append(4)

print(lista)
print(nova)
#OBS: Neste caso as duas listas são modificadas chammos isso de Shallow Copy
-----------------------------------------------------------------------------------------------------------------------------------------------