import random

# Funções para determinar o resultado com base na dificuldade
def easy(numeroMedir):
    if numeroMedir <= 10:
        return 0  # 0 significa falha
    else:
        return 1  # 1 significa sucesso

def intermediary(numeroMedir):
    if numeroMedir <= 20:
        return 0  # 0 significa falha
    else:
        return 1  # 1 significa sucesso

def medium(numeroMedir):
    if numeroMedir <= 30:
        return 0  # 0 significa falha
    else:
        return 1  # 1 significa sucesso

def hard(numeroMedir):
    if numeroMedir <= 40:
        return 0  # 0 significa falha
    else:
        return 1  # 1 significa sucesso

def impossible(numeroMedir):
    if numeroMedir <= 60:
        return 0  # 0 significa falha
    else:
        return 1  # 1 significa sucesso

def goodLuck(numeroMedir):
    if numeroMedir <= 80:
        return 0  # 0 significa falha
    else:
        return 1  # 1 significa sucesso


def medidor(userChoice, numeroMedir):
    if userChoice == 1:
        return easy(numeroMedir)
    elif userChoice == 2:
        return intermediary(numeroMedir)
    elif userChoice == 3:
        return medium(numeroMedir)
    elif userChoice == 4:
        return hard(numeroMedir)
    elif userChoice == 5:
        return impossible(numeroMedir)
    elif userChoice == 6:
        return goodLuck(numeroMedir)
    else:
        print("Escolha inválida.")
        return None


UserChoice = int(input('''
        Escolha a dificuldade da missão:
          
        1. facil
        2. intermediario
        3. medio
        4. dificil
        5. impossivel
        6. boa sorte
        :D
        RESPOSTA: '''))


numeroMedir = random.randint(1, 100)
print(f'O número gerado é: {numeroMedir}')


resultado = medidor(UserChoice, numeroMedir)


if resultado == 0:
    print("Resultado: Falha!")
elif resultado == 1:
    print("Resultado: Sucesso!")
