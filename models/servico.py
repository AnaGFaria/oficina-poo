from abc import ABC, abstractmethod


class Servico(ABC):
  def __init__(self, desc, mao_de_obra):
    self.__desc = desc

    if not isinstance(mao_de_obra, (int, float)) or isinstance(mao_de_obra, bool):
        raise ValueError("O valor da mão de obra deve ser numérico.")

    if mao_de_obra < 0:
        raise ValueError("A mão de obra não pode ser negativa." )

    self.__mao_de_obra = mao_de_obra

  @property
  def desc(self):
    return self.__desc
  
  @property
  def mao_de_obra(self):
    return self.__mao_de_obra

  @abstractmethod
  def calcular_valor(self):
    pass

class TrocaOleo(Servico):
  def __init__(self, custos_materiais, mao_de_obra):
    super().__init__("Troca de Óleo", mao_de_obra)
    self.__custos_materiais = custos_materiais

  def calcular_valor(self):
    return self.mao_de_obra + self.__custos_materiais

class Alinhamento(Servico):
  def __init__(self, custos_equipamento, mao_de_obra):
    super().__init__("Alinhamento", mao_de_obra)

    self.__custos_equipamento = custos_equipamento

  def calcular_valor(self):
    return self.mao_de_obra + self.__custos_equipamento