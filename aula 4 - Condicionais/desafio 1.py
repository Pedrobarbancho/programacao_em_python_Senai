quartos = ["Simples", "Duplo","Luxo"]
preco = [100.00, 150.00, 250.00]

carrinho = []
valor = 0

print ("CLIENTE 1:\n")
#cadastro
print ("Faça o cadastro para começa resevar os quartos")
cadastro_nome_1 = input("Nome: ")
cadastro_idade_1 = int(input("idade: "))

if cadastro_idade_1 >= 18:
    print (f"Cadastro feito com sucesso,{cadastro_nome_1}!\n")
    #reservar o quarto
    print ("1. Simples - R$ 100.00")
    print ("2. Duplo - R$ 150.00")
    print ("3. Luxo - R$ 250.00")
    reserva1 = int(input("Escolha o numero de qual quarto você deseja reservar: "))
    if reserva1 == 1:
        print (f"Você escolheu o {quartos[0]}.")
        dias_1 = int(input("Quantos dias você deseja ficar da sua estadia?\n"))
        carrinho.append(quartos[0])
        valor += preco[0]
        total = dias_1 * valor
        #finalizar a compra
        print ("=== CARRINHO ===\n")
        print (f"Carrinho: {carrinho}\ntotal: R${total}\n")
        finalizar_compra1 = input(f"Você quer finalizar a compra?\n")
        if finalizar_compra1 == 'sim':
            print ("1. PIX")
            print ("2. CC")
            print ("3. CD")
            forma_pagamento1 = int(input("Digita o numero de qual forma de pagamente deseja fazer: "))
            if forma_pagamento1 == 1:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_1}!")
            elif forma_pagamento1 == 2:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_1}!")
            elif forma_pagamento1 == 3:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_1}!")
            else:
                print ("ERRO: Reposta invalida.")
        elif finalizar_compra1 == 'não' or 'nao':
            print ("cancelando a compra.")
        else:
            print ("ERRO: Reposta invalida.")
    elif reserva1 == 2:
        print (f"Você escolheu o {quartos[1]}.")
        dias_1 = int(input("Quantos dias você deseja ficar da sua estadia?\n"))
        carrinho.append(quartos[1])
        valor += preco[1]
        total = dias_1 * valor
        print ("=== CARRINHO ===\n")
        print (f"Carrinho: {carrinho}\ntotal: R${total}\n")
        finalizar_compra1 = input(f"Você finalizar?\n")
        if finalizar_compra1 == 'sim':
            print ("1. PIX")
            print ("2. CC")
            print ("3. CD")
            forma_pagamento1 = int(input("Digita o numero de qual forma de pagamente deseja fazer: "))
            if forma_pagamento1 == 1:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_1}!")
            elif forma_pagamento1 == 2:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_1}!")
            elif forma_pagamento1 == 3:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_1}!")
            else:
                print ("ERRO: Reposta invalida.")
        elif finalizar_compra1 == 'não' or 'nao':
            print ("cancelando a compra.")
        else:
            print ("ERRO: Reposta invalida.")
    elif reserva1 == 3:
        print (f"Você escolheu o {quartos[2]}.")
        dias_1 = int(input("Quantos dias você deseja ficar da sua estadia?\n"))
        carrinho.append(quartos[2])
        valor += preco[2]
        total = dias_1 * valor
        print ("=== CARRINHO ===\n")
        print (f"Carrinho: {carrinho}\ntotal: R${total}\n")
        finalizar_compra1 = input(f"Você finalizar?\n")
        if finalizar_compra1 == 'sim':
            print ("1. PIX")
            print ("2. CC")
            print ("3. CD")
            forma_pagamento1 = int(input("Digita o numero de qual forma de pagamente deseja fazer: "))
            if forma_pagamento1 == 1:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_1}!")
            elif forma_pagamento1 == 2:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_1}!")
            elif forma_pagamento1 == 3:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_1}!")
            else:
                print ("ERRO: Reposta invalida.")
        elif finalizar_compra1 == 'não' or 'nao':
            print ("cancelando a compra.")
        else:
            print ("ERRO: Reposta invalida.")
    else:
        print ("ERRO: Reposta invalida.")
