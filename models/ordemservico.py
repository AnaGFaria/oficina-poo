from models.servico import Servico
from models.veiculo import Veiculo

class OrdemServico:
    def __init__(self, cliente, veiculo):
        if not isinstance(cliente, str) or not cliente.strip():
            raise ValueError("O nome do cliente é obrigatório")
        
        if not isinstance(veiculo, Veiculo):
            raise ValueError("Veículo inválido")

        self.__cliente = cliente.strip()
        self.__veiculo = veiculo
        self.__servicos = []

    @property
    def cliente(self):
        return self.__cliente

    @property
    def veiculo(self):
        return self.__veiculo

    def adicionar_servico(self, servico):
       if not isinstance(servico, Servico):
            raise ValueError("Serviço inválido")

       self.__servicos.append(servico)

    def calcular_valor_total(self):
         return sum(
            servico.calcular_valor()
            for servico in self.__servicos
        )

    def emitir_orcamento(self):
        print(f"Cliente: {self.__cliente}")
        print(f"Veiculo: {self.__veiculo.placa} - {self.__veiculo.modelo} ({self.__veiculo.ano})")
        for s in self.__servicos:
            print(f"{s.desc}: R$ {s.calcular_valor():.2f}")

        print(f"Total: R$ {self.calcular_valor_total():.2f}")

    def listar_servicos(self):
        return self.__servicos