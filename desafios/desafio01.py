# Importa recursos importantes:
# ABC e abstractmethod -> para criar classes abstratas (contratos)
# datetime -> para registrar data e hora das transações
from abc import ABC, abstractmethod
from datetime import datetime


# =========================
# HISTÓRICO
# =========================
class Historico:
    def __init__(self):
        # Lista que armazena todas as transações realizadas na conta
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        # Adiciona uma transação ao histórico com:
        # tipo (Deposito ou Saque), valor e data atual
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,  # Nome da classe da transação
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


# =========================
# CONTA
# =========================
class Conta:
    def __init__(self, numero, cliente):
        # Inicializa uma conta com saldo zerado
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"  # Agência fixa (poderia ser dinâmica)
        self.cliente = cliente
        self.historico = Historico()  # Cada conta tem seu próprio histórico

    def saldo_atual(self):
        # Retorna o saldo atual da conta
        return self.saldo

    def sacar(self, valor):
        # Validação: não pode sacar mais do que tem
        if valor > self.saldo:
            print("❌ Saldo insuficiente")
            return False

        # Validação: valor precisa ser positivo
        if valor <= 0:
            print("❌ Valor inválido")
            return False

        # Realiza o saque
        self.saldo -= valor
        print("✅ Saque realizado")
        return True

    def depositar(self, valor):
        # Validação: valor precisa ser positivo
        if valor <= 0:
            print("❌ Valor inválido")
            return False

        # Realiza o depósito
        self.saldo += valor
        print("✅ Depósito realizado")
        return True


# =========================
# CONTA CORRENTE
# =========================
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # Herda tudo de Conta
        super().__init__(numero, cliente)
        
        # Define limite de crédito e quantidade máxima de saques
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
        # Delegação: quem executa a lógica da transação é o objeto Transacao
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        # Adiciona uma nova conta ao cliente
        self.contas.append(conta)


# =========================
# PESSOA FÍSICA
# =========================
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        # Reaproveita atributos do Cliente
        super().__init__(endereco)
        
        # Dados específicos de pessoa física
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# =========================
# INTERFACE TRANSAÇÃO
# =========================
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        # Toda transação deve ter um valor
        pass

    @abstractmethod
    def registrar(self, conta):
        # Toda transação deve saber como se aplicar a uma conta
        pass


# =========================
# DEPÓSITO
# =========================
class Deposito(Transacao):
    def __init__(self, valor):
        # Valor armazenado como atributo privado (_valor)
        self._valor = valor

    @property
    def valor(self):
        # Getter para acessar o valor do depósito
        return self._valor

    def registrar(self, conta):
        # Tenta depositar na conta
        if conta.depositar(self.valor):
            # Se der certo, registra no histórico
            conta.historico.adicionar_transacao(self)


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
        # Tenta realizar o saque
        if conta.sacar(self.valor):
            # Se der certo, salva no histórico
            conta.historico.adicionar_transacao(self)


# =========================
# TESTE DO SISTEMA
# =========================
if __name__ == "__main__":
    # Cria um cliente do tipo Pessoa Física
    cliente = PessoaFisica(
        nome="Ronaldo",
        cpf="12345678900",
        data_nascimento="01-01-2000",
        endereco="São Paulo"
    )

    # Cria uma conta corrente vinculada ao cliente
    conta = ContaCorrente(numero=1, cliente=cliente)

    # Associa a conta ao cliente
    cliente.adicionar_conta(conta)

    # Cria operações
    deposito = Deposito(1000)
    saque = Saque(200)

    # Executa as transações
    cliente.realizar_transacao(conta, deposito)
    cliente.realizar_transacao(conta, saque)

    # Exibe saldo final
    print("\n💰 Saldo final:", conta.saldo)

    # Exibe histórico de transações
    print("\n📄 Histórico:")
    for t in conta.historico.transacoes:
        print(t)