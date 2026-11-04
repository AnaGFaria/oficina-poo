# Sistema de Oficina Mecânica
Sistema de gerenciamento de uma oficina mecânica desenvolvido em Python, com interface via terminal. O projeto permite cadastrar veículos, registrar ordens de serviço, adicionar diferentes tipos de serviços e emitir orçamentos com o cálculo automático dos valores.
O projeto foi desenvolvido com foco na aplicação prática dos conceitos de **Programação Orientada a Objetos (POO)**.

## Funcionalidades
- Cadastrar veiculos
- Registrar serviços (Troca de óleo e Alinhamento)
- Listar ordens de serviço
- Calcular o valor do orcamento
- Exibir o resumo da ordem de servico

## Tecnologias utilizadas
- **Python 3**

## Estrutura do projeto
```text
oficina-mecanica/
├── models/
│   ├── veiculo.py
│   ├── servico.py
│   ├── ordemservico.py
│   └── oficina.py
├── README.md
└── main.py
```

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Executa o menu interativo e coordena as operações do sistema. |
| `veiculo.py` | Define a classe `Veiculo` e valida seus atributos. |
| `servico.py` | Define a classe abstrata `Servico` e suas subclasses `TrocaOleo` e `Alinhamento`. |
| `ordemservico.py` | Gerencia os serviços de uma ordem e calcula o orçamento. |
| `oficina.py` | Gerencia os veículos cadastrados e as ordens de serviço. |

## 🖥️ Como executar
### Pré-requisitos

- Python 3 instalado.
- Terminal ou console compatível com a execução de programas Python.

### Passos
1. Entre na pasta do projeto:
   ```bash
   cd oficina-mecanica
   ```
2. Execute o programa:
   ```bash
   python main.py
   ```
   No Windows, também é possível utilizar:
   ```bash
   py main.py
   ```

## Menu do sistema
O sistema disponibiliza as seguintes operações:
```text
=================================================
                 OFICINA MECÂNICA
=================================================
1 - Cadastrar veículo
2 - Registrar serviço
3 - Listar ordens de serviço
4 - Exibir orçamento
0 - Sair
=================================================
```
### Fluxo de utilização
1. Cadastre um veículo informando sua placa, modelo e ano.
2. Crie uma nova ordem de serviço, informando o cliente e selecionando um veículo cadastrado.
3. Escolha o serviço desejado e informe os valores da mão de obra e dos custos adicionais.
4. Adicione outros serviços à mesma ordem, quando necessário.
5. Consulte as ordens registradas e emita os respectivos orçamentos.

## Conceitos de Programação Orientada a Objetos
O projeto aplica os seguintes conceitos:

### Encapsulamento
Os atributos das classes são protegidos por atributos privados, utilizando a convenção de nomes com dois sublinhados (`__`). O acesso aos dados do veículo é realizado por meio de propriedades implementadas com `@property` e setters.

### Herança
As classes `TrocaOleo` e `Alinhamento` herdam da classe abstrata `Servico`, compartilhando a estrutura básica de um serviço.

### Abstração
A classe `Servico` herda de `ABC` e define o método abstrato `calcular_valor()`, que deve ser implementado pelas subclasses concretas.

### Polimorfismo
Cada tipo de serviço implementa seu próprio cálculo de valor. A classe `OrdemServico` pode chamar `calcular_valor()` para diferentes serviços sem precisar conhecer os detalhes específicos de cada implementação.

## Armazenamento dos dados
Os veículos e as ordens de serviço são mantidos em memória durante a execução do programa. Portanto, os registros não são preservados automaticamente após o encerramento da aplicação.

## Objetivo acadêmico
Este projeto tem como objetivo consolidar os conhecimentos de Programação Orientada a Objetos em Python, aplicando classes, objetos, encapsulamento, herança, abstração, polimorfismo, propriedades e tratamento de exceções em um cenário prático de gerenciamento de uma oficina mecânica.

---

Desenvolvido como projeto prático de estudo de Programação Orientada a Objetos.

## Autor
Desenvolvido por Ana Gabriela de Faria
Estudante de Ciência da Computação