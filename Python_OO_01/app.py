#print('Hello world')

import os

restaurantes = [
    {'nome': 'Dapraça', 'categoria':'Japonesa', 'ativo': False},
    {'nome': 'Pizza', 'categoria':'Italiana', 'ativo': True},
    {'nome': 'Lanche Top', 'categoria':'Lanches', 'ativo': True}
]

def exibir_nome_programa():

    print('𝐒𝐚𝐛𝐨𝐫 𝐄𝐱𝐩𝐫𝐞𝐬𝐬\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizar_app():
    exibir_subtitulo('Encerrando o app')

def voltar_ao_menu_principal():
    input('Digite uma opção entre 1 e 4  \n')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()
  
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n ')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restauntes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'.{nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
        
    voltar_ao_menu_principal()


def escolher_opcao():
    try: 

        opcao_escolhida = int(input ('Escolha uma opção: '))
        #print(f'Você escolheu a opção {opcao_escolhida}')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
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