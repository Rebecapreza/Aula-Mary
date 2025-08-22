class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if quantidade >= 0 and quantidade <= 100:
            self.fome = max(0, self.fome - quantidade)
            print(f"{self.nome} foi alimentado! Fome agora: {self.fome}")

    def brincar(self, quantidade):
        if quantidade >= 0 and quantidade <= 100:
            self.tedio = max(0, self.tedio - quantidade)
            self.fome += 20  
            print(f"{self.nome} brincou ! Tédio agora: {self.tedio}, Fome agora: {self.fome}")

    def getHumor(self):
        return max(0, min(100, 100 - (self.fome * 0.6 + self.tedio * 0.4)))


    def vida(self):
        if self.fome > 99 or self.tedio > 99:
            self.saude = 0
            print(" Seu bichinho morreu...")
        elif self.fome > 90 or self.tedio > 90:
            print("Estou morrendo, socorro!")
            self.saude -= 20
        elif self.fome > 80 or self.tedio > 80:
            self.saude -= 10
        elif self.fome > 60 or self.tedio > 60:
            self.saude -= 5
        elif self.fome > 50 or self.tedio > 50:
            self.saude -= 2

        self.saude = max(0, self.saude)

    def causa_da_morte(self):
        if self.fome > 99:
            return "de fome"
        elif self.tedio > 99:
            return "de tédio"
        return "por estar muito fraco"


    def tempoPassado(self):
        self.vida()
        self.idade += 2
        self.tedio += 10
        self.fome += 20
        print(f" O tempo passou... Idade: {self.idade:.1f}, Fome: {self.fome}, Tédio: {self.tedio}, Saúde: {self.saude}")