else:
    print ("Não aceitamos menores de idade.")

carrinho.clear()
valor = 0

print ("CLIENTE 2:\n")
#cadastro
print ("Faça o cadastro para começa resevar os quartos")
cadastro_nome_2 = input("Nome: ")
cadastro_idade_2 = int(input("idade: "))

if cadastro_idade_2 >= 18:
    print (f"Cadastro feito com sucesso,{cadastro_nome_2}!\n")
    #reservar o quarto
    print ("1. Simples - R$ 100.00")
    print ("2. Duplo - R$ 150.00")
    print ("3. Luxo - R$ 250.00")
    reserva2 = int(input("Escolha o numero de qual quarto você deseja reservar: "))
    if reserva2 == 1:
        print (f"Você escolheu o {quartos[0]}.")
        dias_2 = int(input("Quantos dias você deseja ficar da sua estadia?\n"))
        carrinho.append(quartos[0])
        valor += preco[0]
        total = dias_2 * valor
        #finalizar a compra
        print ("=== CARRINHO ===\n")
        print (f"Carrinho: {carrinho}\ntotal: R${total}\n")
        finalizar_compra2 = input(f"Você quer finalizar a compra?\n")
        if finalizar_compra2 == 'sim':
            print ("1. PIX")
            print ("2. CC")
            print ("3. CD")
            forma_pagamento2 = int(input("Digita o numero de qual forma de pagamente deseja fazer: "))
            if forma_pagamento2 == 1:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_2}!")
            elif forma_pagamento2 == 2:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_2}!")
            elif forma_pagamento2 == 3:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_2}!")
            else:
                print ("ERRO: Reposta invalida.")
        elif finalizar_compra2 == 'não' or 'nao':
            print ("cancelando a compra.")
        else:
            print ("ERRO: Reposta invalida.")
    elif reserva2 == 2:
        print (f"Você escolheu o {quartos[1]}.")
        dias_2 = int(input("Quantos dias você deseja ficar da sua estadia?\n"))
        carrinho.append(quartos[1])
        valor += preco[1]
        total = dias_2 * valor
        print ("=== CARRINHO ===\n")
        print (f"Carrinho: {carrinho}\ntotal: R${total}\n")
        finalizar_compra2 = input(f"Você finalizar?\n")
        if finalizar_compra2 == 'sim':
            print ("1. PIX")
            print ("2. CC")
            print ("3. CD")
            forma_pagamento2 = int(input("Digita o numero de qual forma de pagamente deseja fazer: "))
            if forma_pagamento2 == 1:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_2}!")
            elif forma_pagamento2 == 2:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_2}!")
            elif forma_pagamento2 == 3:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_2}!")
            else:
                print ("ERRO: Reposta invalida.")
        elif finalizar_compra2 == 'não' or 'nao':
            print ("cancelando a compra.")
        else:
            print ("ERRO: Reposta invalida.")
    elif reserva2 == 3:
        print (f"Você escolheu o {quartos[2]}.")
        dias_2 = int(input("Quantos dias você deseja ficar da sua estadia?\n"))
        carrinho.append(quartos[2])
        valor += preco[2]
        total = dias_2 * valor
        print ("=== CARRINHO ===\n")
        print (f"Carrinho: {carrinho}\ntotal: R${total}\n")
        finalizar_compra2 = input(f"Você finalizar?\n")
        if finalizar_compra2 == 'sim':
            print ("1. PIX")
            print ("2. CC")
            print ("3. CD")
            forma_pagamento2 = int(input("Digita o numero de qual forma de pagamente deseja fazer: "))
            if forma_pagamento2 == 1:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_2}!")
            elif forma_pagamento2 == 2:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_2}!")
            elif forma_pagamento2 == 3:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_2}!")
            else:
                print ("ERRO: Reposta invalida.")
        elif finalizar_compra2 == 'não' or 'nao':
            print ("cancelando a compra.")
        else:
            print ("ERRO: Reposta invalida.")
    else:
        print ("ERRO: Reposta invalida.")
else:
    print ("Não aceitamos menores de idade.")
    
