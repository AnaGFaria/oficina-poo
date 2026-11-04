from models.servico import Servico
from models.veiculo import Veiculo
from models.ordemservico import OrdemServico

class Oficina:
    def __init__(self):
        self.__veiculos = []
        self.__ordens_servico = []

    def cadastrar_veiculo(self, veiculo):
        if not isinstance(veiculo, Veiculo):
            raise ValueError("Veículo inválido.")
        
        if self.buscar_veiculo_por_placa(veiculo.placa):
            raise ValueError("Já existe um veículo cadastrado com essa placa.")
        
        self.__veiculos.append(veiculo)

    def registrar_ordem_servico(self, ordem):
        if not isinstance(ordem, OrdemServico):
            raise ValueError("Ordem de serviço inválida.")

        self.__ordens_servico.append(ordem)

    def listar_veiculos(self):
        return self.__veiculos

    def listar_ordens_servico(self):
        return self.__ordens_servico

    def buscar_veiculo_por_placa(self, placa):
        if not isinstance(placa, str):
            return None
        
        placa = placa.strip().upper()

        for veiculo in self.__veiculos:
            if placa == veiculo.placa:
                return veiculo

        return None