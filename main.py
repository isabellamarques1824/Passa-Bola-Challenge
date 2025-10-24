from funcoes import *

"""
main.py

Ponto de entrada do sistema PassaBola.

Este arquivo é responsável por iniciar a execução do programa,
importando as funções (funcoes.py). 
A partir dele, o sistema exibe a tela inicial e direciona o 
usuário para o fluxo correto (visitante, comum, jogadora ou admin).
"""

# Carrega os dados do JSON
dados_carregados = carregar_dados()

# Dicionários (usuarios)
usuarios.clear()
usuarios.update(dados_carregados['usuarios'])

times.clear()
times.extend(dados_carregados['times'])
quadras.clear()
quadras.extend(dados_carregados['quadras'])
noticias.clear()
noticias.extend(dados_carregados['noticias'])
jogos.clear()
jogos.extend(dados_carregados['jogos'])
campeonatos.clear()
campeonatos.extend(dados_carregados['campeonatos'])

while True:
    logo()
    print("\nBem-vinda ao PassaBola! Aqui você acompanha tudo sobre futebol feminino.\n")
    escolha = forca_opcao("Escolha uma opção (digite a sua escolha): ", ["Login", "Cadastro", "Entrar como visitante", "Sair"])

    if escolha == "Login":
        usuario_logado = login_usuario()
        if usuario_logado:
            if usuario_logado['tipo']== "administrador":
                menu_admin(usuario_logado)
            else:
                home(usuario_logado)
        else:
            print("Não foi possível realizar o login. Tente novamente ou cadastre-se.")

    elif escolha == "Cadastro":
        cadastrar_usuario()
        usuario_logado = login_usuario()
        if usuario_logado:
            if usuario_logado['tipo']== "administrador":
                menu_admin(usuario_logado)
            else:
                home(usuario_logado)
    elif escolha == "Sair":
        break
    else:
        home()


