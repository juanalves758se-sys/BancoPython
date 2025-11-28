from projeto_banco.models.cliente import Cliente
import csv


class Banco:

    contas = {}

    @classmethod
    def listar_clientes(cls) -> str | dict:
        """Retorna um dicionário com todos os clientes cadastrados no banco."""
        if len(cls.contas) == 0:
            raise ValueError('Nenhum cliente cadastrado no banco.')
        else:
            return {chave: cliente for chave, cliente in Banco.contas.items()}

    @staticmethod
    def adicionar_cliente(cliente: "Cliente") -> str:
        """Adiciona um cliente ao banco."""
        if not isinstance(cliente, Cliente):
            raise TypeError('Esse cliente não existe!')
        Banco.contas[cliente.identificador] = cliente
        return f'Cliente {cliente.nome} adicionado com sucesso!'

    @staticmethod
    def saque(cliente: "Cliente", valor: float | int) -> str:
        """Realiza um saque do saldo do cliente."""
        if not isinstance(cliente, Cliente):
            raise TypeError('Esse cliente não existe!')
        if not isinstance(valor, (float, int)):
            raise TypeError('Valor precisa ser do tipo numérico.')
        if valor > cliente.saldo:
            raise ValueError(f'Saldo insuficiente! Saldo do {cliente.nome} - {cliente.saldo} reais.')
        else:
            cliente.saldo -= valor
            return f'Seu saldo atual é: {cliente.saldo} reais'

    @staticmethod
    def deposito(cliente: "Cliente", deposito: float | int) -> str:
        """Deposita um valor no saldo do cliente."""
        if not isinstance(cliente, Cliente):
            raise TypeError('Esse cliente não existe!')
        if not isinstance(deposito, (float, int)):
            raise TypeError('Depósito precisa ser numérico.')
        if deposito > 1000000:
            raise ValueError('Depósito excedido pelo valor máximo (1.000.000)')
        if deposito <= 0:
            raise ValueError('Depósito precisa ser positivo.')
        else:
            cliente.saldo += deposito
            return f'Seu saldo atual é: {cliente.saldo} reais'

    @staticmethod
    def transferencia(conta1: "Cliente", conta2: "Cliente", valor: float | int) -> str:
        """Transfere um valor do saldo de um cliente para outro cliente."""
        if not isinstance(conta1, Cliente):
            raise TypeError('Esses clientes não existem!')
        if not isinstance(conta2, Cliente):
            raise TypeError('Esses clientes não existem!')
        if not isinstance(valor, (float, int)):
            raise TypeError('Valor precisa ser do tipo numérico')
        if valor > conta1.saldo:
            raise ValueError(f'Valor de transferência maior que o saldo de {conta1.nome} - {conta1.saldo} reais.')
        if valor > 1000000000:
            raise ValueError('Valor de transferência excedido pelo valor máximo (1.000.000)')
        if valor <= 0:
            raise ValueError('Valor de transferência precisa ser positivo')
        else:
            conta1.saldo -= valor
            conta2.saldo += valor
            return (f'Saldo atual do(a) {conta1.nome}: {conta1.saldo} reais\n'
                    f'Saldo atual do(a) {conta2.nome}: {conta2.saldo} reais')

    @classmethod
    def consultar(cls, identificador: int) -> tuple:
        """Consulta um cliente específico no banco com base pela chave."""
        if not isinstance(identificador, int):
            raise TypeError('Identificador precisa ser um número inteiro.')
        if identificador not in cls.contas.keys():
            raise ValueError('Conta não encontrada.')
        else:
            return cls.contas[identificador]

    @classmethod
    def excluir_cliente(cls, identificador: int) -> str:
        """Exclui um cliente do banco com base na chave."""
        if not isinstance(identificador, int):
            raise TypeError('Identificador precisa ser um número inteiro.')
        if identificador not in cls.contas.keys():
            raise ValueError('Conta não encontrada.')
        else:
            conta_removida = cls.contas.pop(identificador)
            f'É impossível cancelar exclusões de contas! E não é possível nem atualizá-las, então, tome cuidado.'
            return f'Conta {conta_removida} excluída com sucesso!'

    @classmethod
    def filtrar_clientes(cls, valor: int | float) -> dict | str:
        """Filtra um ou mais clientes no banco com base pelo valor.
        Ele retorna os clientes com saldo maior que o valor informado"""
        if not isinstance(valor, (int, float)):
            raise TypeError('O valor precisa ser numérico')
        if valor > 1000000000:
            raise ValueError('Valor excedeu o limite máximo (1.000.000)')
        if valor < 0:
            raise ValueError('Valor precisa ser positivo')
        else:
            clientes = dict(filter(lambda dicio: dicio[1].saldo > valor, cls.contas.items()))
            if len(clientes) == 0:
                raise ValueError('Nenhum cliente foi encontrado!')
            else:
                return clientes

    @classmethod
    def atualizar_clientes(cls, identificador: int, nome: str, idade: int) -> str:
        """Atualiza um cliente específico informado pela base. Atualiza nome e idade."""
        if not isinstance(identificador, int):
            raise TypeError('Identificador precisa ser do tipo inteiro.')
        if not isinstance(nome, str):
            raise TypeError('Nome precisa ser textual.')
        if not isinstance(idade, int):
            raise TypeError('Idade precisa ser um número inteiro.')
        if identificador not in cls.contas.keys():
            raise ValueError('Conta não encontrada.')
        if len(nome) > 30:
            raise ValueError('Nome muito grande.')
        if idade > 110:
            raise ValueError('Idade com valor muito grande.')
        else:
            f'Cliente: {cls.contas[identificador].nome} atualizado!\n'
            cls.contas[identificador].nome = nome
            cls.contas[identificador].idade = idade
            return (f'Nome alterado para - {cls.contas[identificador].nome} '
                    f'e idade para - {cls.contas[identificador].idade}')

    @classmethod
    def salvar_clientes(cls) -> None:
        """Essa função é chamada automaticamente ao sair do sistema. Ela salva os clientes em um arquivo CSV."""
        with open('clientes_do_banco.csv', 'a', encoding='utf-8', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(['Nome', 'Idade', 'Saldo'])
            for cliente in cls.contas.values():
                escritor.writerow([cliente.nome, cliente.idade, cliente.saldo])

    @staticmethod
    def sair_sistema():
        """Sai do programa e chama a função salvar_clientes."""
        if len(Banco.contas) == 0:
            raise ValueError('Impossível sair caso não tenha nenhum cliente '
                             'no banco (volte para sessão anterior para sair)')
        Banco.salvar_clientes()
        return exit('Até logo :)')
