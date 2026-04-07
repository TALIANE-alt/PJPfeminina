def saudacao ():
    print('Olá, aluno!')

saudacao ()

def vlade(ssss):
    print(f'Olá, {ssss}')



vlade('segundamos fia')

#exemplo de soma

def soma(a, b, c):
    valor = a + b + c
    print(valor)

soma(5, 10, 15)

#exemplo de soma com lista


def soma(lista_valores):

    soma_valores = 0
    for valor in lista_valores:
        soma_valores += valor

    print('Esse mês suas compras deram:' , soma_valores)

lista = [20, -74, 56, 89, 12]
soma(lista)