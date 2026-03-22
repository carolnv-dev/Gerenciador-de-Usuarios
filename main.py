from collections import Counter

usuarios = []
programa = 0
while programa == 0:
    comando = input('Digite ADD para adicionar um usuário e END para finalizar o programa: ').upper()

    if comando == 'ADD':
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cpf = input('CPF: ')

        if len(cpf) < 14:
            print('CPF inválido! Tente novamente.')
        else:
            usuario = {
                'nome': nome,
                'idade': idade,
                'cpf': cpf
            }
            usuarios.append(usuario)

    elif comando == 'END':

        soma_idades = 0
        usuarios_nomes = ''
        for u in usuarios:

            # soma todas as idades:
            soma_idades += u['idade']

            # concatena todos os nomes:
            usuarios_nomes += u['nome']

        # mostra a média das idades na tela
        print(f'A média das idades é: {soma_idades / len(usuarios)}')

        # mostra a incidência das 3 letras que mais aparecem na tela
        contagem_letras = Counter(usuarios_nomes.upper())
        print(f'As letras com maior incidência foram: {contagem_letras.most_common(3)}')

        # finaliza o loop
        programa = 1
    else:
        print('Comando inválido! Tente novamente.')