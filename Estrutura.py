nota = 10

#condicional para avaliar notas

if nota >= 0 and nota < 3:
    categoria = 'Reprovado'

elif nota >= 3 and nota < 7:
    categoria = 'Recuperação'
 
else:
    categoria = 'Aprovado'

print('você está' , categoria)

#ATIVIDADE DE CONDICIONAL

#pedir para digitar a idade e avaliar conforme categoria

idade = int(input('Digite sua idade:'))

if idade >= 0 and idade <= 12:
    categoria ='Criança'
elif idade >= 13 and idade <= 17:
    categoria = 'Adolescente'
elif idade >= 18 and idade <= 59:
    categoria = 'Adulto'
else:
    categoria = 'Idoso'

print('Você é' , categoria)

#aluno digita uma nota de 0 a 10 e sistema classifica conforme condições

nota = float(input('Digite sua nota:'))

if nota >= 9:
    categoria = 'Excelente'
elif nota >= 7:
    categoria = 'Bom'
elif nota >= 5:
    categoria = 'Regular'
else:
    categoria = 'Reprovado'

print('Você é um aluno', categoria)
