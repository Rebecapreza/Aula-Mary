class veiculo:
    def __init__(self, marca, ano_fab, cor, qnt_porta, modelo):
        self.marca = marca
        self.ano_fab = ano_fab
        self.cor = cor
        self.qtd_porta = qnt_porta
        self.modelo = modelo


    def andar (self):
        print(f"{self.modelo} andando")

    def parar (self):
        print(f'{self.modelo} parando')

    def abastecimento(self):
        print(f'{self.modelo} está abastecendo')


        
class carros:
    def __init__(self, marca, ano_fab, cor, qnt_porta, modelo, musica):
        self.marca = marca
        self.ano_fab = ano_fab
        self.cor = cor
        self.qtd_porta = qnt_porta
        self.modelo = modelo
        self.musica = musica


    def imprimir(self):
        print("O veículo tem características: \n"
              f"Marca: {self.marca}\n"
              f"Modelo: {self.modelo}\n"
              f"Ano de fabricação: {self.ano_fab}\n"
              f"Cor: {self.cor}\n"
              f"Quantidade de porta: {self.qtd_porta}\n"
              f"A música que está tocando é: {self.musica}\n")

class caminhoes:
    def __init__(self, marca, ano_fab, cor, qnt_porta, modelo, motorista):
        self.marca = marca
        self.ano_fab = ano_fab
        self.cor = cor
        self.qtd_porta = qnt_porta
        self.modelo = modelo
        self.motorista = motorista

    def imprimir(self):
        print("O veículo tem características: \n"
              f"Marca: {self.marca}\n"
              f"Modelo: {self.modelo}\n"
              f"Ano de fabricação: {self.ano_fab}\n"
              f"Cor: {self.cor}\n"
              f"Quantidade de porta: {self.qtd_porta}\n"
              f"A motorista desse caminhão é: {self.motorista} \n")
        

class motos:
    def __init__(self, marca, ano_fab, cor, modelo):
        self.marca = marca
        self.ano_fab = ano_fab
        self.cor = cor
        self.modelo = modelo

    def imprimir(self):
        print("O veículo tem características: \n"
              f"Marca: {self.marca}\n"
              f"Modelo: {self.modelo}\n"
              f"Ano de fabricação: {self.ano_fab}\n"
              f"Cor: {self.cor}\n")



def main ():
    carro = carros("Chevrolet", 2008, "preto", 4, "onix", "Céu explica tudo - Henrique e Juliano")
    carro.imprimir()
    moto = motos("Kawasaki", 2004, "verde", "Kawasaki Ninja ZX-10R")
    moto.imprimir()
    caminhao = caminhoes("Mercedes Benz", 2025, "cinza", 2, "Axor 2545 S", "Mariany")
    caminhao.imprimir()

main()