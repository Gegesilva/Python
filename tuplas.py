
Tuple

Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças:
1- As tuplas são reprentadas por parenteses ()
2- As tuplas são imutáveis (toda operção em uma tupla gera uma nova)

tupla1 = (1, 2, 3, 4, 5, 6)
----------------------------------------------------------------------------------------------------------------
#podem ser declaradas sem o uso dos parenteses também ex:
tupla2 = 1, 2, 3, 4, 5, 6

print(type(tupla1))
print(type(tupla2))
----------------------------------------------------------------------------------------------------------------
#Tuplas com um elemento
tupla3 = (4) #isto não e uma tupla, sim um inteiro

print(type(tupla3))

tupla4 = (4,) #isso sim e uma tupla apenas adicionando uma virgula

print(type(tupla4))

#Outro exemplo

tupla5 = 4, #isso e uma tupla a tupla e definida pela virgula

print(type(tupla5))

-------------------------------------------------------------------------------------------------------------------------
#tupla utilizando range lembrando que o range tem (inicio, fim, passo) podem ser setados no parenteses

tupla = tuple(range(0, 11, 2))

print(tupla)

#desenpcotamento de tupla

tupla1 = ('George', 'Silva')

Nome, sobrenome = tupla1

print(Nome, sobrenome)

Adições e remoções não existem, são imutaveis
-----------------------------------------------------------------------------------------------------------------
#Operações em tuplas

tupla = 1, 2, 3, 4, 5

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
--------------------------------------------------------------------------------------------------------------------
#concatenando tuplas

tupla1 = (1, 2, 3)
tupla = (4, 5, 6)

print(tupla1 + tupla)
print(tupla)
print(tupla1)
---------------------------------------------------------------------------------------------------------------------------
#não há alteração nas tuplas somente se criarmos uma nova

tupla3 = tupla1 + tupla

print('Tupla3: ', tupla3)
--------------------------------------------------------------------------------------------------------------------------
#podemos sobrescrever uma tupla

tupla1 = tupla1 + tupla

print(tupla1)

print(4 in tupla)
--------------------------------------------------------------------------------------------------------------------------------
#iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
-------------------------------------------------------------------------------------------------------------------------------
#Contando elementos dentro de uma

tupla = ('a', 'd', 'd', 'q', 'a')

print(tupla.count('a'))

nome = tuple('George da Silva Rodrigues')
print(nome)
print(nome.count('e'))
-------------------------------------------------------------------------------------------------------------------------------
#Numerando os dados da tupla

meses = ('janeiro',
         'fevereiro',
         'março',
         'abril',
         'maio',
         'junho',
         'julho',
         'agosto',
         'setembro',
         'outubro',
         'novembro',
         'dezembro'
         )

i = 0
while i < len(meses):
    print(i, meses[i])
    i += 1
----------------------------------------------------------------------------------------------------------------------------------
# Verificando em qual indice um elemento esta na tupla

print(meses.index('junho', 3))
------------------------------------------------------------------------------------------------------------------------------------
#Slicing
-------------------------------------------------------------------------------------------------------------------------
print(meses[0:8])
---------------------------------------------------------------------------------------------------------------------------
#copiando uma tupla

tupla = (1, 2, 3, 4, 5)
teste = ('Soma', 6, 7, 8)

nova = tupla

print(nova)

nova += teste

print(nova)






