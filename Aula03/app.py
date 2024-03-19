# Criação das variaveis
num1 = 5
num2 = 3.5
#--------------------

#Identificar qual o tipo de variavel que estamos utilizando (Utilizar o "type" para chamar a variavel)
print(type(num1))
print(type(num2))

#Convertendo uma variavel para outra classe
a= float(num1)
print(a)
print(type(a))

b = int(num2)
print(b)
print(type(b))
#----------------------------

#Criação das variaveis
c = "8"
d = "4.5"
#--------------------

#Imprimindo o tipo de variavel
print(type(c))
print(type(d))

#Convertendo uma variavel para outra classe
c= float(c)
d= int(float(d))

# Não e possivel converter um valor string quebrado, de uma vez! Deve primeiro converter pra float e depois para inteiro
print(type(c))
print(type(d))
print(d)
print (c)