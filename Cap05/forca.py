print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')

palavra_secreta = 'banana'
letras_acertada = ['_', '_', '_', '_', '_', '_']

acertou = False
enforcou = False

while(not acertou and not enforcou):
    chute = input('Qual a letra?')

    posicao = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertada[posicao] = letra
        posicao = posicao + 1

        print(letras_acertada)

print('Fim do jogo')