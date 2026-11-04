from models.oficina import Oficina
from models.veiculo import Veiculo
from models.ordemservico import OrdemServico
from models.servico import TrocaOleo, Alinhamento

import os

def main():
    oficina = Oficina()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=================================================")
        print("                 OFICINA MECÂNICA                ")
        print("=================================================")
        print("1 - Cadastrar veículo")
        print("2 - Registrar serviço")
        print("3 - Listar ordens de serviço")
        print("4 - Exibir orçamento")
        print("0 - Sair")
        print("_________________________________________________")
        opcao = input("\nEscolha uma opção: ")

        try:
            if opcao == "1":
                cadastrar_veiculo(oficina)
                input("Digite qualquer tecla para sair...")

            elif opcao == "2":
                registrar_servico(oficina)
                input("Digite qualquer tecla para sair...")

            elif opcao == "3":
                listar_servicos(oficina)
                input("Digite qualquer tecla para sair...")

            elif opcao == "4":
                exibir_orcamento(oficina)
                input("Digite qualquer tecla para sair...")

            elif opcao == "0":
               print("Fechando...")
               break
            
            else:
               print("Opção inválida.")

        except ValueError as erro:
            print(f"\nErro: {erro}")
            input("\nPressione Enter para continuar...")

def cadastrar_veiculo(oficina):
    placa = input("Digite a placa do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = int(input("Digite o ano do veículo: "))

    veiculo = Veiculo(placa, modelo, ano)
    oficina.cadastrar_veiculo(veiculo)

    print(f"\nVeículo {veiculo.placa} cadastrado com sucesso!")

def registrar_servico(oficina):
    ordens = oficina.listar_ordens_servico()

    print("1 - Criar nova ordem de serviço")
    print("2 - Adicionar serviço a uma ordem existente")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cliente = input("Informe o nome do cliente: ")
        placa = input("Digite a placa do veículo: ")

        veiculo = oficina.buscar_veiculo_por_placa(placa)

        if veiculo is None:
            print("Veículo não encontrado.")
            return

        ordem = OrdemServico(cliente, veiculo)
        nova_ordem = True

    elif opcao == "2":
        if not ordens:
            print("Nenhuma ordem de serviço registrada.")
            return

        listar_servicos(oficina)
        numero = int(input("Escolha a ordem de serviço: "))

        if numero < 1 or numero > len(ordens):
            print("Ordem inválida.")
            return

        ordem = ordens[numero - 1]
        nova_ordem = False

    else:
        print("Opção inválida.")
        return
        
    print("\n\n--------------- Tipos de Serviços ---------------")
    print("1 - Troca de Óleo")
    print("2 - Alinhamento")

    servico_op = input("Escolha o serviço desejado: ")

    if servico_op not in ("1", "2"):
        print("Serviço inválido.")
        return

    mao_de_obra = float(input("Mão de obra: R$ "))
    custos = float(input("Custos adicionais: R$ "))

    if (servico_op == "1"):
        servico = TrocaOleo(custos, mao_de_obra)
    elif (servico_op == "2"):
        servico = Alinhamento(custos, mao_de_obra)

    ordem.adicionar_servico(servico)

    if nova_ordem:
        oficina.registrar_ordem_servico(ordem)

    print("Serviço adicionado à ordem com sucesso!")
    print(f"Total atualizado: R$ {ordem.calcular_valor_total():.2f}")

def listar_servicos(oficina):
    ordens_servico = oficina.listar_ordens_servico()

    if not ordens_servico:
        print("Nenhuma ordem de serviço registrada.")
        return

    print("=================================================")
    print("                SERVIÇOS LANÇADOS                ")
    print("=================================================")
    for i, servico in enumerate(ordens_servico, start=1):
        print(f"Serviço {i}")
        servico.emitir_orcamento()
        print("_________________________________________________")


def exibir_orcamento(oficina):
    ordens_servico = oficina.listar_ordens_servico()

    if not ordens_servico:
        print("Nenhuma ordem de serviço registrada.")
        return

    print("========== ORDENS DE SERVIÇO ==========")

    for i, ordem in enumerate(ordens_servico, start=1):
        print(f"{i} - Ordem de serviço {i}")

    try:
        numero = int(input("Escolha a ordem de serviço: "))

        if numero < 1 or numero > len(ordens_servico):
            print("Número de ordem inválido.")
            return

        ordem = ordens_servico[numero - 1]

        print("\n========== ORÇAMENTO ==========")
        ordem.emitir_orcamento()

    except ValueError:
        print("Digite um número inteiro válido.")



if __name__ == "__main__":
    main()