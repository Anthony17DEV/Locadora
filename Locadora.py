lista_veiculos = []
lista_clientes = []
aluguel_carro = []

class App():

    def alugar(self):

        self.cpf = str(input("Digite o CPF: "))
        while True:
            if not Cliente.existe_cliente(self):
                print("Novo Cadastro!")
                Cliente.novo_cliente(self)
            else:
                break
        Carro.listar_carro(self)
        Carro.buscar_carro_alugar(self)
        App.lista_aluguel(self)

    def lista_aluguel(self):
        alugado = {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg,
            'placa': self.placa,
            'ano': self.ano,
            'marca': self.marca,
            'modelo': self.modelo,
            'km': self.km,
            'aluguel': self.aluguel
        }
        aluguel_carro.append(alugado)
        print(aluguel_carro)

    def lista_alugados(self):
        if len(aluguel_carro) > 0:
            for i, loc in enumerate(aluguel_carro):
                print(f"Carro {i + 1}:")
                print(f"Nome: {loc['nome']}")
                print(f"CPF: {loc['cpf']}")
                print(f"RG: {loc['rg']}\n")
                print(f"Placa: {loc['placa']}")
                print(f"Ano: {loc['ano']}")
                print(f"Marca: {loc['marca']}")
                print(f"Modelo: {loc['modelo']}")
                print(f"Km: {loc['km1']}")
                print(f"Aluguel:{loc['aluguel']}")
            print(f"Total de veículos alugados é: {len(aluguel_carro)}\n")
        else:
            print("\nNenhum veículo alugado para listar! ")

    def menu(self):

        while True:
            print("Bem Vindo a locadora Rapazes")
            print("1 - Cadastrar novo veículo")
            print("2 - Cadastrar novo cliente")
            print("3 - Locação de veículo")
            print("4 - Relatório de locação")
            print("5 - Busca de veículos cadastrados")
            print("6 - Busca de clientes cadastrados")
            print("7 - Relatório de veículos cadastrados")
            print("8 - Relatório de clientes cadastrados")
            print("9 - Alterar dados veículos cadastrados")
            print("10 - Alterar dados clientes cadastrados")
            print("11 - Finalizar o programa !!!")

            while True:
                try:
                    opcao = int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")

            if opcao == 1:
                Carro.novo_carro(self)

            elif opcao == 2:
                Cliente.novo_cliente(self)

            elif opcao == 3:
                App.alugar(self)

            elif opcao == 4:
                App.lista_aluguel(self)

            elif opcao == 5:
                Carro.buscar_carro(self)

            elif opcao == 6:
                Cliente.buscar_cliente(self)

            elif opcao == 7:
                Carro.listar_carro(self)

            elif opcao == 8:
                Cliente.listar_cliente(self)

            elif opcao == 9:
                Carro.alterar_carro(self)

            elif opcao == 10:
                Cliente.alterar_cliente(self)

            elif opcao == 11:
                print("\nFinalizado!!!")
                break

            else:
                print("\nInválido!\n")

