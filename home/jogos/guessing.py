print('************')
print('* Jogo da Adivinhação *')
print('************')

secretnumber = 42
level1 = 20
level2 = 10
level3 = 5

points = 1000

level = int(input('Escolha um nível: (1) Fácil  (2) Médio  (3) Difícil ' ))

if level == 1:
    attemps = level1
    print(f'No nível fácil você terá: {level1} tentativas.')
elif level == 2:
    attemps = level2
    print(f'No nível médio você terá: {level2} tentativas.')
elif level == 3:
    attemps = level3
    print(f'No nível difícil você terá: {level3} tentativas.')
else:
    print('Nível inválido. Digite 1, 2 ou 3.')
    exit()

    
for rounds in range (1, attemps+1):
    guess = int(input(f'{rounds}ª tentativa. Digite um número: '))


    if guess == secretnumber:
        print('Você acertou!')
        break
    else:
        lose = abs(guess - secretnumber)
        points -= lose
    
    if guess > secretnumber:
        print('Você errou! O seu chute foi maior que o número secreto.')
    else:
        print('Você errou! O seu chute foi menor que o número secreto.')

    print(f'Você perdeu {lose} pontos.')
    print(f'Sua pontuação atual é: {points}')

else:
    print('Você perdeu.')
    

print(f'Pontuação: {points}')
print('Fim de jogo.')

    