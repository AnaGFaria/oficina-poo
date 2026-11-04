class Veiculo:
    def __init__(self, placa, modelo, ano):
        self.__placa = placa
        self.__modelo = modelo
        self.__ano = ano

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, nova_placa):
       if not nova_placa or not nova_placa.strip():
           raise ValueError("A placa é obrigatória.")

       self.__placa = nova_placa.strip().upper()

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, novo_modelo):
       if not novo_modelo or not novo_modelo.strip():
           raise ValueError("O modelo é obrigatório.")

       self.__modelo = novo_modelo.strip().upper()

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        if not isinstance(novo_ano, int) or isinstance(novo_ano, bool):
            raise ValueError("O ano deve ser um número inteiro.")

        if novo_ano <= 0:
            raise ValueError("O ano deve ser válido.")
 
        self.__ano = novo_ano