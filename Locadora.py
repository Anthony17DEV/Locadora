from datetime import datetime, timedelta

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.disponivel = True

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, placa, quilometragem, valor_diaria):
        super().__init__(marca, modelo, ano)
        self.placa = placa
        self.quilometragem = quilometragem
        self.valor_diaria = valor_diaria

class Cliente:
    def __init__(self, nome, cliente_cpf):
        self.nome = nome
        self.cliente_cpf = cliente_cpf
        self.carros_alugados = []
    
    def alugar_carro(self, carro, dias):
        if carro.disponivel:
            alugel = Alugel(carro, self, datetime.today(), dias)
            carro.disponivel = False
            self.carros_alugados.append(alugel)

class Alugel:
    def __init__(self, carro, cliente, data_inicial, dias):
        self.carro = carro
        self.cliente = cliente
        self.data_inicial = data_inicial
        self.data_final = data_inicial + timedelta(days=dias)
        self.valor_alugel = dias * carro.valor_diaria
        self.valor_multa = 0

    def devolver(self):
        if datetime.today() > self.data_final:
            dias_atraso = (datetime.today() - self.data_final).days
            self.valor_multa = dias_atraso * 0.20 * self.carro.valor_diaria
        self.data_final = datetime.today()
    
    def __str__(self):
        return f"{self.carro.marca} {self.carro.modelo} ({self.carro.ano}) - {self.carro.placa}"
    
class App:
    def __init__(self):
        self.carros = []
        self.clientes = []

    def cadastrar_carro(self, carro):
        self.carros.append(carro)

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_carros_disponiveis(self):
        return [carro for carro in self.carros if carro.disponivel]
    
    def listar_carros_por_marca(self, marca):
        return [carro for carro in self.carros if carro.marca.lower() == marca.lower()]
    
    def listar_carros_por_ano(self, ano):
        return [carro for carro in self.carros if carro.ano == ano]
    
    def alugar_carro(self, cliente_cpf, placa, dias):
        cliente = next((c for c in self.carros if c.placa == placa), None)
        if cliente and carro:
            alugel = cliente.alugar_carro(carro, dias)
            if alugel:
                return f"{cliente}"
