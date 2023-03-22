import os #tirar na versao final, so coloquei pra ajudar na hora de limpar a idle
from datetime import *
from random import *

#Arrumar as entradas de dados, quando sai um Int ao inves de uma String, a locadora morre. Arrumar isso.
#Arrumar Data 
#Arrumar Quilometragem de cada carro - *Arrumada 19/03
#Arrumar Valor do aluguel e o atraso - *Arrumado o Valor do Aluguel 19/03, Arrumado o atraso do aluguel 22/03
#Arrumar Histórico de Carros de cada Cliente - *Arrumado o histórico 22/03


clientes_cadastrados = [] #Lista para guardar os clientes
historico = [] #Lista para guardar os carros alugados

class Veiculo():
    def _init_(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.disponivel = True
    
    def alugado(self):
        self.disponivel = False

    def devolvido(self):
        self.disponivel = True


class Carro(Veiculo): #Carro herda de veiculo
    def _init_(self, marca, modelo, ano, placa, quilometragem, valor_diaria):
        super()._init_(marca, modelo, ano)
        self.placa = placa
        self.quilometragem = quilometragem
        self.valor_diaria = valor_diaria

    def _str_(self):
        return f'{self.marca} {self.modelo} - Ano ({self.ano}) - Placa: {self.placa} - Valor da diária: {self.valor_diaria} R$ - Quilometragem do Carro: {self.quilometragem} Km'
    
    def valor_aluguel(self,dias):

        self.dias_alugados = dias
        self.valor_total = self.valor_diaria * dias

        return self.valor_total
    
    def devolver_aluguel(self, tempo):
        self.tempo = tempo

        if(tempo > self.dias_alugados):
            print("\nO carro está atrasado\n")
            diferenca = tempo - self.dias_alugados
            self.valor_final = (self.valor_diaria * self.dias_alugados) + ((self.valor_diaria + (self.valor_diaria * 0.20)) * diferenca)
        else:
            self.valor_final = self.valor_total 

        return self.valor_final      

    
    def mudanca_quilometragem(self, quilo):
        self.quilo = quilo
        self.quilometragem = quilo - self.quilometragem
        print("\nNova quilometragem do carro é : {} Km\n".format(self.quilometragem))


class Cliente():  #Arrumar, tirar essa classe de dentro
    def _init_(self,nome):
        self.nome = nome
        self.id = randint(1, 200)
        self.historico_clientes = [] #Lista para guardar os historicos dos clientes
 
#Talvez eu tenha feita uma seboseira aqui!
    def seu_historico(self):
        #print(self.historico_clientes)
        tam = len(self.historico_clientes)
        print(f"\nTamanho: {tam}\n")

        if(tam == 0):
            print("\nEsse Usuário nunca alugou nenhum carro!\n")
        else:
            print("\nDeu certo!\n")
            for carro in self.historico_clientes:
                print(f"Marca: {carro.marca}\nModelo: {carro.modelo}\nAno: {carro.ano}\nPlaca: {carro.placa}\nQuilometragem: {carro.quilometragem}\nValor da Diária: {carro.valor_diaria}")

    def base_pro_historico(self, carro):  
        self.historico_clientes.append(carro)
        tam2 = len(self.historico_clientes)
        print(f"\nTamanho: {tam2}\n")

        if(tam2 == 0):
            print("\nEsse Usuário nunca alugou nenhum carro!\n")
        else:
            print("\nDeu certo!\n")
            print(carro)

    def _str_(self):
       return f'Cliente: {self.nome} - {self.id}'
    

class Carro_Disponivel:
    def _init_(self):
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
    


class App(Carro): #Arrumar, tirar essa classe de dentro

    def _init_(self):
        self.disponivel = Carro_Disponivel()
        
    def cadastrar_cliente(nome): #Cadastro de clientes
        clientes_cadastrados.append(nome) 

    def alugar_carro(carro): 
        #carro.disponivel = False
        historico.append(carro)
            
    def devolver_carro(carro):
        #self.data = data
        #if carro in self.historico:
        if historico != 0:
            #carro.disponivel = True
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
            #print(f'{i + 1} - {lista_alugados[i]} pelo Cliente {clientes[i]}')  #{v[cliente_certo]}\n
             print(f'{i + 1} - {lista_alugados[i]} pelo Cliente ...')

           

    def mostrar():
        cliente = clientes_cadastrados
               
                    
        print("\nClientes Cadastrados: \n")
        i = 1
        for c in cliente:
           print(f'Nº {i} - {c} \n')
           i += 1    




    def run(self):
        
        
        cliente = Cliente("LEONARDO COUTO")
        
        App.cadastrar_cliente(cliente)

        #App.cadastrar_cliente(self,'LEONARDO COUTO') #Cadastrar um cliente
        historico.append(Carro('BMW', 'BM3', 2022, '1234', 12, 12)) #Cadastrar um carro alugado
        
        #Cadastrar alguns carros antes
        self.disponivel.adicionar_carro(Carro('FIAT', 'UNO', 2020, '1234', 12, 12))
        self.disponivel.adicionar_carro(Carro('FIAT', 'PULSE', 2020, '1234', 12, 12))
        self.disponivel.adicionar_carro(Carro('FIAT', 'PUNTO', 2020, '1234', 12, 12))
        #self.disponivel.adicionar_carro(Carro('FIAT', 'TORO', 2020, '1234', 12, 12))
        

        while True:

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

                marca = str(input("Marca: ")) #Colocar Marca e modelo Maisculos para facilitar a comparação
                marca2 = marca.upper() #Colocar Marca e modelo Maisculos para facilitar a comparação
                modelo = str(input("Modelo: ")) #Colocar Marca e modelo Maisculos para facilitar a comparação
                modelo2 = modelo.upper() #modelo em CAPSLOCK
                ano = int(input("Ano: "))
                placa = str(input("Placa: "))
                quilometragem = int(input("Quilometragem: "))
                valor_da_diaria = int(input("Valor da diária: "))
                carro = Carro(marca2, modelo2, ano, placa, quilometragem, valor_da_diaria)
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
                marca = str(input("Marca: "))
                marca2 = marca.upper() #marca em CAPSLOCK
                carros_por_marca = self.disponivel.get_carros_por_marca(marca2)
                if carros_por_marca:
                    print(f'Veículos da marca {marca2}')
                    for carro in carros_por_marca:
                        print(f'{i} - {carro}')
                        i = i + 1
                else:
                    print(f'Não há veículos da marca {marca2}.')

                print()

                os.system('pause')

            elif (escolha == 4):
                i = 1
                modelo = str(input("Modelo: "))
                modelo2 = modelo.upper() #modelo em CAPSLOCK
                carros_por_modelo = self.disponivel.get_carros_por_modelo(modelo2)
                if carros_por_modelo:
                    print(f'Veículos do modelo {modelo2}:')
                    for carro in carros_por_modelo:
                        print(f'{i} - {carro}')
                        i = i + 1
                else:
                    print(f'Não há veículos do modelo {modelo2}. ')

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
                    #cliente_certo = v.index(cliente_escolhido.upper())    

                    for cliente in v:
                        if cliente_escolhido == cliente.nome:
                            cliente_certo = cliente
                            print(cliente_certo)



                    tam = len(lista)
                    print("\nCarros Disponíveis para Aluguel: \n")
                    for i in range(0,tam):
                        print(f'{i + 1}- {lista[i]}\n')

                    carro_alugado = (int(input("Deseja Alugar qual carro?\nEscolha pela a numeração! ")) - 1)
                    

                    if carro_alugado > tam:
                        print("Impossível alugar um carro que não está na lista!")
                    
                    else:
                        
                        
                        
                        #Ver também de fazer a comparação normal

                        data = date.today()
                        data_certa = data.strftime('%d/%m')
                        
                        
                        tempo_de_aluguel = int(input("Deseja alugar o carro por quantos dias: "))
                        dia = timedelta(days= tempo_de_aluguel)
                        data_de_entrega = data + dia
                        
                        
                        valor = lista[carro_alugado]
                        
                        total = valor.valor_aluguel(tempo_de_aluguel)
                        #Arrumar aqui depois, ja que to pegando pela a Classe (Carro)

                        '''
                        print("\nLista de Clientes Disponíveis: \n")
                        for i in range(0, len(clientes_cadastrados)):
                            print(f'Nº {i + 1} - {clientes_cadastrados[i]}\n')
                        '''
                        
                    
                        App.alugar_carro(lista[carro_alugado])


                        #print(v[cliente_certo])

                        #c = Cliente(v[cliente_certo])
                        #c = Cliente(cliente_certo)
                        #c = v[cliente_certo]
                        

                        #c = testando()
                        
                        
                        #teste_cliente = Cliente(v[cliente_alternativo])
                        
                        cliente_certo.base_pro_historico(lista[carro_alugado])
                        #teste_cliente.base_pro_historico(lista[carro_alugado])

                        lista.pop(carro_alugado)

                        
                        #print(f"\nCarro alugado com sucesso na Data: {data_certa} pelo o Cliente {v[cliente_certo]}\n")
                        print(f"\nCarro alugado com sucesso na Data: {data_certa} pelo o Cliente {cliente_certo}\n")
                        print(f"\nData de entrega do Carro é: {data_de_entrega}\n")
                        print(f"Valor a se pagar no final do aluguel : {total} R$")

                       

                    os.system('pause')
                    
            elif (escolha == 7):

                lista_alugados = historico
                lista = self.disponivel.carros
                
                data = date.today()
                data_certa = data.strftime('%d/%m')

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
                    #Arrumar aqui depois, ja que to pegando pela a Classe (Carro)

                    
                        
                    total2 = carro_d.devolver_aluguel(tempo) #o 0 significa o tempo de atraso, ajustar isso ainda
                    #Arrumar aqui depois, ja que to pegando pela a Classe (Carro)
                    
                    #Ver também de fazer a comparação normal

                    if carro_devolvido > tam:
                        print("Impossível devolver um carro que não está na lista!")
                    else: 
                        lista.append(lista_alugados[carro_devolvido])
                        App.devolver_carro(carro_devolvido)

                        carro_d.mudanca_quilometragem(nova_quilometragem)
                        #Arrumar aqui depois, ja que to pegando pela a Classe (Carro)

                        print(f"\nCarro devolvido com sucesso na data {data_certa} pelo o Cliente ...\n")
                        #print(f"\nData de entrega do Carro é: {data_de_entrega}\n")
                        print(f"\nValor a se pagar no final do aluguel : {total2} R$\n")


                os.system('pause')

            elif (escolha == 8):
                nome = str(input("Digite seu Nome para o cadastro: "))  
                #id = input("Digite seu ID como cliente: ")   #ID talvez seria bom gerar aleatoriamente, se der.
                App.cadastrar_cliente(nome.upper())
                
                os.system('pause')

            elif (escolha == 9):
                clientes = clientes_cadastrados
                historico_c = cliente.historico_clientes
                tam = len(clientes_cadastrados)
                #tam2 = len(self.cliente.historico_clientes)
                '''
                print("\nClientes Cadastrados: \n")
                i = 1
                for cliente in clientes:
                    print(f'Nº {i} - {cliente} - {self.cliente.id}\n')
                    i += 1
                '''
                App.mostrar()
                hist = (int(input("Deseja ver o histórico de carros de qual cliente cadastrado? Escolha pela a numeração: ")) - 1)
               
                cliente_ok = clientes[hist]
                #cliente_ok = Cliente(clientes[hist])
                #cliente_ok = clientes[hist]
                #antigo_cliente = Cliente(cliente_ok)
                cliente_ok.seu_historico()
                
                #cliente_ok.self.cliente.seu_historico()
                        
                     
                    

                os.system('pause')

            elif (escolha == 10):
               
                
                App.historico_carros_alugado()

                os.system('pause')

            elif escolha == 0:
                print("\nLocadora Encerrada!\n")
                break




app = App()
app.run()
