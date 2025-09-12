from funcoes import *
from dados import *

# =========================================
# Funções do código
# =========================================


def formulario_profissional(usuario):
    print("\n--- Formulário para se tornar profissional ---")
    print("Preencha as informações abaixo:")

    posicao = input("Qual sua posição em campo? ")
    experiencia = input("Tem experiência anterior em times? (sim/não) ")
    cidade = input("Cidade/Estado onde você joga: ")

    # Salva direto no dicionário do usuário
    usuario["posicao"] = posicao
    usuario["experiencia"] = experiencia
    usuario["cidade"] = cidade

    # Atualiza categoria para profissional
    usuario["nivel"] = "profissional"

    print("\n✅ Formulário enviado com sucesso!")
    print("Agora você é uma jogadora profissional!\n")


def menu_jogos():
    while True:
        escolha = forca_opcao(
            "\n--- Gestão de Jogos ---",
            ["Adicionar jogo", "Listar jogos", "Alterar status de jogo", "Apagar jogo", "Voltar"]
        )
        if escolha == "Adicionar jogo":
            registrar_jogo()
        elif escolha == "Listar jogos":
            mostrar_lista("Jogos", jogos)
        elif escolha == "Alterar status de jogo":
            alterar_status_jogo()
        elif escolha == "Apagar jogo":
            apagar_item(jogos, "jogo")
        elif escolha == "Voltar":
            break


#função que mostra os jogos em que a jogadora pode se inscrever

def proximos_encontros(usuario):
    print("\n--- Próximos Encontros ---\n")
    jogos_amadores = [j for j in jogos if j["tipo"] == "amador"]

    if not jogos_amadores:
        print("Nenhum jogo amador disponível para inscrição.")
        return

    # mostra lista
    i = 1
    for jogo in jogos_amadores:
        print(f"{i}. {jogo['data']} {jogo['hora']} - Jogo amador ({jogo['categoria']}) | Status: {jogo['status']}")
        i += 1

    opcao = verifica_numero("\nDigite o número do jogo para se inscrever (ou 0 para cancelar): ")

    if opcao == 0:
        return

    jogo_escolhido = jogos_amadores[opcao - 1]

    # descobrir username da jogadora logada
    username = None
    for user, dados in usuarios.items():
        if dados == usuario:
            username = user
            break

    # checar inscrição
    if username in jogo_escolhido["inscritas"]:
        print("⚠️ Você já está inscrita nesse jogo!")
    else:
        jogo_escolhido["inscritas"].append(username)
        print("✅ Inscrição realizada com sucesso!")

# função que mostra o calendario das jogadoras

def meu_calendario(usuario):
    print("\n--- Meu Calendário ---\n")

    # Descobrir o username pela referência no dicionário
    username = None
    for user, dados in usuarios.items():
        if dados == usuario:
            username = user
            break

    encontrou = False
    for jogo in jogos:
        if username in jogo.get("inscritas", []):
            encontrou = True
            if jogo["tipo"] == "profissional":
                time1 = pega_nome_time(jogo["times"][0])
                time2 = pega_nome_time(jogo["times"][1])
                print(f"{jogo['data']} {jogo['hora']} - {time1} x {time2} | Status: {jogo['status']}")
            else:
                print(f"{jogo['data']} {jogo['hora']} - Jogo amador ({jogo['categoria']}) | Status: {jogo['status']}")

    if not encontrou:
        print("📌 Você ainda não está inscrita em nenhum jogo.")

# ver perfil

