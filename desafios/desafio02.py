from abc import ABC, abstractmethod
from datetime import datetime


# =========================
# HISTÓRICO
# =========================
class Historico:
    def __init__(self):
        # Armazena todas as transações da conta
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        # Registra uma transação com tipo, valor e data/hora
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,  # Nome da classe (Deposito/Saque)
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


# =========================
# CONTA
# =========================
class Conta:
    def __init__(self, numero, cliente):
        # Dados básicos da conta
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente

        # Cada conta possui seu próprio histórico
        self.historico = Historico()

    def sacar(self, valor):
        # Validação de saldo
        if valor > self.saldo:
            print("❌ Saldo insuficiente")
            return False

        # Validação de valor inválido
        if valor <= 0:
            print("❌ Valor inválido")
            return False

        # Executa saque
        self.saldo -= valor
        return True

    def depositar(self, valor):
        # Validação de valor inválido
        if valor <= 0:
            print("❌ Valor inválido")
            return False

        # Executa depósito
        self.saldo += valor
        return True


# ContaCorrente herda de Conta e adiciona regras específicas
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)

        # Limite de crédito e limite de saques
        self.limite = limite
        self.limite_saques = limite_saques


# =========================
# CLIENTE
# =========================
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []  # Um cliente pode ter várias contas

    def realizar_transacao(self, conta, transacao):
        # O cliente delega a execução da transação
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        # Associa uma conta ao cliente
        self.contas.append(conta)


# Representa uma pessoa física
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)

        # Dados pessoais
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# =========================
# TRANSAÇÕES (ABSTRAÇÃO)
# =========================
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        # Toda transação precisa ter um valor
        pass

    @abstractmethod
    def registrar(self, conta):
        # Toda transação precisa saber como se aplicar a uma conta
        pass


# =========================
# DEPÓSITO
# =========================
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor  # atributo "protegido"

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Executa depósito
        if conta.depositar(self.valor):
            # Se deu certo, registra no histórico
            conta.historico.adicionar_transacao(self)
            print("✅ Depósito realizado com sucesso!")


# =========================
# SAQUE
# =========================
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Executa saque
        if conta.sacar(self.valor):
            # Se deu certo, registra no histórico
            conta.historico.adicionar_transacao(self)
            print("✅ Saque realizado com sucesso!")


# =========================
# FUNÇÕES DO MENU (VERSÃO 2)
# =========================

def criar_cliente(clientes):
    # Solicita CPF
    cpf = input("Informe o CPF: ")

    # Verifica se já existe cliente com esse CPF
    for cliente in clientes:
        if cliente.cpf == cpf:
            print("❌ Cliente já existe!")
            return

    # Coleta dados do cliente
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    endereco = input("Endereço: ")

    # Cria cliente e adiciona na lista
    cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
    clientes.append(cliente)

    print("✅ Cliente criado com sucesso!")


def criar_conta(clientes, contas):
    cpf = input("Informe o CPF do cliente: ")

    # Busca cliente pelo CPF (uso de generator expression 👀)
    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if not cliente:
        print("❌ Cliente não encontrado!")
        return

    # Gera número da conta automaticamente
    numero_conta = len(contas) + 1

    conta = ContaCorrente(numero_conta, cliente)

    # Associa conta ao cliente
    cliente.adicionar_conta(conta)
    contas.append(conta)

    print("✅ Conta criada com sucesso!")


def selecionar_conta(clientes):
    cpf = input("Informe o CPF do cliente: ")

    # Busca cliente
    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if not cliente:
        print("❌ Cliente não encontrado!")
        return None

    if not cliente.contas:
        print("❌ Cliente não possui conta!")
        return None

    # Retorna a primeira conta (simplificação do sistema)
    return cliente.contas[0]


def depositar(clientes):
    conta = selecionar_conta(clientes)
    if not conta:
        return

    valor = float(input("Valor do depósito: "))

    # Cria objeto de transação
    transacao = Deposito(valor)

    # Executa via cliente
    conta.cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    conta = selecionar_conta(clientes)
    if not conta:
        return

    valor = float(input("Valor do saque: "))
    transacao = Saque(valor)

    conta.cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    conta = selecionar_conta(clientes)
    if not conta:
        return

    print("\n📄 EXTRATO")

    # Lista todas as transações
    for t in conta.historico.transacoes:
        print(t)

    print(f"\n💰 Saldo: {conta.saldo}")


# =========================
# MENU PRINCIPAL
# =========================
def menu():
    clientes = []
    contas = []

    while True:
        # Interface simples via terminal
        print("""
1 - Criar cliente
2 - Criar conta
3 - Depositar
4 - Sacar
5 - Extrato
0 - Sair
""")

        opcao = input("Escolha: ")

        # Direciona para a função correta
        if opcao == "1":
            criar_cliente(clientes)

        elif opcao == "2":
            criar_conta(clientes, contas)

        elif opcao == "3":
            depositar(clientes)

        elif opcao == "4":
            sacar(clientes)

        elif opcao == "5":
            exibir_extrato(clientes)

        elif opcao == "0":
            print("👋 Saindo...")
            break

        else:
            print("❌ Opção inválida!")


# Ponto de entrada do sistema
if __name__ == "__main__":
    menu()