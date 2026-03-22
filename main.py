from collections import Counter

nomes = []
idades = []
cpfs = []

programa = 0
while programa == 0:
    comando = input('Digite ADD para adicionar um usuário ou END para finalizar: ').upper()

    if comando == 'ADD':
        nomes.append(input(f'Digite o nome: '))
        idades.append(int(input(f'Digite a idade: ')))
        cpf = input('Digite o CPF:')

        if len(cpf) < 14:
            print('CPF inválido! Tente novamente.')
            del nomes[-1]
            del idades[-1]
        else:
            cpfs.append(cpf)

    elif comando == 'END':
        print(f'A média das idades é {sum(idades) / len(idades)}')
        contagem = Counter(''.join(nomes).upper())
        print(f'As letras que mais apareceram foram: {contagem.most_common(3)}')
        programa = 1
    else:
        print('Você digitou um comando inválido! Tente novamente.')