carrinho.clear()
valor = 0

print ("CLIENTE 1:\n")
#cadastro
print ("Faça o cadastro para começa resevar os quartos")
cadastro_nome_3 = input("Nome: ")
cadastro_idade_3 = int(input("idade: "))

if cadastro_idade_3 >= 18:
    print (f"Cadastro feito com sucesso,{cadastro_nome_1}!\n")
    #reservar o quarto
    print ("1. Simples - R$ 100.00")
    print ("2. Duplo - R$ 150.00")
    print ("3. Luxo - R$ 250.00")
    reserva3 = int(input("Escolha o numero de qual quarto você deseja reservar: "))
    if reserva3 == 1:
        print (f"Você escolheu o {quartos[0]}.")
        dias_3 = int(input("Quantos dias você deseja ficar da sua estadia?\n"))
        carrinho.append(quartos[0])
        valor += preco[0]
        total = dias_3 * valor
        #finalizar a compra
        print ("=== CARRINHO ===\n")
        print (f"Carrinho: {carrinho}\ntotal: R${total}\n")
        finalizar_compra3 = input(f"Você quer finalizar a compra?\n")
        if finalizar_compra3 == 'sim':
            print ("1. PIX")
            print ("2. CC")
            print ("3. CD")
            forma_pagamento3 = int(input("Digita o numero de qual forma de pagamente deseja fazer: "))
            if forma_pagamento3 == 1:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_3}!")
            elif forma_pagamento3 == 2:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_3}!")
            elif forma_pagamento3 == 3:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_3}!")
            else:
                print ("ERRO: Reposta invalida.")
        elif finalizar_compra3 == 'não' or 'nao':
            print ("cancelando a compra.")
        else:
            print ("ERRO: Reposta invalida.")
    elif reserva3 == 2:
        print (f"Você escolheu o {quartos[1]}.")
        dias_3 = int(input("Quantos dias você deseja ficar da sua estadia?\n"))
        carrinho.append(quartos[1])
        valor += preco[1]
        total = dias_3 * valor
        print ("=== CARRINHO ===\n")
        print (f"Carrinho: {carrinho}\ntotal: R${total}\n")
        finalizar_compra3 = input(f"Você finalizar?\n")
        if finalizar_compra3 == 'sim':
            print ("1. PIX")
            print ("2. CC")
            print ("3. CD")
            forma_pagamento3 = int(input("Digita o numero de qual forma de pagamente deseja fazer: "))
            if forma_pagamento3 == 1:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_3}!")
            elif forma_pagamento3 == 2:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_3}!")
            elif forma_pagamento3 == 3:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_3}!")
            else:
                print ("ERRO: Reposta invalida.")
        elif finalizar_compra3 == 'não' or 'nao':
            print ("cancelando a compra.")
        else:
            print ("ERRO: Reposta invalida.")
    elif reserva3 == 3:
        print (f"Você escolheu o {quartos[2]}.")
        dias_3 = int(input("Quantos dias você deseja ficar da sua estadia?\n"))
        carrinho.append(quartos[2])
        valor += preco[2]
        total = dias_3 * valor
        print ("=== CARRINHO ===\n")
        print (f"Carrinho: {carrinho}\ntotal: R${total}\n")
        finalizar_compra3 = input(f"Você finalizar?\n")
        if finalizar_compra3 == 'sim':
            print ("1. PIX")
            print ("2. CC")
            print ("3. CD")
            forma_pagamento3 = int(input("Digita o numero de qual forma de pagamente deseja fazer: "))
            if forma_pagamento3 == 1:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_3}!")
            elif forma_pagamento3 == 2:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_3}!")
            elif forma_pagamento3 == 3:
                print ("Compra finalizada!")
                print (f"Obrigado pela compra, {cadastro_nome_3}!")
            else:
                print ("ERRO: Reposta invalida.")
        elif finalizar_compra1 == 'não' or 'nao':
            print ("cancelando a compra.")
        else:
            print ("ERRO: Reposta invalida.")
    else:
        print ("ERRO: Reposta invalida.")
else:
    print ("Não aceitamos menores de idade.")
    
carrinho.clear()
valor = 0