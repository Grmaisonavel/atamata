i = 0
j = 0
k = 0
l = 0
valor = [i,j,k,l]

v = int(input("Insira o valor que deseja retirar: "))

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

print(i,j,k,l)