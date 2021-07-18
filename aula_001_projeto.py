# Jogo de busca binaria
import math

inicio = int(input('Primeiro número: '))
fim = int(input('Ultimo número: '))
if fim > inicio:
    input('Opa, Tenho um desafio pra você: pense em um numero entre %d e %d' % (inicio, fim))
    qtd_num = (fim - inicio) + 1
    max_tentativas = math.ceil(math.log(qtd_num, 2))
    input('Vou o numero secreto em até %d tentativas' % max_tentativas)
    tentativas = 0
    acabou = False
    while not acabou:
        meio = (inicio + fim) // 2
        tentativas += 1
        opcao = input(' %d tentativa: o numero secreto é maior (>) ou igual (=) a %d?' % (tentativas, meio))
        if opcao == '>':
            inicio = meio + 1
        elif opcao == '<':
            fim = meio - 1
        else:
            acabou = True
    print('Eu sabia! o numero secreto é %d! E adivinhei após %d tentativas' % (meio, tentativas))