class Veiculo():
    def __int__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.alugado = False

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, placa, valor, km):
        super().__int__(marca, modelo, ano)
        self.placa = placa
        self.valor = valor
        self.km = km

    def novo_carro(self):
        while True:
            self.placa = str(input("\n\nPlaca: ")).upper()
            if not Carro.existe_carro(self):
                break
            else:
                print("\nJá cadastrado no sistema")
        self.ano = int(input("Ano: "))
        self.marca = str(input("Digite a marca: ")).upper()
        self.modelo = str(input("Digite o modelo: ")).upper()
        self.km = int(input("Quantos km já foram percorridos: "))
        self.aluguel = "DISPONIVEL"
        carro = {
            'placa': self.placa,
            'ano': self.ano,
            'marca': self.marca,
            'modelo': self.modelo,
            'km': self.km,
            'aluguel': self.aluguel
        }
        lista_veiculos.append(carro)
        print(lista_veiculos)

    def listar_carro(self):
        if len(lista_veiculos) > 0:
            for i, car in enumerate(lista_veiculos):
                print(f"Carro {i + 1}:")
                print(f"Placa: {car['placa']}")
                print(f"Ano: {car['ano']}")
                print(f"Marca: {car['marca']}")
                print(f"Modelo: {car['modelo']}")
                print(f"Km: {car['km']}")
                print(f"Aluguel:{car['aluguel']}")
            print(f"Total de veículos é: {len(lista_veiculos)}\n")
        else:
            print("\nNenhum veículo para listar! ")

    def buscar_carro(self):
        if len(lista_veiculos) > 0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in lista_veiculos:
                if car['placa'] == self.placa:
                    print(f"Placa: {car['placa']}")
                    print(f"Ano: {car['ano']}")
                    print(f"Marca: {car['marca']}")
                    print(f"Modelo: {car['modelo']}")
                    print(f"Km: {car['km']}")
                    print(f"Aluguel:{car['aluguel']}")
                    break
        else:
            print("Nenhum veiculo cadastrado")

    def buscar_carro_alugar(self):
        if len(lista_veiculos) > 0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in lista_veiculos:
                if car['aluguel'] == "ALUGADO":
                    print("Nenhum veiculo disponível para alugar TOPEZERA!")
                else:
                    if car['placa'] == self.placa:
                        print(f"Placa: {car['placa']}")
                        print(f"Ano: {car['ano']}")
                        print(f"Marca: {car['marca']}")
                        print(f"Modelo: {car['modelo']}")
                        print(f"Km: {car['km']}")
                        print(f"Aluguel:{car['aluguel']}")
                        if car['aluguel'] == "ALUGADO":
                            print("O veículo já está locado!")
                        else:
                            car['aluguel'] = "ALUGADO"
        else:
            print("Nenhum veiculo disponível para alugar!!!")

    def existe_carro(self): #quero
        if len(lista_veiculos) > 0:
            for car in lista_veiculos:
                if car['placa'] == self.placa:
                    return True
        return False

    def alterar_carro(self):
        if len(lista_veiculos) > 0:
            self.placa = str(input("Digite a placa : ")).upper()
            if Carro.existe_carro(self):
                for car in lista_veiculos:
                    if car['placa'] == self.placa:
                        print(f"\n\tPlaca: {car['placa']}")
                        print(f"\tAno: {car['ano']}")
                        print(f"\tMarca: {car['marca']}")
                        print(f"\tModelo: {car['modelo']}")
                        print(f"\tKm: {car['km']}")
                        print(f"\tAluguel: {car['aluguel']}\n")

                        car['placa'] = str(input("Placa:")).upper()
                        car['ano'] = str(input("Ano:"))
                        car['marca'] = str(input("Marca:")).upper()
                        car['modelo'] = str(input("modelo:")).upper()
                        car['km'] = int(input("Km: "))
                        car['aluguel'] = print(
                            f"\tAluguel: {car['aluguel']}\n")

                        print(f"Os dados da {self.placa} foram alterados")
                        break

            else:
                print(
                    f"Não existe veiculo cadastrado com a placa informado {self.placa}")
        else:
            print("Não existe veículo a ser alterado!")

class Cliente():
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

    def alterar_cliente(self):
        if len(lista_clientes) > 0:
            self.cpf = str(input("Digite o CPF : ")).upper()
            if Cliente.existe_cliente(self):
                for clt in lista_clientes:
                    if clt['cpf'] == self.cpf:
                        print(f"\n\tNome: {clt['nome']}")
                        print(f"\tCPF: {clt['cpf']}")
                        print(f"\tRG: {clt['rg']}")

                        clt['nome'] = str(input("Nome: ")).upper()
                        clt['cpf'] = str(input("CPF: "))
                        clt['rg'] = str(input("RG: "))

                        print(f"Os dados de {self.nome} foi alterado")
                        break

            else:
                print("Esse CPF não está cadastrado")
        else:
            print("Não existem clientes a serem alterados!")

    def listar_cliente(self):
        if len(lista_clientes) > 0:
            for i, clt in enumerate(lista_clientes):
                print(f"\nCliente {i + 1}:")
                print(f"Nome: {clt['nome']}")
                print(f"CPF: {clt['cpf']}")
                print(f"RG: {clt['rg']}\n")
            print(f"Total de clientes é: {len(lista_clientes)}\n")
        else:
            print("\nNenhum cliente para listar!\n")

    def buscar_cliente(self):
        if len(lista_clientes) > 0:
            self.cpf = str(input("Digite o cpf: ")).upper()
            for car in lista_clientes:
                if car['cpf'] == self.cpf:
                    print(f"\nNome: {car['nome']}")
                    print(f"CPF: {car['cpf']}")
                    print(f"RG: {car['rg']}\n")
                    break
        else:
            print("\nNenhum cliente cadastrado no sistema!\n")

    def existe_cliente(self):
        if len(lista_clientes) > 0:
            for clt in lista_clientes:
                if clt['cpf'] == self.cpf:
                    return True
        return False

    def novo_cliente(self):
        while True:
            self.cpf = str(input("Digite o CPF: "))
            if not Cliente.existe_cliente(self):
                break
            else:
                print("Já cadastrado no sistema")
        self.nome = str(input("Nome do cliente: ")).upper()
        self.rg = str(input("RG: "))
        usuario = {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg
        }

        lista_clientes.append(usuario)
        print(lista_clientes)


App.menu(self=App)
