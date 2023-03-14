class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.disponivel = True
    
    def alugado(self):
        self.disponivel = False

    def devolvido(self):
        self.disponivel = True

class Carro(Veiculo): #Carro herda de veiculo
    def __init__(self, marca, modelo, ano, placa, quilometragem, valor_diaria):
        super().__init__(marca, modelo, ano)
        self.placa = placa
        self.quilometragem = quilometragem
        self.valor_diaria = valor_diaria

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano}) - placa {self.placa}'
    
class Cliente:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.historico = [] #Lista para guardar os carros alugados

    def alugar_carro(self, carro):
        if carro.disponivel:
            carro.disponivel = False
            self.historico.append(carro)
            return True
        else:
            return False
    
    def devolver_carro(self, carro):
        if carro in self.historico:
            carro.disponivel = True
            self.historico.remove(carro)

class Carro_Disponivel:
    def __init__(self):
        self.carros = [] #Cria uma lista para armazenar os carros

    def adicionar_carro(self, carro):
        self.carros.append(carro)
    
    def get_carros_disponiveis(self):
        return [carro for carro in self.carros if carro.disponivel]
    
    def get_carros_por_marca(self, marca):
        return [carro for carro in self.carros if carro.marca == marca]
    
    def get_carros_por_modelo(self, modelo):
        return [carro for carro in self.carros if carro.modelo == modelo]
    
    def get_carros_por_ano(self, ano):
        return [carro for carro in self.carros if carro.ano == ano]
    
class App:
    def __init__(self):
        self.disponivel = Carro_Disponivel()

    def run(self):
        while True:
            print("1. Cadastrar veículo")
            print("2. Consultar disponibilidade de veículos")
            print("3. Listar veículos por marca")
            print("4. Listar veículos por modelo")
            print("5. Listar veículos por ano")
            print("0. Sair")
            escolha = input("Escolha uma opção: ")
            if escolha == '1':
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                ano = input("Ano: ")
                placa = input("Placa: ")
                quilometragem = input("Quilometragem: ")
                carro = Carro(marca, modelo, ano, placa, quilometragem)
                self.disponivel.adicionar_carro(carro)
                print(f'{carro} cadastrado com sucesso!\n')
            elif escolha == '2':
                Carro_Disponivel = self.disponivel.get_carros_disponiveis()
                if Carro_Disponivel:
                    print("Veículos disponíveis: ")
                    for carro in Carro_Disponivel:
                        print(f'- {carro}')
                else:
                    print("Não há veículos disponíveis no momento. ")
                print()
            elif escolha == '3':
                marca = input("Marca: ")
                carros_por_marca = self.disponivel.get_carros_por_marca(marca)
                if carros_por_marca:
                    print(f'Veículos da marca {marca}')
                    for carro in carros_por_marca:
                        print(f'- {carro}')
                else:
                    print(f'Não há veículos da marca {marca}.')
                print()
            elif escolha == '4':
                modelo = input("Modelo: ")
                carros_por_modelo = self.disponivel.get_carros_por_modelo(modelo)
                if carros_por_modelo:
                    print(f'Veículos do modelo {modelo}:')
                    for car in carros_por_modelo:
                        print(f'- {carro}')
                else:
                    print(f'Não há veículos do modelo {modelo}. ')
                print()
            
