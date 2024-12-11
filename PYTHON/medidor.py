import random

#resposta do bot treinado vai entrar mais tarde
#dificulty=["facil" , "intermediario", "medio","dificil", "impossivel", "Boa sorte"]







#10% de chance de falha 
def easy(numeroMedir):
    if numeroMedir <= 10:
        resultado = 0 # 0 significa falha 
    else:
        resultado=1 #significa sucesso

    print=resultado

#20% de chance de falha 
def intermediary(numeroMedir):
    if numeroMedir <= 20:
        resultado = 0 # 0 significa falha 
    else:
        resultado=1 #significa sucesso

    print=resultado

#30% de chance de falha 
def medium(numeroMedir):
    if numeroMedir <=30:
        resultado = 0 # 0 significa falha 
    else:
        resultado=1 #significa sucesso

    print=resultado

#40% de chance de falha 
def hard(numeroMedir):
    if numeroMedir <=40:
        resultado = 0 # 0 significa falha 
    else:
        resultado=1 #significa sucesso

    print=resultado
#60% de chance de falha 
def impossible(numeroMedir):
    if numeroMedir <=60:
        resultado = 0 # 0 significa falha 
    else:
        resultado=1 #significa sucesso

    print=resultado

#80% de chance de falha 
def goodLuck(numeroMedir):
    if numeroMedir <=80:
        resultado = 0 # 0 significa falha 
    else:
        resultado=1 #significa sucesso

    print=resultado




def medidor(userChoice):
    if userChoice == 1:
        easy(numeroMedir)
    elif userChoice == 2:
        intermediary(numeroMedir)
    elif userChoice == 3:
        medium(numeroMedir)
    elif userChoice == 4:
        hard(numeroMedir)
    elif userChoice == 5:
        impossible(numeroMedir)
    elif userChoice == 6:
        goodLuck(numeroMedir)


UserChoice=int(input('''
        Escolha  a dificuldade da missão:
          
        1.facil
        2.intermediario
        3.medio
        4.dificil
        5.impossivel
        6.boa sorte
        :D
        RESPOSTA:'''))



numeroMedir= random.randint(1,100)
print(f'O numero é: {numeroMedir}')


medidor(UserChoice)


