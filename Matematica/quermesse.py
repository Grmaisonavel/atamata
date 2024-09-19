ordem = []
ganhador = 0


quantpessoa = int(input("Insira o numero de pessoas que atenderam a festa: "))

for i in range(quantpessoa):
    numingresso = int(input("Insira o numero do ingresso em ordem de chegada: "))
    ordem.append(numingresso)

for a in range(0, len(ordem)):
    if a + 1 == ordem[a]:
        ganhador = ordem[a]
        break

print(ganhador)
