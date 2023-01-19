valor = 1
cont = 0
soma = 0

while cont < 10:
    valor = int(input('Digite: '))
    soma += valor
    cont += 1
    print(soma)

result = soma / cont

print(soma, cont)
print(result)
