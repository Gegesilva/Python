'''
#mapas = conhecidos como Dicionarios em python
   #São representados por {}

   #iterar(loop) sobre dicionarios

for chave in receita:
    print(chave) #imprimindo chave

for chave in receita:
    print(receita[chave]) #imprimindo valores

for chave in receita:
    print(f'{chave}: recebi R${receita[chave]}') #imprimindo chave valor
------------------------------------------------------------------------------------------------------------------------

'''

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

print(receita.keys()) #tras um dicionario de chaves


for chave in receita.keys():
    print(receita[chave])
