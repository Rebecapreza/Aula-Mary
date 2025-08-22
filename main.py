from Tamagoshifilho import TamagoshiAmoroso, TamagoshiHobbies, TamagoshiSkin


def criar_bicho():
    print("Criando novo bichinho!")
    nome = input("Digite o nome do bichinho: ")
    print("Escolha o tipo do bichinho:")
    print("1 - Skinzudo 🛍️")
    print("2 - Talentudo 💋")
    print("3 - Amorosudo 💌")
    tipo = input("Digite o número do tipo: ")

    if tipo == "1":
        cor_asa = input("Cor das asas: ")
        poder = input("Poder: ")
        cor_corpo = input("Cor do corpo: ")
        cor_cabelo = input("Cor do cabelo: ")
        return TamagoshiSkin(nome, cor_asa, poder, cor_corpo, cor_cabelo)
    elif tipo == "2":
        musica = input("Música favorita: ")
        dancar = input("Dança favorita: ")
        andando_skate = input("Andar de skate (sim/não): ")
        show = input("Participa de show (sim/não): ")
        return TamagoshiHobbies(nome, musica, dancar, andando_skate, show)
    elif tipo == "3":
        declaracao = input("Declaração de amor: ")
        cantor = input("Cantor favorito: ")
        elogio = input("Elogio: ")
        return TamagoshiAmoroso(nome, declaracao, cantor, elogio)
    else:
        print("Tipo inválido, criando TamagoshiSkin padrão")
        return TamagoshiSkin(nome, "branco", "voar", "cinza", "preto")

def salvar_bicho(bicho):
    import pickle
    with open("bicho_salvo.pkl", "wb") as f:
        pickle.dump(bicho, f)

def carregar_bicho():
    import os
    import pickle
    if os.path.exists("bicho_salvo.pkl"):
        with open("bicho_salvo.pkl", "rb") as f:
            return pickle.load(f)
    return None


def main():
    print("🎉🎉🎉🎉 Bem-vindo ao Tamagoshi! 🎉🎉🎉🎉")

    bicho = carregar_bicho()

    if bicho:
        print(f"Seu bichinho {bicho.nome} acordou!")
    else:
        bicho = criar_bicho()
        print(f"Você criou um novo bichinho chamado {bicho.nome}!✨")

    while True:
        print("\nO que deseja fazer?")
        print("1 - Alimentar 🍽️")
        print("2 - Brincar ⛳")
        print("3 - Ver humor 😜😣🙂🤕")
        print("4 - Ver status 🚦")
        print("8 - Mudar skin (apenas Skinzudo) 🛍️💸")
        print("9 - Criar novo bichinho 🐢🐕")

        if isinstance(bicho, TamagoshiSkin):
            print("5 - Alterar aparência (asas, corpo, cabelo)")
            print("6 - Alterar poder")
            print("7 - Sair (salvar bichinho)")
        elif isinstance(bicho, TamagoshiHobbies):
            print("5 - Ouvir música 🎵")
            print("6 - Dançar 💃🕺")
            print("7 - Andar skate 🛹")
            print("8 - Show 🎤🎙️")
            print("10 - Sair (salvar bichinho)")
        elif isinstance(bicho, TamagoshiAmoroso):
            print("5 - Fazer declaração de amor 💞💞💞")
            print("6 - Cantar moda de viola 🎻🎻")
            print("7 - Receber elogio 💆💆‍♀️💆‍♂️")
            print("8 - Sair (salvar bichinho)")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            quant = int(input("Quanto deseja alimentar (0-100)? "))
            bicho.alimentar(quant)
        elif opcao == "2":
            quant = int(input("Quanto deseja brincar (0-100)? "))
            bicho.brincar(quant)
        elif opcao == "3":
            humor = bicho.getHumor()
            print(f"Humor do {bicho.nome}: {humor:.2f}")
        elif opcao == "4":
            print(f"Nome: {bicho.nome}")
            print(f"Fome: {bicho.fome}")
            print(f"Tédio: {bicho.tedio}")
            print(f"Saúde: {bicho.saude}")
            print(f"Idade: {bicho.idade}")

            if isinstance(bicho, TamagoshiSkin):
                print(f"Asas: {bicho.cor_asa}")
                print(f"Corpo: {bicho.cor_corpo}")
                print(f"Cabelo: {bicho.cor_cabelo}")
                print(f"Poder: {bicho.poder}")
            elif isinstance(bicho, TamagoshiHobbies):
                print(f"Música: {bicho.musica}")
                print(f"Dança: {bicho.dancar}")
                print(f"Andando skate: {bicho.andando_skate}")
                print(f"Show: {bicho.show}")
            elif isinstance(bicho, TamagoshiAmoroso):
                print(f"Declaração: {bicho.declaracao}")
                print(f"Cantor: {bicho.cantor}")
                print(f"Elogio: {bicho.elogio}")

        elif opcao == "8" and isinstance(bicho, TamagoshiSkin):
            print("Criando uma nova skin para seu bichinho...")
            nome = bicho.nome  
            cor_asa = input("Nova cor das asas: ")
            poder = input("Novo poder: ")
            cor_corpo = input("Nova cor do corpo: ")
            cor_cabelo = input("Nova cor do cabelo: ")
            bicho = TamagoshiSkin(nome, cor_asa, poder, cor_corpo, cor_cabelo)
            print("Skin alterada com sucesso!")

        elif opcao == "9":
            print("Criando um novo bichinho...")
            bicho = criar_bicho()
            print(f"Você criou um novo bichinho chamado {bicho.nome}!")

        elif opcao == "7" and isinstance(bicho, TamagoshiSkin):
            print(f"Salvando {bicho.nome} e encerrando o jogo...")
            salvar_bicho(bicho)
            break

        elif isinstance(bicho, TamagoshiHobbies):
            if opcao == "5":
                musica = input("Digite a música para o bichinho ouvir: ")
                bicho.ouvir_musica(musica)
            elif opcao == "6":
                dancar = input("Digite o movimento de dança: ")
                bicho.dancando(dancar)
            elif opcao == "7":
                skate = input("Seu bichinho está andando skate? (sim/não): ")
                if skate.lower() == "sim":
                    bicho.andar_skate(skate)
                else:
                    print("Seu bichinho ainda não está andando skate...")
            elif opcao == "8":
                show = input("Seu bichinho está no show? (sim/não): ")
                if show.lower() == "sim":
                    bicho.show_de_bola(show)
                else:
                    print("Seu bichinho não está no show.")
            elif opcao == "10":
                print(f"Salvando {bicho.nome} e encerrando o jogo...")
                salvar_bicho(bicho)
                break
            else:
                print("Opção inválida.")

        elif isinstance(bicho, TamagoshiAmoroso):
            if opcao == "5":
                bicho.amor()
            elif opcao == "6":
                bicho.modadeviola()
            elif opcao == "7":
                bicho.love()
            elif opcao == "8":
                print(f"Salvando {bicho.nome} e encerrando o jogo...")
                salvar_bicho(bicho)
                break
            else:
                print("Opção inválida.")
        else:
            print("Opção inválida.")

        bicho.tempoPassado()

        if bicho.saude <= 0:
            print(f"Infelizmente, seu bichinho {bicho.nome} morreu {bicho.causa_da_morte()}.")
            print("O jogo será reiniciado...")
            import os
            if os.path.exists("bicho_salvo.pkl"):
                os.remove("bicho_salvo.pkl")
            bicho = criar_bicho()

if __name__ == "__main__":
    main()