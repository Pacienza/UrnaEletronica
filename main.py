candidatoVivi = {
    'nome': 'Carlota Joaquina',
    'numero': 66,
    'vice': 'Bluezão'
}

candidatoDavi = {
    'nome': 'Paulo Kogos',
    'numero': 71,
    'vice': 'Monark'
}

candidatoAmauri = {
    'nome': 'Patati',
    'numero': 24,
    'vice': 'Ben 10'
}

candidatoLucas = {
    'nome': 'Sieghart',
    'numero': 33,
    'vice': 'Neosoro'
}

candidatoLuan = {
    'nome': 'Agostinho Carrara',
    'numero': 17,
    'vice': 'Tuco'
}

candidatos = [candidatoVivi, candidatoLucas, candidatoDavi, candidatoAmauri, candidatoLuan]

votos = {candidato['numero']: 0 for candidato in candidatos}


def listar_candidatos():
    for candidato in candidatos:

        print('Presidente: ', candidato['nome'], '[', candidato['numero'], ']')
        print('Vice: ', candidato['vice'])
        print('='*36)


def votar(numero):
    if numero not in votos:
        print('Candidato inexistente!')
        return

    while True:
        confirmacao = input(f"Você votou em {candidatos[numero]}. Confirmar voto? (S/N) ").strip().upper()
        if confirmacao == 'S':
            votos[numero] += 1
            print("Voto confirmado!")
            break
        elif confirmacao == 'N':
            print("Voto anulado. Tente novamente.")
            break
        else:
            print("Opção inválida. Por favor, responda com 'S' para sim ou 'N' para não.")


print('#' * 36)
print('*' * 36)
print('***  Urna Eletronica em Python   ***')
print('*' * 9, 'Made by Pacienza', '*' * 9)
print('#' * 36)
print('###  ', '01 - Listar Candidatos', '    ###')
print('_' * 36)
print('###  ', '02 - Votar', ' ' * 15, '###')
print('_' * 36)
print('###  ', '03 - Resultado', ' ' * 11, '###')
print('_' * 36)

opcao = int(input('--- Opção desejada:  '))
print('-' * 36)

if opcao == 1 or 0o1:
    listar_candidatos()
