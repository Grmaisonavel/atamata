ordem = []
ganhador = 0

#Recebe o numero de pessoas que perticiparam da festa
quantpessoa = int(input("Insira o numero de pessoas que atenderam a festa: "))

#Recebe o numero dos ingressos dos participantes em ordem de chegada
for i in range(quantpessoa):
    numingresso = int(input("Insira o numero do ingresso em ordem de chegada: "))
    ordem.append(numingresso)

#Compara o numero do ingresso com a ordem de chegada
for a in range(0, len(ordem)):
    if a + 1 == ordem[a]:
        ganhador = ordem[a]
        break

#Mostra o numero do ingresso do ganhador 
print(ganhador)
