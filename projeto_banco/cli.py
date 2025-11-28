from projeto_banco.services.banco import Banco, Cliente

id_clientes = {}

def interacao():
    while True:
        print('\n##ARÉA CLIENTE##\n')
        print('1 - Criar cliente.')
        print('2 - Acessar banco.')
        print('3 - Listar clientes.')
        print('4 - Excluir cliente.')
        print('5 - Sair do sistema.')
        try:
            opcoes = int(input('\nQuais das opções você deseja acessar?: '))
            if opcoes == 1:
                cliente()
            if opcoes == 2:
                banco()
            if opcoes == 3:
                listar_clientes()
            if opcoes == 4:
                excluir_cliente()
            if opcoes == 5:
                try:
                    sair = input('Deseja realmente sair do sistema? (S/N)'
                                 ' (QUALQUER CLIENTE NÃO SALVO NO BANCO DE DADOS NÃO SERÁ MAIS RECUPERADO: ').title()
                    if sair == 'N':
                        continue
                    if sair == 'S':
                        exit('Obrigado pela atenção!')
                except (ValueError, TypeError):
                    print('Digite um valor que seja correto para o sistema.')
            if opcoes > 5 or opcoes < 1:
                print('Opção não encontrada, tente novamente.')
                continue
        except (ValueError, TypeError):
            print('Digite um valor que seja correto para o sistema.')


def cliente():
    while True:
        try:
            nome = input('Digite o nome do cliente ou "sair" para voltar para a sessão anterior: ').title()
            if nome == "Sair":
                return
            idade = int(input('Digite a idade do cliente: '))
            saldo = float(input('Digite o saldo do cliente: '))
            novo_cliente = Cliente(nome, idade, saldo)
            id_clientes[novo_cliente.identificador] = novo_cliente
            print(f'Cliente criado com sucesso ({novo_cliente.nome}) ID - {novo_cliente.identificador}')
        except (ValueError, TypeError) as err:
            print(f'Ocorreu um erro: {err}')


def listar_clientes():
    if len(id_clientes) == 0:
        print('Nenhum cliente foi registrado.')
        return
    else:
        print({chave: cliente_info for chave, cliente_info in id_clientes.items()})
        return


def excluir_cliente():
    if len(id_clientes) == 0:
        print('Nenhum cliente foi registrado.')
    else:
        while True:
            try:
                chave = int(input('Digite o ID do cliente: '))
                if chave not in id_clientes.keys():
                    print('Nenhum cliente com esse ID foi encontrado.')
                    return
                else:
                    cliente_excluido = id_clientes.pop(chave)
                    print(f'CLIENTE EXCLUÍDO COM SUCESSO: {cliente_excluido}')
                    return
            except (ValueError, TypeError):
                print('Digite um valor que seja correto para o sistema.')


def banco():
    print('\n##BANCO##\n')
    print('1 - Listar clientes cadastrados no banco.')
    print('2 - Adicionar cliente.')
    print('3 - Sacar valor.')
    print('4 - Depositar valor.')
    print('5 - Transferir valor.')
    print('6 - Consultar cliente do banco.')
    print('7 - Excluir cliente do banco.')
    print('8 - Filtrar cliente do banco.')
    print('9 - Atualizar cliente do banco.')
    print('10 - Voltar para sessão anterior.')
    print('11 - Sair do sistema (ADICIONA TODOS OS CLIENTES QUE FORAM ADICIONADOS NO BANCO EM UM ARQUIVO CSV!).')

    opcoes = {
        1: Banco.listar_clientes,
        2: adicionar_banco,
        3: sacar_banco,
        4: depositar_banco,
        5: transferencia_banco,
        6: consultar_banco,
        7: excluir_banco,
        8: filtrar_banco,
        9: atualizar_banco,
        10: None,
        11: Banco.sair_sistema,
    }

    while True:
        try:
            escolha = int(input(': '))
            if escolha not in opcoes.keys():
                print('Opção não encontrada. Tente novamente.')
            else:
                if escolha == 11:
                    return
                else:
                    opcoes[escolha]()
        except (ValueError, TypeError) as err:
            print(f'Ocorreu um erro: {err}')


def adicionar_banco():
    if len(id_clientes) == 0:
        print('Nenhum cliente foi registrado.')
        return
    else:
        while True:
            try:
                print('Quem você deseja adicionar?')
                print(id_clientes)
                chave = int(input('Digite o ID do cliente: '))
                if chave not in id_clientes.keys():
                    print('Nenhum cliente com esse ID foi encontrado.')
                    return
                else:
                    print(Banco.adicionar_cliente(id_clientes[chave]))
                    return
            except (ValueError, TypeError) as err:
                print(f'Ocorreu um erro: {err}')