def ver_perfil(usuario):
    while True:
        logo()
        print("--- Informações do Perfil ---")
        print(f"Nome: {usuario['nome']} {usuario.get('sobrenome', '')}")
        print(f"Idade: {usuario['idade']}")
        print(f"Email: {usuario['email']}")

        mostrar_lista("Amigos", usuario.get("amigos", []))
        mostrar_lista("Times Favoritos", usuario["favoritos"]["times"])
        mostrar_lista("Jogadoras Favoritas", usuario["favoritos"]["jogadoras"])

        escolha = forca_opcao("\nAdicionar ou apagar(Amigos, Jogadoras, Times): ", ["Apagar", "Adicionar"] )
        if escolha == "Adicionar":
            sub_escolha = forca_opcao("Escolha uma opção: ", ["Amigos", "Jogadoras favoritas", "Times favoritos", "Voltar"])
            if sub_escolha == "Amigos":
                adicionar_item(usuario, list(usuarios.keys()), "amigos", "amigos")
            elif sub_escolha == "Times favoritos":
                adicionar_item(usuario, [t["nome"] for t in times], "favoritos.times", "times favoritos")
            elif sub_escolha == "Jogadoras favoritas":
                adicionar_item(usuario, [u for u in usuarios if usuarios[u]["tipo"] == "jogadora"],"favoritos.jogadoras", "jogadoras favoritas")
            else:
                break

        else:
            if escolha == "Apagar":
                sub_escolha = forca_opcao("Escolha uma opção: ",["Amigos", "Jogadoras favoritas", "Times favoritos", "Voltar"])
                if sub_escolha == "Amigos":
                    apagar_item_simples(usuario["amigos"], "amigo")
                elif sub_escolha == "Jogadoras favoritas":
                    apagar_item_simples(usuario["favoritos"]["jogadoras"], "jogadora favorita")
                elif sub_escolha == "Times favoritos":
                    apagar_item_simples(usuario["favoritos"]["times"], "time favorito")
                elif sub_escolha == "Voltar":
                    break


# Funções de menu
def menu_profissional(usuario, campeonatos):
    print("\n===============================")
    print("      🌟 Área Profissional 🌟   ")
    print("===============================")

    # Campeonatos
    print("\n--- 🏆 Campeonatos Disponíveis ---")
    for camp in campeonatos:
        print(f"- {camp['nome']} | Data: {camp['data']} | Local: {camp['local']}")

    # Jogadoras em destaque
    print("\n--- ⭐ Jogadoras em Destaque ---")
    for username, dados in usuarios.items():
        if dados.get("categoria") == "profissional":
            print(f"- {dados['nome']} {dados['sobrenome']}")

    # Mural de oportunidades
    print("\n--- 📌 Mural de Oportunidades ---")
    print("Times estão procurando jogadoras para fortalecer suas equipes!\n")
    for time in times:
        print(f"🏟️ O time {time['nome']} está contratando jogadoras!")
        escolha = input(f"Deseja se inscrever para o {time['nome']}? (s/n) ")
        if escolha.lower() == "s":
            print("✅ Inscrição enviada! Seu perfil será avaliado.\n")
        else:
            print("⚠️ Você optou por não se inscrever.\n")

    print("===============================")

def profissional(usuario):
    if usuario.get("categoria") == "profissional":
        menu_profissional(usuario,campeonatos)
    else:
        formulario_profissional(usuario)

def menu_visitante():
    while True:
        escolha = forca_opcao(
            "\nEscolha uma opção: ",
            ["Ver notícias", "Calendário de jogos", "Criar conta", "Sair"]
        )
        if escolha == "Ver notícias":
            listar_noticias()
        elif escolha == "Calendário de jogos":
           listar_jogos()
        elif escolha == "Criar conta":
            cadastrar_usuario()
            usuario_logado = login_usuario()
            if usuario_logado:
                home(usuario_logado)
        elif escolha == "Sair":
            print("Saindo do modo visitante...")
            break

def menu_comum(usuario):
    while True:
        escolha = forca_opcao(
            f"\n{usuario['nome']}, escolha uma opção: ",
            ["Meu perfil", "Ver notícias", "Calendário de jogos", "Sair"]
        )
        if escolha == "Meu perfil":
            ver_perfil(usuario)
        elif escolha == "Ver notícias":
            listar_noticias()
        elif escolha == "Calendário de jogos":
            listar_jogos()
        elif escolha == "Sair":
            print("Logout realizado.")
            break


