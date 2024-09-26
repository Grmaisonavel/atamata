i = 0
j = 0
k = 0
l = 0
valor = [i,j,k,l]

#Recebe o valor a ser retirado
v = int(input("Insira o valor que deseja retirar: "))

#Vê quantas notas de cada tipos são necessárias para atingir o valor
if v >= 50:
    i = v//50
    v = v-i*50

if v >= 10:
    j = v//10
    v = v-j*10

if v >= 5:
    k = v//5
    v = v-k*5

if v >= 1:
    l = v//1
    v = v-l*1

#Mostra a quantidade de notas necessárias de cada valor
print(i,j,k,l)