def sacar_banco():
    if len(Banco.contas) == 0:
        return print('Nenhum cliente foi registrado no banco.')
    else:
        while True:
            try:
                print(Banco.contas)
                chave = int(input('Quem você deseja que saque o dinheiro?: '))
                valor = float(input('Digite o valor do dinheiro: '))
                if chave not in Banco.contas.keys():
                    return print('Nenhum cliente do banco com esse ID foi encontrado.')
                else:
                    return print(Banco.saque(Banco.contas[chave], valor))
            except (ValueError, TypeError) as err:
                print(f'Ocorreu um erro: {err}')


def depositar_banco():
    if len(Banco.contas) == 0:
        print('Nenhum cliente foi registrado no banco.')
        return
    else:
        while True:
            try:
                print(Banco.contas)
                chave = int(input('Quem você deseja que saque o dinheiro?: '))
                valor = float(input('Digite o valor do depósito: '))
                if chave not in Banco.contas.keys():
                    print('Nenhum cliente com esse ID foi encontrado.')
                    return
                else:
                    print(Banco.deposito(Banco.contas[chave], valor))
                    return
            except (ValueError, TypeError) as err:
                print(f'Ocorreu um erro: {err}')


def transferencia_banco():
    if len(Banco.contas) == 0:
        print('Nenhum cliente foi registrado no banco.')
        return
    else:
        while True:
            try:
                print(Banco.contas)
                chave1 = int(input('Digite o ID do primeiro cliente: '))
                chave2 = int(input('Digite o ID do segundo cliente: '))
                valor = float(input('Digite o valor da transferência: '))
                if chave1 == chave2:
                    print('ERRO, TENTANDO FAZER TRANSFERÊNCIA PARA O PRÓPRIO CLIENTE!!!')
                    return
                if chave1 not in Banco.contas.keys():
                    print('Nenhum cliente com esse ID foi encontrado.')
                    return
                if chave2 not in Banco.contas.keys():
                    print('Nenhum cliente com esse ID foi encontrado.')
                    return
                else:
                    print(Banco.transferencia(Banco.contas[chave1], Banco.contas[chave2], valor))
            except (ValueError, TypeError) as err:
                print(f'Ocorreu um erro: {err}')


def consultar_banco():
    if len(Banco.contas) == 0:
        print('Nenhum cliente foi registrado no banco.')
        return
    else:
        while True:
            try:
                print(Banco.contas)
                chave = int(input('Digite o ID do cliente para consulta: '))
                if chave not in Banco.contas.keys():
                    print('Nenhum cliente com esse ID foi encontrado.')
                    return
                else:
                    print(Banco.consultar(chave))
                    return
            except (ValueError, TypeError) as err:
                print(f'Ocorreu um erro: {err}')


def excluir_banco():
    if len(Banco.contas) == 0:
        print('Nenhum cliente foi registrado no banco.')
        return
    else:
        while True:
            try:
                print(Banco.contas)
                chave = int(input('Digite o ID do cliente que deseja excluir: '))
                if chave not in Banco.contas.keys():
                    print('Nenhum cliente com esse ID foi encontrado.')
                    return
                else:
                    print(Banco.excluir_cliente(chave))
                    return
            except (ValueError, TypeError) as err:
                print(f'Ocorreu um erro: {err}')


def filtrar_banco():
    if len(Banco.contas) == 0:
        print('Nenhum cliente foi registrado no banco.')
        return
    else:
        while True:
            try:
                print(Banco.contas)
                chave = int(input('Digite o ID do cliente para que deseja filtrar: '))
                if chave not in Banco.contas.keys():
                    print('Nenhum cliente com esse ID foi encontrado.')
                    return
                else:
                    print(Banco.filtrar_clientes(chave))
                    return
            except (ValueError, TypeError) as err:
                print(f'Ocorreu um erro: {err}')


def atualizar_banco():
    if len(Banco.contas) == 0:
        print('Nenhum cliente foi registrado no banco.')
        return
    else:
        while True:
            try:
                print(Banco.contas)
                chave = int(input('Digite o ID do cliente para que deseja atualizar: '))
                nome = input('Digite o novo nome do cliente: ')
                idade = int(input('Digite a nova idade do cliente: '))
                if chave not in Banco.contas.keys():
                    print('Nenhum cliente com esse ID foi encontrado.')
                    return
                else:
                    print(Banco.atualizar_clientes(chave, nome, idade))
                    return
            except (ValueError, TypeError) as err:
                print(f'Ocorreu um erro: {err}')
