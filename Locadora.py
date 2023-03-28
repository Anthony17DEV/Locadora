import os 
from datetime import *
from random import *


clientes_cadastrados = [] #Lista para guardar os clientes
historico = [] #Lista para guardar os carros alugados

class Veiculo(): #Classe Veiculo
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

    def __str__(self): #Mostrar informações do carro
        return f'{self.marca} {self.modelo} - Ano ({self.ano}) - Placa: {self.placa} - Valor da diária: {self.valor_diaria} R$ - Quilometragem do Carro: {self.quilometragem} Km'
    
    def valor_aluguel(self, dias, data):
        self.data = data #data de entrega
        self.dias_alugados = dias #tempo de aluguel
        self.valor_total = self.valor_diaria * dias
        
        return self.valor_total
    
    def devolver_aluguel(self, tempo):
        self.tempo = tempo

        if(tempo != 0): #Calculo do tempo de atraso
            tempo_tratado = timedelta(days= tempo)
            print(f"\nO carro está atrasado em {tempo} dias\n")
            diferenca = tempo - self.dias_alugados
            self.valor_final = ((self.valor_diaria * self.dias_alugados) + ((self.valor_diaria + (self.valor_diaria * 0.20)) * diferenca) + self.valor_total)
            print(f"\nCarro devolvido com sucesso, em atraso na data {self.data + tempo_tratado}\n")

        else:
            self.valor_final = self.valor_total 
            print(f"\nCarro devolvido com sucesso na data {self.data}\n") 
        return self.valor_final      

    
    def mudanca_quilometragem(self, quilo): #Quilometragem do carro quando devolvido
        self.quilo = quilo
        a = quilo - self.quilometragem
        print("\nKM rodado durante o aluguel do carro é : {} Km\n".format(a))
        self.quilometragem = quilo 

class Cliente():  
    def __init__(self,nome):
        self.nome = nome
        self.id = randint(1, 200) #Gerar o ID automaticamente
        self.historico_clientes = [] #Lista para guardar os historicos dos clientes

    def seu_historico(self): #Buscando o historico do cliente
        tam = len(self.historico_clientes)

        if(tam == 0):
            print("\nEsse Usuário nunca alugou nenhum carro!\n")
        else:
            for carro in self.historico_clientes:
                print(f"\nMarca: {carro.marca}\nModelo: {carro.modelo}\nAno: {carro.ano}\nPlaca: {carro.placa}\nQuilometragem: {carro.quilometragem}\nValor da Diária: {carro.valor_diaria}\n")

    def base_pro_historico(self, carro):  #Adicionando o carro no historico do cliente
        self.historico_clientes.append(carro)
        tam2 = len(self.historico_clientes)

    def __str__(self):
       return f'Cliente: {self.nome} - {self.id}'
    

class Carro_Disponivel(): #Classe pra conferir as disponibilidades dos carros
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
    


