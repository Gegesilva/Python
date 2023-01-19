ativo = True
logado: bool = False

if ativo or logado:
    print('bem vindo')
else:
    print('Acesse seu email, para ativar')


if ativo and logado:
    print('bem vindo')
else:
    print('Acesse seu email, para ativar')

