from projeto_banco.services.banco import Banco, Cliente

import unittest

class BancoTest(unittest.TestCase):

    def setUp(self):
        Cliente.identificacao = 10
        Banco.contas.clear()

        self.c1 = Cliente('Julian', 25, 500)
        self.c2 = Cliente('Juan', 35, 5600)
        self.c3 = Cliente('Barbára', 29, 870)

    def test_adicionar_cliente(self):
        with self.assertRaises(TypeError):
            Banco.adicionar_cliente(3)
        self.assertEqual(Banco.adicionar_cliente(self.c1),
                f'Cliente {self.c1.nome} adicionado com sucesso!')
        self.assertIn(self.c1.identificador, Banco.contas.keys())

    def test_listar_clientes(self):
        with self.assertRaises(ValueError):
            Banco.listar_clientes()
        Banco.adicionar_cliente(self.c1)
        self.assertEqual(Banco.listar_clientes(), {chave: cliente for chave, cliente in Banco.contas.items()})

    def test_saque(self):
        with self.assertRaises(ValueError):
            Banco.saque(self.c1, 600)
        with self.assertRaises(TypeError):
            Banco.saque('Teste', 300)
        with self.assertRaises(TypeError):
            Banco.saque(self.c1, 'True')
        self.assertEqual(Banco.saque(self.c1, 20), f'Seu saldo atual é: {self.c1.saldo} reais')
        self.assertEqual(self.c1.saldo, 480)

    def test_deposito(self):
        with self.assertRaises(TypeError):
            Banco.deposito(35, 10)
        with self.assertRaises(TypeError):
            Banco.deposito(self.c1, 'Olá')
        with self.assertRaises(ValueError):
            Banco.deposito(self.c1, 10000000000)
        with self.assertRaises(ValueError):
            Banco.deposito(self.c1, -50)
        self.assertEqual(Banco.deposito(self.c1, 500), f'Seu saldo atual é: {self.c1.saldo} reais')

    def test_transferencia(self):
        with self.assertRaises(TypeError):
            Banco.transferencia(self.c1, 54, 100)
        with self.assertRaises(TypeError):
            Banco.transferencia(32, 54, 100)
        with self.assertRaises(TypeError):
            Banco.transferencia(32, 54, 'cliente 3')
        with self.assertRaises(ValueError):
            Banco.transferencia(self.c1, self.c2, 10000000000)
        with self.assertRaises(ValueError):
            Banco.transferencia(self.c2, self.c1, 0)
        with self.assertRaises(ValueError):
            Banco.transferencia(self.c1, self.c2, 15000)
        self.assertEqual(Banco.transferencia(self.c1, self.c2, 50),
                         f'Saldo atual do(a) {self.c1.nome}: {self.c1.saldo} reais\n'
                                f'Saldo atual do(a) {self.c2.nome}: {self.c2.saldo} reais')
        self.assertEqual(self.c1.saldo, 450)
        self.assertEqual(self.c2.saldo, 5650)

    def test_consultar(self):
        Banco.adicionar_cliente(self.c1)
        with self.assertRaises(TypeError):
            Banco.consultar('10')
        with self.assertRaises(ValueError):
            Banco.consultar(33)
        self.assertEqual(Banco.consultar(10), Banco.contas[10])
        Banco.adicionar_cliente(self.c2)
        self.assertEqual(Banco.consultar(11), Banco.contas[11])

    def test_excluir_cliente(self):
        Banco.adicionar_cliente(self.c1)
        with self.assertRaises(TypeError):
            Banco.excluir_cliente('Número 9')
        with self.assertRaises(ValueError):
            Banco.excluir_cliente(33)
        self.assertEqual(Banco.excluir_cliente(10), f"Conta {self.c1} excluída com sucesso!")
        self.assertNotIn(self.c1, Banco.contas.values())

    def test_filtrar_clientes(self):
        Banco.adicionar_cliente(self.c1)
        Banco.adicionar_cliente(self.c2)
        Banco.adicionar_cliente(self.c3)
        with self.assertRaises(TypeError):
            Banco.filtrar_clientes('oi')
        with self.assertRaises(ValueError):
            Banco.filtrar_clientes(100000000000)
        with self.assertRaises(ValueError):
            Banco.filtrar_clientes(-100)
        with self.assertRaises(ValueError):
            Banco.filtrar_clientes(600000)
        Banco.adicionar_cliente(self.c1)
        Banco.adicionar_cliente(self.c3)
        self.assertEqual(Banco.filtrar_clientes(1000), {11: self.c2})

    def test_atualizar_clientes(self):
        Banco.adicionar_cliente(self.c1)
        with self.assertRaises(ValueError):
            Banco.atualizar_clientes(30, 'Juan', 10)
        with self.assertRaises(TypeError):
            Banco.atualizar_clientes('erro', 'Juan', 100)
        with self.assertRaises(ValueError):
            Banco.atualizar_clientes(10, 'Juan', 300)
        self.assertEqual(Banco.atualizar_clientes(10, 'Diego', 33),
                         f'Nome alterado para - {self.c1.nome} e idade para - {self.c1.idade}')
        self.assertEqual(Banco.listar_clientes(), {10: self.c1})

if __name__ == '__main__':
    unittest.main()
