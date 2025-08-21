class Lucky:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if 0 <= quantidade <= 100:
            self.fome -= self.fome * (quantidade / 100)

    def brincar(self, quantidade):
        if 0 <= quantidade <= 100:
            self.tedio -= self.tedio * (quantidade / 100)

    def getHumor(self):
        return max(0, 100 - ((self.fome * self.tedio) / 2))        

    def vida(self):
        if (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("Seu bichinho morreu")
        elif (self.fome > 90) or (self.tedio > 90):
            print("Estou morrendo SOS")
        elif (60 < self.fome <= 80) or (60 < self.tedio <= 80):
            self.saude = max(0, self.saude - 30)
        elif (80 < self.fome <= 90) or (80 < self.tedio <= 90):
            self.saude = max(0, self.saude - 50)
        elif (50 < self.fome <= 60) or (50 < self.tedio <= 60):
            self.saude = max(0, self.saude - 10)

    def passagemTempo(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5

    def status(self):
        print(f"\n--- STATUS do {self.nome} ---")
        print(f"Idade: {self.idade:.1f}")
        print(f"Saúde: {self.saude}")
        print(f"Fome: {self.fome}")
        print(f"Tédio: {self.tedio}")
        print(f"Humor: {self.getHumor()}")

    def dormir(self):
        print(f"{self.nome} está dormindo... ")

    def acordar(self):
        print(f"{self.nome} acordou animado! ")

class LuckySkin(Lucky):
    def __init__(self, nome, cor_asa, poder, cor_corpo, cor_cabelo):
        super().__init__(nome)
        self.cor_asa = cor_asa
        self.cor_corpo = cor_corpo
        self.cor_cabelo = cor_cabelo
        self.poder = poder

    def mudar_skin(self):
        nova_cor = input("Nova cor das asas: ")
        self.cor_asa = nova_cor
        print(f"As asas agora são {self.cor_asa}")

    def mostrar_skin(self):
        print(f"Asa: {self.cor_asa}, Corpo: {self.cor_corpo}, "
              f"Cabelo: {self.cor_cabelo}, Poder: {self.poder}")

    def trocar_poder(self):
        novo_poder = input("Digite o novo poder: ")
        self.poder = novo_poder
        print(f"O poder agora é {self.poder}")


class LuckyHobbies(Lucky):
    def __init__(self, nome, musica, dancar, pular, andando_skate):
        super().__init__(nome)
        self.musica = musica
        self.dancar = dancar
        self.pular = pular
        self.andando_skate = andando_skate

    def dancar_musica(self):
        print(f"{self.nome} está dançando {self.dancar} ao som de {self.musica} 🎶")

    def pularzinho(self):
        print(f"{self.nome} está pulando assim: {self.pular}")

    def andar_de_skate(self):
        print(f"{self.nome} está andando de skate no estilo {self.andando_skate} 🛹")


class LuckyDorminhoco(Lucky):
    def __init__(self, nome, dormir, roncando, cansado):
        super().__init__(nome)
        self.dormir_tipo = dormir
        self.ronco = roncando
        self.cansaco = cansado
        
    def dormirzinho(self):
        print(f"{self.nome} está dormindo {self.dormir_tipo} 💤")

    def fazer_ronco(self):
        print(f"{self.nome} está roncando assim: {self.ronco}")

    def mostrar_cansaco(self):
        print(f"Nível de cansaço: {self.cansaco}")

def main():
    nome_bichinho = None
    historico = []

    while True:
        print("\n Bem-vindo ao jogo do Lucky ")

        if nome_bichinho is None:  
            nome_bichinho = input("Digite o nome do seu bichinho: ")
            print(f"Nome escolhido: {nome_bichinho}")
        else:
            print(f"Seu bichinho continua se chamando: {nome_bichinho}")
            print(f"{nome_bichinho} acordou! ")

        print(f"\nEscolha o tipo do seu {nome_bichinho}:")
        print("1 - Lucky Básico")
        print("2 - Lucky com Skin")
        print("3 - Lucky com Hobbies")
        print("4 - Lucky Dorminhoco")
        print("0 - Sair do jogo")

        tipo = input("Escolha (0-4): ")

        if tipo == "0":
            print("\n📜 Histórico de escolhas:")
            for i, escolha in enumerate(historico, 1):
                print(f"{i}ª escolha: {escolha}")
            print(f"{nome_bichinho} vai dormir... ")
            break

        if tipo == "1":
            bicho = Lucky(nome_bichinho)
            historico.append("Lucky Básico")
        elif tipo == "2":
            cor_asa = input("Cor das asas: ")
            poder = input("Poder: ")
            cor_corpo = input("Cor do corpo: ")
            cor_cabelo = input("Cor do cabelo: ")
            bicho = LuckySkin(nome_bichinho, cor_asa, poder, cor_corpo, cor_cabelo)
            historico.append(f"Skin - Asa: {cor_asa}, Poder: {poder}, Corpo: {cor_corpo}, Cabelo: {cor_cabelo}")
        elif tipo == "3":
            musica = input("Música favorita: ")
            dancar = input("Dança favorita: ")
            pular = input("Como ele pula: ")
            skate = input("Estilo de skate: ")
            bicho = LuckyHobbies(nome_bichinho, musica, dancar, pular, skate)
            historico.append(f"Hobbies - Música: {musica}, Dança: {dancar}, Pulo: {pular}, Skate: {skate}") 
        elif tipo == "4":
            dormir = input("Como ele dorme: ")
            roncando = input("Tipo de ronco: ")
            cansado = input("Estado de cansaço: ")
            bicho = LuckyDorminhoco(nome_bichinho, dormir, roncando, cansado)
            historico.append(f"Dorminhoco - Dorme: {dormir}, Ronco: {roncando}, Cansaço: {cansado}")
        else:
            print("Opção inválida, tente novamente.")
            continue

        while True:
            print("\n--- Menu de Interação ---")
            print("1 - Alimentar")
            print("2 - Brincar")
            print("3 - Passagem do tempo")
            print("4 - Ver status")
            
            if isinstance(bicho, LuckySkin):
                print("5 - Mudar skin")
                print("6 - Mostrar skin")
                print("7 - Trocar poder")
            elif isinstance(bicho, LuckyHobbies):
                print("5 - Dançar música")
                print("6 - Pular")
                print("7 - Andar de skate")
            elif isinstance(bicho, LuckyDorminhoco):
                print("5 - Dormir")
                print("6 - Roncar")
                print("7 - Mostrar cansaço")

            print("9 - Voltar ao menu principal")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                qtd = int(input("Quanto deseja alimentar (0-100)? "))
                bicho.alimentar(qtd)
            elif escolha == "2":
                qtd = int(input("Quanto deseja brincar (0-100)? "))
                bicho.brincar(qtd)
            elif escolha == "3":
                bicho.passagemTempo()
                print("O tempo passou...")
            elif escolha == "4":
                bicho.status()
            elif escolha == "5":
                if isinstance(bicho, LuckySkin): #isinstance - verifica se um objeto é de uma determinada classe - retorna True ou False
                    bicho.mudar_skin()
                elif isinstance(bicho, LuckyHobbies):
                    bicho.dancar_musica()
                elif isinstance(bicho, LuckyDorminhoco):
                    bicho.dormirzinho()
            elif escolha == "6":
                if isinstance(bicho, LuckySkin):
                    bicho.mostrar_skin()
                elif isinstance(bicho, LuckyHobbies):
                    bicho.pularzinho()
                elif isinstance(bicho, LuckyDorminhoco):
                    bicho.fazer_ronco()
            elif escolha == "7":
                if isinstance(bicho, LuckySkin):
                    bicho.trocar_poder()
                elif isinstance(bicho, LuckyHobbies):
                    bicho.andar_de_skate()
                elif isinstance(bicho, LuckyDorminhoco):
                    bicho.mostrar_cansaco()
            elif escolha == "9":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida, tente novamente.")

main()
