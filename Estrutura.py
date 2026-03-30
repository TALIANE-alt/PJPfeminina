nota = 10

#condicional para avaliar notas

if nota >= 0 and nota < 3:
    categoria = 'Reprovado'

elif nota >= 3 and nota < 7:
    categoria = 'Recuperação'
 
else:
    categoria = 'Aprovado'

print('você está' , categoria)
