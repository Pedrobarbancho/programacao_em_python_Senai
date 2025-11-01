import random

print('sistema jogos: ')

opcao =input('''
escolha o jogo:
1 = advinha o numero
2 - charada
3 - pedra, papel e tesoura 🪨 🧻✂️
''')

if opcao == 1:
    print ("ADVINHA O NUMERO")
    numero = random.randrange(1,10)
    escolha1 = int(input("Escolha um numero de 1 a 10: "))

    if numero == escolha1:
        print ("vc acertou!! ")
        print (f"o numero aleatoria é {numero}")
    else:
        print("ERROU FEIO! KKKKKKKKK")
        print (f"o numero aleatoria é {numero}\n")
        print ("ez")
elif opcao == 2:
    print ("CHARADA")
    perguntas =[
    "O que é o que é? Quanto mais se tira, maior fica?",
    "Por que o livro foi ao médico?",
    "O que é o que é que tem dentes, mas não morde?",
    "Por que o computador foi preso?",
    "O que é o que é que cai em pé e corre deitado?",
    "O que é um pontinho vermelho no jardim?",
    "O que o tomate foi fazer no banco?",
    "O que é o que é que tem asa, mas não voa, e canta sem ter boca?",
    "Por que o lápis se deu mal na prova?",
    "O que é o que é que quanto mais quente fica, mais frio deixa o ambiente?",
    ]

    respostas = [
    "Um buraco",
    'Porque ele estava com muitas “histórias” pra contar',
    "O pente",
    "Porque ele executou um programa",
    "A chuva",
    "Uma formiga com batom!",
    "Tirar extrato",
    "O ventilador",
    "Porque estava sem ponta",
    "O ar-condicionado",
    ]

    aleatorio_pergunta = random.choice(perguntas)
    print (aleatorio_pergunta)

    escolha2 = int(input(f'''
    0 - {respostas[0]}
    1 - {respostas[1]}
    2 - {respostas[2]}
    3 - {respostas[3]}
    4 - {respostas[4]}
    5 - {respostas[5]}
    6 - {respostas[6]}
    7 - {respostas[7]}
    8 - {respostas[8]}
    9 - {respostas[9]}
    '''))

    indece_pergunta = perguntas.index(aleatorio_pergunta)


    if indece_pergunta == escolha2:
        print('acertou!!')
    else:
        print("ERROU FEIO! KKKKKKKKKKKKKKK")
else:
    print("PEDRO, PAPEL E TESOURA")
    ppt_maquina = ['🪨','🧻','✂️']
ppt_jogador = ['🪨','🧻','✂️']

aleatorio = random.choice(ppt_maquina)
escolha3 = int(input('''
0 -🪨
1 -🧻
2 -✂️                 
'''))

if aleatorio == ppt_jogador [escolha3]:
    print ("empate!")
    print (f"A maquina escolheu {aleatorio}")
    print (f"Vc escolheu {ppt_jogador[escolha3]}")
elif aleatorio == '🧻' and ppt_jogador[escolha3] == '🪨':
    print ("A maquina ganhou!")
    print (f"A maquina escolheu {aleatorio}")
    print (f"Vc escolheu {ppt_jogador[escolha3]}")
elif aleatorio == '🪨' and ppt_jogador[escolha3] == '✂️':
    print ("A maquina ganhou!")
    print (f"A maquina escolheu {aleatorio}")
    print (f"Vc escolheu {ppt_jogador[escolha3]}")
elif aleatorio == '✂️' and ppt_jogador[escolha3] == '🧻':
    print ("A maquina ganhou!")
    print (f"A maquina escolheu {aleatorio}")
    print (f"Vc escolheu {ppt_jogador[escolha3]}")
elif aleatorio == '✂️' and ppt_jogador[escolha3] == '🪨':
    print ("Vc ganhou!")
    print (f"A maquina escolheu {aleatorio}")
    print (f"Vc escolheu {ppt_jogador[escolha3]}")
elif aleatorio == '🪨' and ppt_jogador[escolha3] == '🧻':
    print ("Vc ganhou!")
    print (f"A maquina escolheu {aleatorio}")
    print (f"Vc escolheu {ppt_jogador[escolha3]}")
else:
    print ("Vc ganhou!")
    print (f"A maquina escolheu {aleatorio}")
    print (f"Vc escolheu {ppt_jogador[escolha3]}")