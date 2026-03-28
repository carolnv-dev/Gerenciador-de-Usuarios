from collections import Counter

usuarios = []
programa = 0
while programa == 0:
    comando = input('Digite ADD para adicionar um usuário e END para finalizar o programa: ').upper()

    if comando == 'ADD':
        nome = input('Nome: ')
        try:
            idade = int(input('Idade: '))
        except ValueError:
            print('Digite uma idade válida')
            continue
        cpf = input('CPF: ')

        if len(cpf) != 14:
            print('Número de caracteres do CPF inválido! Tente novamente.')
        else:

            usuario = {
                'nome': nome,
                'idade': idade,
                'cpf': cpf
            }
            usuarios.append(usuario)

    elif comando == 'END':
        if len(usuarios) == 0:
            print('Você não registrou nenhum usuário!')
            break

        usuarios_nomes = ''
        lista_idades = []
        for u in usuarios:
            usuarios_nomes += u['nome']
            lista_idades.append(u['idade'])

        media_idades = sum(lista_idades) / len(usuarios)
        print(f'A média das idades é {media_idades:.2f}')

        cont_letras = Counter(usuarios_nomes.upper().replace(' ', ''))
        print(f'As letras com maior incidência foram: {cont_letras.most_common(3)}')

        indice_maior_idade = lista_idades.index(max(lista_idades))
        indice_menor_idade = lista_idades.index(min(lista_idades))

        print(f'O usuário mais velho é {usuarios[indice_maior_idade]['nome']} '
              f'com {usuarios[indice_maior_idade]['idade']} anos de idade '
              f'e CPF {usuarios[indice_maior_idade]['cpf']}')

        print(f'O usuário mais novo é {usuarios[indice_menor_idade]['nome']} '
              f'com {usuarios[indice_menor_idade]['idade']} anos de idade '
              f'e CPF {usuarios[indice_menor_idade]['cpf']}')
        programa = 1

    else:
        print('Comando inválido! Tente novamente.')