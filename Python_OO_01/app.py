#print('Hello world')

import os

restaurante = []

def exibir_nome_programa():

    print('𝐒𝐚𝐛𝐨𝐫 𝐄𝐱𝐩𝐫𝐞𝐬𝐬\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizar_app():
    os.system('cls')
    print('Encerrando o app\n')

def opcao_invalida():
    print('Opção inválida\n')
    input('Digite uma opção entre 1 e 4')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novo restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurante.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n ')
    input('Digite uma opção entre 1 e 4')
    main()


def escolher_opcao():
    try: 

        opcao_escolhida = int(input ('Escolha uma opção: '))
        #print(f'Você escolheu a opção {opcao_escolhida}')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurante')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()