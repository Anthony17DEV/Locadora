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
        self.clientes_cadastrados = [] #Lista para guardar os clientes, ainda não foi implementada

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
    
    def __init__(self):
        self.cliente = Cliente()



    def run(self):
        
        while True:

            print("1. Cadastrar veículo")
            print("2. Consultar disponibilidade de veículos")
            print("3. Listar veículos por marca")
            print("4. Listar veículos por modelo")
            print("5. Listar veículos por ano")
            print("6. Alugar veículos")
            print("7. Devolver veículos")
            print("8. Cadastrar Cliente")
            print("9. Lista de Clientes")
            print("0. Sair")

            escolha = int(input("Escolha uma opção: "))

            if (escolha == 1):

                marca = input("Marca: ")
                modelo = input("Modelo: ")
                ano = input("Ano: ")
                placa = input("Placa: ")
                quilometragem = input("Quilometragem: ")
                valor_da_diaria = input("Valor da diária: ")
                carro = Carro(marca, modelo, ano, placa, quilometragem, valor_da_diaria)
                self.disponivel.adicionar_carro(carro)
                print(f'{carro} cadastrado com sucesso!\n')

            elif (escolha == 2):

                Carro_Disponivel = self.disponivel.get_carros_disponiveis()
                if Carro_Disponivel:
                    print("Veículos disponíveis: ")
                    for carro in Carro_Disponivel:
                        print(f'- {carro}')
                else:
                    print("Não há veículos disponíveis no momento. ")
                print()

            elif (escolha == 3):

                marca = input("Marca: ")
                carros_por_marca = self.disponivel.get_carros_por_marca(marca)
                if carros_por_marca:
                    print(f'Veículos da marca {marca}')
                    for carro in carros_por_marca:
                        print(f'- {carro}')
                else:
                    print(f'Não há veículos da marca {marca}.')
                print()

            elif (escolha == 4):

                modelo = input("Modelo: ")
                carros_por_modelo = self.disponivel.get_carros_por_modelo(modelo)
                if carros_por_modelo:
                    print(f'Veículos do modelo {modelo}:')
                    for car in carros_por_modelo:
                        print(f'- {carro}')
                else:
                    print(f'Não há veículos do modelo {modelo}. ')

                print()

            elif (escolha == 5):

                modelo = input("Modelo: ")
                carros_por_ano = self.disponivel.get_carros_por_modelo(ano)
                if carros_por_ano:
                    print(f'Veículos do ano {ano}:')
                    for car in carros_por_ano:
                        print(f'- {carro}')
                else:
                    print(f'Não há veículos do modelo {ano}. ')

                print()


            elif (escolha == 6):

                lista = self.disponivel.carros  #talvez tenha de arrumar essa parte aqui

                carro_alugado = input("Qual carro você deseja alugar :")
                alugado = self.cliente.alugar_carro(carro_alugado)

                if alugado not in lista:
                    print("Impossível alugar um carro, que não está disponível!")

                else:
                    lista.append(alugado)    #talvez tenha de arrumar essa parte aqui pois já tem lá em cima.
                    print("Carro alugado com sucesso!")

            elif (escolha == 7):
                carro_devolvido = input("Digite o carro que você desejar devolver: ")
                self.cliente.devolver_carro(carro_devolvido)


            elif (escolha == 8):
                nome = input("Digite seu Nome para o cadastro: ")  
                id = input("Digite seu ID como cliente: ")   #ID talvez seria bom gerar aleatoriamente, se der.

                self.cliente.clientes_cadastrados.append(nome, id) #arrumar aqui ainda, ta meio na lógica

            elif (escolha == 9):
                print("")


            elif escolha == 0:
                print("\nLocadora Encerrada!\n")
                break


i = 1
App.run(i)
