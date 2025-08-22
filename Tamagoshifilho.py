from Tamagoshi import Tamagoshi

class TamagoshiSkin(Tamagoshi):
    def __init__(self, nome, cor_asa, poder, cor_corpo, cor_cabelo):
        super().__init__(nome)
        self.cor_asa = cor_asa
        self.cor_corpo = cor_corpo
        self.cor_cabelo = cor_cabelo
        self.poder = poder

    def cor_asa_escolhida(self, escolher):
        if escolher == self.cor_asa:
            print(f"A cor das asas do seu bichinho é: {self.cor_asa}")
        else:
            self.cor_asa = escolher
            print(f"A cor das asas mudou para: {self.cor_asa}")
            
    def cor_corpo_escolhido(self, escolher):
        if escolher == self.cor_corpo:
            print(f"A cor do corpo é {self.cor_corpo}")
        else:
            self.cor_corpo = escolher
            print(f"A cor do corpo mudou para: {self.cor_corpo}")

    def cor_cabelo_escolhido(self, escolher):
        if escolher == self.cor_cabelo:
            print(f"A cor do cabelo é: {self.cor_cabelo}")
        else:
            self.cor_cabelo = escolher
            print(f"A cor do cabelo mudou para: {self.cor_cabelo}")
            
    def poder_escolhido(self, escolher):
        if escolher == self.poder:
            print(f"O poder atual é: {self.poder}")
        else:
            self.poder = escolher
            print(f"O poder mudou para: {self.poder}")


class TamagoshiHobbies(Tamagoshi):
    def __init__(self, nome, musica, dancar, andando_skate, show):
        super().__init__(nome)
        self.musica = musica
        self.dancar = dancar
        self.andando_skate = andando_skate
        self.show = show

    def dancando(self, movimento):
        if movimento == self.dancar:
            print("Seu bichinho já sabe essa dança!")
        else:
            self.dancar = movimento
            print(f"Seu bichinho está dançando {self.dancar} ao som de {self.musica} 🎶")
            
    def andar_skate(self, skatista):
        if skatista == self.andando_skate:
            print("Seu bichinho está arrasando no skate 🛹")
        else:
            print("Seu bichinho ainda precisa treinar no skate...")

    def ouvir_musica(self, musica):
        self.musica = musica
        print(f"Seu bichinho está curtindo a música {self.musica} 🎧")

    def show_de_bola(self, talentoso):
        if talentoso == self.show:
            print("Seu bichinho está apresentando no show do Faustão 🎉")
        else:
            print("Seu bichinho ainda não conseguiu participar do show 😢")


class TamagoshiAmoroso(Tamagoshi):
    def __init__(self, nome, declaracao, cantor, elogio):
        super().__init__(nome)
        self.declaracao = declaracao
        self.cantor = cantor
        self.elogio = elogio
        
    def amor(self):
        print(f"Seu bichinho declara: te amo {self.declaracao} ❤️")
            
    def modadeviola(self):
        print(f"""🎵 E nessa loucura de dizer que não te quero
                Vou negando as aparências
                Disfarçando as evidências
                Mas pra que viver fingindo
                Se eu não posso enganar meu coração?
                Eu sei que te amo! {self.cantor} 🎤""")

    def love(self):
        print(f"Seu bichinho te elogia: você é sensacional{self.elogio} 💕")
