#1
'''
numero = int(input("Digita um numero (negativo ou postivo): "))

if numero >= 1:
    print ("O numero é positivo!")
elif numero == 0:
    print ("O numero pe zero!")
else:
    print ("O numero é negativo!")
#2
idade = int(input("Digita a sua idade: "))

if idade >= 16:
    print ("Vc ja pode votar!")
else:
    print ("Vc não pode votar por enquanto.")
#3
numero2 = int(input("Digita um numero: "))

if numero2 % 2==0:
    print ("é par!")
else:
    print ("é impar!")
#4
n1 = int(input("Digita primeiro numero para criar um triângulo: "))
n2 = int(input("Digita segundo numero: "))
n3 = int(input("Digita terceiro numero: "))

if n2 == n1 and n3 == n2:
    print ("Seu triângulo é equilátero")
elif n3 == n2:
    print ("Seu triângulo é isósceles")
else:
    print ("Seu triângulo é escaleno")
#5
nuemro3 = int(input("Digita um numero: "))

if nuemro3 == 35:
    print ("Seu numero é múltiplo de 5 e 7!")
else:
    print ("Seu numero não é múltiplo de 5 e 7.")
#6
numero4 = int(input("Digita um numero: "))

if numero4 > 10:
    print ("Seu numero é positivo e é maior de 10!")
elif numero4 > 0 and numero4 < 10:
    print ("Seu numero é positivo mas não é maior de 10.")
else:
    print ("Seu numero nem é positivo e nem maior de 10.")
'''    
#7
numero5 = int(input("Digita um numero: "))

if numero5 % 3 == 0 or numero5 % 5 == 0:
    print ("Seu numero é divisível!")
else:
    print ("Seu numero não é numero divisível.")