def menu_jogadora(usuario):
    while True:
        logo()
        escolha = forca_opcao(
            f"\n{usuario['nome']} (jogadora), escolha uma opção: ",
            ["Meu perfil", "Meu calendário", "Próximos encontros", "Profissional", "Sair"]
        )
        if escolha == "Meu perfil":
            ver_perfil(usuario)
        elif escolha == "Meu calendário":
            meu_calendario(usuario)
        elif escolha == "Próximos encontros":
            proximos_encontros(usuario)
        elif escolha == "Profissional":
            profissional(usuario)
        elif escolha == "Sair":
            print("Logout realizado.")
            break

# area ADM

def menu_times():
    while True:
        escolha = forca_opcao(
            "\n--- Gestão de Times ---",
            ["Adicionar time", "Listar times", "Apagar time", "Voltar"]
        )
        if escolha == "Adicionar time":
            adicionar_time()
        elif escolha == "Listar times":
            mostrar_lista("Times", times)
        elif escolha == "Apagar time":
            apagar_item(times, "time")
        elif escolha == "Voltar":
            break

def menu_noticias():
    while True:
        escolha = forca_opcao(
            "\n--- Gestão de Notícias ---",
            ["Adicionar notícia", "Listar notícias", "Apagar notícia", "Voltar"]
        )
        if escolha == "Adicionar notícia":
            registrar_noticia()
        elif escolha == "Listar notícias":
            mostrar_lista("Notícias", noticias)
        elif escolha == "Apagar notícia":
            apagar_item(noticias, "notícia")
        elif escolha == "Voltar":
            break


def menu_campeonatos():
    while True:
        escolha = forca_opcao("\n--- Gestão de Campeonatos ---",
                              ["Adicionar campeonato", "Listar campeonatos", "Atualizar fase", "Apagar campeonato",
                               "Voltar"])

        if escolha == "Adicionar campeonato":
            registrar_campeonato()
        elif escolha == "Listar campeonatos":
           mostrar_lista("Campeonatos", campeonatos)
        elif escolha == "Atualizar fase":
            atualizar_fase_campeonato()
        elif escolha == "Apagar campeonato":
            apagar_item(campeonatos, "campeonato")
        elif escolha == "Voltar":
            break


def menu_admin(usuario):
    while True:
        escolha = forca_opcao(
            "\n--- Menu do Administrador ---\nEscolha uma seção:",
            ["Times", "Notícias", "Campeonatos", "Jogos", "Sair"]
        )

        if escolha == "Times":
            menu_times()

        elif escolha == "Notícias":
            menu_noticias()

        elif escolha == "Campeonatos":
            menu_campeonatos()

        elif escolha == "Jogos":
            menu_jogos()

        elif escolha == "Sair":
            print("Saindo do menu administrador.")
            break

# função principal  - home

def home(usuario=None):
    logo()

    # Principais notícias

    print("\n--- Principais Notícias ---\n")
    for noticia in noticias[:2]:
        print(f"{noticia['data']}: {noticia['titulo']}")

    # Principais jogos

    print("\n--- Principais Jogos ---\n")
    for jogo in jogos[:2]:  # pega os dois primeiros jogos
        if jogo['tipo'] == 'profissional':
            time1 = pega_nome_time(jogo['times'][0])
            time2 = pega_nome_time(jogo['times'][1])
            print(f"{jogo['data']} {jogo['hora']} - {time1} x {time2} | Status: {jogo['status']}")
        else:
            print(f"{jogo['data']} {jogo['hora']} - Jogo amador ({jogo['categoria']}) | Status: {jogo['status']}")

    # Decide qual menu chamar
    if usuario is None:
        menu_visitante()
    elif usuario['tipo'] == "comum":
        menu_comum(usuario)
    elif usuario['tipo'] == "jogadora":
        menu_jogadora(usuario)

# =========================================
# Loop principal
# =========================================


while True:
    logo()
    print("\nBem-vinda ao PassaBola! Aqui você acompanha tudo sobre futebol feminino.\n")
    escolha = forca_opcao("Escolha uma opção (digite a sua escolha): ", ["Login", "Cadastro", "Entrar como visitante"])

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
    else:
        home()


