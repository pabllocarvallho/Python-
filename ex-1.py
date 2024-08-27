nota = 7
if nota >= 7:
    print ("Aprovado")
else:
    print ("Reprovado")


nota1 = 7
if nota1 == 7:
    print ("No Limite")
elif nota1 > 7:
    print ("Aprovado")
else:
    print ("Reprovado")


#aplicando operadores logicos

#and = as duas tem que ser verdadeiras
#or = uma ou outra apenas verdadeira
#not = (inversores) se ela for verdadeira se torna falsa

nota2 = float ( input ("Digite a nota = "))
if nota2 == 7:
    print ("No Limite")
elif nota2 > 7:
    print ("Aprovado")
if nota2 >= 5 and nota2 < 7:
    print ("Exame especial")
else:
    print ("Reprovado")
    
