estados = ['amapá', 'pará', 'paraná', 'santa catarina']
numeros = [1, 2, 3, 4]

print('Primeiro estado:', estados [0])
print('Ultimo estado:', estados [-1])

estados[2] = 'acre'
print('Após alterar:', estados)

estados.append('Brasilia')
estados.insert(1, 'pernambuco')
print('Após adicionar:', estados)

estados.remove('Brasilia')

print("Após remover 'Brasilia'", estados)

ultima = estados.pop()
print('Última removida:', ultima)





