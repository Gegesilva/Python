nome = input('Qual seu nome?')

print('Seja bem vindo %s' % nome)

idade = input('Qual sua idade')

print('A %s tem %s anos' %- (nome, idade))

# forma mais antigo de exibir o print a nova e a .format()

print(f'Seja bem vindo {nome} vc tem {idade} anos')

print(f'Vc nasceu em {2022 - int(idade)}')
