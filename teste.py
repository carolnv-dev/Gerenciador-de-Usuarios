cpf = '140.825.089-61'


cpf = cpf.replace('.', '').replace('-', '')

# verifica se a qtd de caracteres é 11 e se todos os caracteres não são iguais (ex.: 111.111.111-11)
if len(cpf) != 11 or cpf == cpf[0] * 11:
    print('CPF Inválido!')

# -------- Validação dos digitos verificadores --------

# dv1 = cpf[0] * 10 + cpf[1] * 9 + cpf[2] * 8



valores_dv1 = []
dv1 = 0
for i in range(9):
    valores_dv1.append(cpf[i] * (10 - i))
    soma_1 = sum(valores_dv1)
    dv1 = 11 - (int(soma_1) % 11)
    if dv1 >= 10:
        dv1 = 0

dv2 = 0
valores_dv2 = []
for i in range(10):
    valores_dv2.append(cpf[i] * (11 - i))
    soma_2 = sum(valores_dv2)
    dv2 = 11 - (int(soma_2) % 11)
    if dv2 >= 10:
        dv2 = 0

if dv1 != cpf[10] or dv2 != cpf[11]:
    print('CPF Inválido!')
else:
    print('ok')



