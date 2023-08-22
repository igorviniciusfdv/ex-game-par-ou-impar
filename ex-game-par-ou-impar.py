from random import randint
print('~' * 30)
print('JOGO DO PÁR OU ÍMPAR')
print('~' * 30)
c = 0
while True:
    print('--' * 30)
    jog = int(input('Jogue um número: '))
    poi = str(input('PÁR OU ÍMPAR? [P/I]: ')).strip().upper()[0]
    comp = randint(0, 10)
    res = jog + comp
    if poi in 'Pp' and res % 2 == 0:
        print(f'O computador jogou {comp}!')
        print(f'O jogador jogou {jog}, o resultado é PÁR')
        print('VOCÊ VENCEU!')
        c += 1
    if poi in 'Pp' and res % 2 != 0:
        print(f'O computador jogou {comp}!')
        print(f'O jogador jogou {jog}, e o resultado é ÍMPAR')
        break
    if poi in 'Ii' and res % 2 != 0:
        print(f'O computador jogou {comp}!')
        print(f'O jogador jogou {jog}, o resultado é ÍMPAR')
        print('VOCÊ VENCEU!')
        c += 1
    if poi in 'Ii' and res % 2 == 0:
        print(f'O computador jogou {comp}!')
        print(f'O jogador jogou {jog}, e o resultado é PÁR')
        break
    if poi not in 'PpIi':
        print('Opção inválida, tente novamente!')

print('--' * 30)
print(f'Você PERDEU. Suas vitórias consecutivas foram {c}')
print('--' * 30)