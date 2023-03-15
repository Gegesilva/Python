'''
#Dicionarios

#OBS: em algumas liguagens são conhecidos por mapas
#Dicianarios são representados por {}
#chave e valor são separados por dois pontos, ambos podem ser de qualquer tipo de dados e podem ser misturados

print(type({}))
--------------------------------------------------------------------------------------------------------------------
#criação de dicionarios

#Forma mais comum
paises =  {'br:' 'Brasil', 'eua:' 'Estados Unidos', 'py:' 'Paraguay'}

print(paises)
print(type(paises))

#menos comum

paises = dict(br='Brasil', eua='Estados unidos', py='Paraguay')

print(paises)
---------------------------------------------------------------------------------------------------------------
#acessando elementos

paises = dict(br='Brasil', eua='Estados unidos', py='Paraguay')

#acessando via chave (usado colchetes)

print(paises['br'])

#utilizando get (recomendado)

print(paises.get('eua'))

#utilizando o get o retorno quendo não ouver a chave procurada será None, não um erro como o acesso via chaves, geraria muito codigo de tratameto

print(paises.get('ru'))
---------------------------------------------------------------------------------------------------------------
#exemplo
#aqui funciona normalmente
paises = dict(br='Brasil', eua='Estados unidos', py='Paraguay')

pais = paises.get('ru')

if pais:
    print('Encotrado')
else:
    print('Não encontrado')



#aqui apresenta erro



pais = paises['ru']

if pais:
    print('Encotrado')
else:
    print('Não encontrado')
#exemplo2

paises = dict(br='Brasil', eua='Estados unidos', py='Paraguay')

pais = paises.get('ru', 'não') #o segundo parametro e fixo se não for encontrado o dado buscado
print(f'Encontrei o {pais}')


paises = dict(br='Brasil', eua='Estados unidos', py='Paraguay')
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises) #não busca por valor somente pela chave

if 'br' in paises:
    russia = paises['br']
------------------------------------------------------------------------------------------------------------------------
#podemos utilizar varios tipo de dados

#tuplas são interessantes para serem usadas com chave pois são imutáveis
localidades = {
    (35.6895, 396917): 'Tokio',
    (40.7120, 74.0060): 'Nova York',
    (37.7749, 122.4194): 'São Paulo'
}

print(localidades)
print(type(localidades))
------------------------------------------------------------------------------------------------------------------------
#adicionar elementos no dicionario

receita = {'jan': 100, 'fev': 150, 'mar': 200}

#forma mais comum
receita['ABR'] = 300
#
novoDado = {'MAI': 400}
#
receita.update(novoDado) #receita.uodate({'mai': 400}) poderia ser assim tbm


print(receita)

print(type(receita))

------------------------------------------------------------------------------------------------------------------------
# atualizando um dicionario (OBS: Não podemos ter chaves repetidas)
#forma 1
receita['MAI'] = 450

#forma 2
receita.update({'jan': 30000})

print(receita)
------------------------------------------------------------------------------------------------------------------------
#remover dados de um dicionário

receita = {'jan': 100, 'fev': 150, 'mar': 200}

#forma 1 - mais comum
ret = receita.pop('mar')  #Aqui precisamos sempre informar a chave/do contrario teremos um erro

print(ret) #Quando removemos um valor ele retorne este valor durante a operação

print(receita)

#forma 2

del receita['fev'] #não retorna valor


print(receita)

#OBS: Se a chave não existir será gerado um erro
------------------------------------------------------------------------------------------------------------------------

#ideia de utilização
#Lista
carrinho = []

produto1 = ['Playstation4', 1, 2300.00]
produto2 = ['Godofwar', 1, 100.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
#OBS: Neste caso teriamos que saber o indice de cada produto
'''

#Tupla
carrinho = []

produto1 = ['Playstation4', 1, 2300.00]
produto2 = ['Godofwar', 1, 100.00]

carrinho = (produto1, produto2)

print(carrinho)
