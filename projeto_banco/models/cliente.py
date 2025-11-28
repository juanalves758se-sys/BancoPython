class Cliente:

    identificacao = 10

    def __init__(self, nome: str, idade: int, saldo: float) -> None:
        self.__identificador: int = Cliente.identificacao
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        Cliente.identificacao += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if not isinstance(saldo, (float, int)):
            raise TypeError('O saldo do cliente precisa ser numérico')
        if saldo <= 0:
            raise ValueError('O saldo precisa ser positivo')
        if saldo > 1000000:
            raise ValueError('O saldo excede o valor máximo')
        else:
            self.__saldo = saldo

    @property
    def identificador(self) -> int:
        return self.__identificador

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if len(nome) > 30:
            raise ValueError('Nome muito grande.')
        if not isinstance(nome, str):
            raise TypeError('O nome do cliente precisa ser textual')
        else:
            self.__nome = nome

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade: int) -> None:
        if not isinstance(idade, int):
            raise TypeError('A idade do cliente precisa ser um número inteiro')
        if idade > 110:
            raise ValueError('Idade com valor muito grande.')
        else:
            self.__idade = idade

    def __repr__(self) -> str:
        return f'{self.nome, self.idade, self.saldo}'
