print('************')
print('* Jogo da Adivinhação *')
print('************')

secretnumber = 42
attemps = 3
rounds = 1

while rounds <= attemps:
    print(f'{rounds}º tentativa de {attemps}.')
    guessing = int(input('Digite um número: '))
    print(f'Você digitou: {guessing}')

    correct = guessing == secretnumber
    maior = guessing > secretnumber
    menor = guessing < secretnumber

    if correct:
        print('Você acertou!')
    elif maior:
        print('Você errou! O seu chute foi maior que o número secreto.')
    elif menor:
        print('Você errou! O seu chute foi menor que o número secreto.')

    rounds = rounds + 1

print('Fim de jogo.')