class App(Carro): #Classe app herda carro pra poder acessar as informações

    def __init__(self):
        self.disponivel = Carro_Disponivel()
        
    def cadastrar_cliente(nome): #Cadastro de clientes
        clientes_cadastrados.append(nome) 

    def alugar_carro(carro): 
        historico.append(carro)
            
    def devolver_carro(carro):
        if historico != 0:
            historico.pop(carro)
        else:
            return False  

    def historico_carros_alugado():
        lista_alugados = historico
                
        tam = len(lista_alugados)
                
        if tam == 0:
             print("\nNenhum carro está alugado no momento!\n")

        else:
            print("\nCarros em Aluguel: \n")
            for i in range(0,tam):
             print(f'{i + 1} - {lista_alugados[i]}')

        
    def mostrar():
        cliente = clientes_cadastrados          
        print("\nClientes Cadastrados: \n")
        i = 1
        for c in cliente:
           print(f'{i} - {c} \n')
           i += 1    


    def run(self):
        
        
        cliente = Cliente("LEONARDO COUTO") #Cadastro de Cliente
        
        App.cadastrar_cliente(cliente) #Cadastro de Cliente
        
        #Cadastrar alguns carros antes
        self.disponivel.adicionar_carro(Carro('FIAT', 'UNO', 2020, 'ABC1235', 0, 50))
        self.disponivel.adicionar_carro(Carro('FIAT', 'PULSE', 2020, 'ABC1234', 0, 50))
        self.disponivel.adicionar_carro(Carro('FIAT', 'PUNTO', 2020, 'ABC1224', 0, 50))
        self.disponivel.adicionar_carro(Carro('FIAT', 'TORO', 2020, 'ABC1134', 10, 50))
        

        while True: #Menu

            os.system('clear||cls')

            print("\nBem-Vindo a Locadora de Carros dos Rapazes\n")
            print("1. Cadastrar veículo")
            print("2. Consultar disponibilidade de veículos")
            print("3. Listar veículos por marca")
            print("4. Listar veículos por modelo")
            print("5. Listar veículos por ano")
            print("6. Alugar veículos")
            print("7. Devolver veículos")
            print("8. Cadastrar Cliente")
            print("9. Lista de Clientes e Histórico")
            print("10. Lista de Carros alugados")
            print("0. Sair")

            escolha = int(input("Escolha uma opção: "))

            if (escolha == 1):

                marca = (str(input("Marca: ")).upper()) #Colocar Marca e modelo Maisculos para facilitar a comparação
                modelo = (str(input("Modelo: ").upper())) #Colocar Marca e modelo Maisculos para facilitar a comparação
                ano = int(input("Ano: "))
                placa = str(input("Placa: "))
                quilometragem = int(input("Quilometragem: "))
                valor_da_diaria = int(input("Valor da diária: "))
                
                carro = Carro(marca, modelo, ano, placa, quilometragem, valor_da_diaria)
                self.disponivel.adicionar_carro(carro)
                print(f'{carro} cadastrado com sucesso!\n')

                os.system('pause')

            elif (escolha == 2):
                i = 1
                Carro_Disponivel = self.disponivel.get_carros_disponiveis()
                if Carro_Disponivel:
                    print("Veículos disponíveis: ")
                    for carro in Carro_Disponivel:
                        print(f'{i} - {carro}')
                        i = i + 1
                else:
                    print("Não há veículos disponíveis no momento. ")
                print()

                os.system('pause')

            elif (escolha == 3):
                i = 1
                marca = (str(input("Marca: ")).upper()) #marca em CAPSLOCK   
                carros_por_marca = self.disponivel.get_carros_por_marca(marca)
                if carros_por_marca:
                    print(f'Veículos da marca {marca}')
                    for carro in carros_por_marca:
                        print(f'{i} - {carro}')
                        i = i + 1
                else:
                    print(f'Não há veículos da marca {marca}.')

                print()

                os.system('pause')

            elif (escolha == 4):
                i = 1
                modelo = (str(input("Modelo: ").upper())) #modelo em CAPSLOCK
                carros_por_modelo = self.disponivel.get_carros_por_modelo(modelo)
                if carros_por_modelo:
                    print(f'Veículos do modelo {modelo}:')
                    for carro in carros_por_modelo:
                        print(f'{i} - {carro}')
                        i = i + 1
                else:
                    print(f'Não há veículos do modelo {modelo}. ')

                print()

                os.system('pause')

            elif (escolha == 5):
                i = 1
                ano = int(input("Ano: "))
                carros_por_ano = self.disponivel.get_carros_por_ano(ano)
                if carros_por_ano:
                    print(f'Veículos do ano {ano}:')
                    for carro in carros_por_ano:
                        print(f'{i} - {carro}')
                        i = i + 1
                else:
                    print(f'Não há veículos do modelo {ano}. ')

                print()

                os.system('pause')

            elif (escolha == 6):

                lista = self.disponivel.carros #para pegar a lista de carros disponíveis para aluguel
                
                if not lista: #se a lista de carros disponiveis estiver vazia
                    print("Impossível alugar um carro, pois não tem nenhum disponível!")
                    os.system("pause")

                else: #se a lista de carros disponiveis não estiver vazia
                    
                    App.mostrar()
                    cliente_escolhido = (str(input("Qual o cliente que deseja alugar o carro? Digite pelo o Nome: ")).upper())

                    v = clientes_cadastrados 
                    for cliente in v:
                        if cliente_escolhido == cliente.nome:
                            cliente_certo = cliente
                            
                    tam = len(lista)
                    print("\nCarros Disponíveis para Aluguel: \n")
                    for i in range(0,tam):
                        print(f'{i + 1}- {lista[i]}\n')

                    carro_alugado = (int(input("Deseja Alugar qual carro?\nEscolha pela a numeração! ")) - 1)

                    if carro_alugado > tam:
                        print("Impossível alugar um carro que não está na lista!")
                    
                    else:
                    
                        #Ver também de fazer a comparação normal

                        #Variaveis da data
                        data = date.today()
                        data_certa = data.strftime('%d/%m')
                        
                        #Tratamento do tempo
                        tempo_de_aluguel = int(input("Deseja alugar o carro por quantos dias: "))
       
                        dia = timedelta(days= tempo_de_aluguel)
                        data_de_entrega = data + dia
                        
                        valor = lista[carro_alugado] #valor pega a o carro na posição da lista
                         
                        total = valor.valor_aluguel(tempo_de_aluguel, data_de_entrega) #total pega o retorno da função valor_aluguel, com o valor do aluguel

                        App.alugar_carro(lista[carro_alugado]) #Envio do carro pra alugar na função alugar_carro

                        cliente_certo.base_pro_historico(lista[carro_alugado]) 
                        lista.pop(carro_alugado) #Tira o carro da lista dos carros disponíveis

                    
                        print(f"\nCarro alugado com sucesso na Data: {data_certa} pelo o {cliente_certo}\n") #Nome do cliente
                        print(f"\nData de entrega do Carro é: {data_de_entrega}\n") #Data de entrega do Carro
                        print(f"Valor a se pagar no final do aluguel : {total} R$") #Valor do aluguel

                       

                    os.system('pause')
                    
            elif (escolha == 7):

                lista_alugados = historico
                lista = self.disponivel.carros
                
                data = date.today()
                
                if not lista_alugados:
                    print("Nenhum carro está alugado!")

                else:
                    tam = len(lista_alugados)
                    
                    print("\nCarros em Aluguel: \n")
                    for i in range(0,tam):
                        print(f'{i + 1} - {lista_alugados[i]}\n')


                    carro_devolvido = (int(input("Digite o carro que você desejar devolver: ")) - 1)
                   
                    nova_quilometragem = int(input("Digite a Quilometragem Final do Carro: "))
                    

                    tempo = int(input("O carro foi devolvido quantos dias após o aluguel? "))
                    

                    carro_d = lista_alugados[carro_devolvido]
                    v = clientes_cadastrados 

                    for cliente in v:
                        if cliente_escolhido == cliente.nome:
                            cliente_certo = cliente
                            
                
                    total2 = carro_d.devolver_aluguel(tempo)

                    if carro_devolvido > tam:
                        print("Impossível devolver um carro que não está na lista!")
                    else: 
                        lista.append(lista_alugados[carro_devolvido])
                        App.devolver_carro(carro_devolvido)

                        carro_d.mudanca_quilometragem(nova_quilometragem)

                        print(f"{cliente_certo}\n")
                        print(f"\nValor a se pagar no final do aluguel : {total2} R$\n")


                os.system('pause')

            elif (escolha == 8):
                nome = (str(input("Digite seu Nome para o cadastro: ")).upper()) 
                while not nome[0].isalpha():
                        if not nome.isalpha():
                            print("Por favor digite uma palavra:")
                            nome = (str(input("Digite seu Nome para o cadastro: ")).upper()) 
                        else:
                            break 

                nome = Cliente(nome)
                App.cadastrar_cliente(nome)
                print("Cliente cadastrado!")
                os.system('pause')

            elif (escolha == 9):
                clientes = clientes_cadastrados
                tam = len(clientes_cadastrados)
                
                App.mostrar()

                hist = (int(input("Deseja ver o histórico de carros de qual cliente cadastrado? Escolha pela a numeração: ")) - 1)
            

                cliente_ok = clientes[hist]   
                cliente_ok.seu_historico()
                
                os.system('pause')

            elif (escolha == 10):    
                App.historico_carros_alugado()

                os.system('pause')

            elif escolha == 0:
                print("\nLocadora Encerrada!\n")
                break

app = App()
app.run()
