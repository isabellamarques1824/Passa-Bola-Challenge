from dados import *

"""
funcoes.py

Contém todas as funções do sistema PassaBola:
- Funções utilitárias (input, menus, listas)
- Funções de cadastro e login de usuários
- Funções de manipulação de jogos, campeonatos, notícias e times
- Menus para visitantes, usuários comuns, jogadoras e administradores

Este arquivo deve ser importado pelo main.py para execução do sistema.
"""

# =========================================
# 1. Funções helpers / utilitárias
# =========================================


# Essa função verifica se o valor digitado pelo usuário realmente é um número

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        print('Valor inválido. Tente novamente.')
        num = input(msg)
    return int(num)

# Essa função força o usuário a escolher uma opção dentro da lista fornecida.

def forca_opcao(msg, lista_opcoes, msg_erro='Digite uma opção válida.'):
    opcoes = ', '.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n-> ")
    while escolha not in lista_opcoes:
        print(msg_erro)
        escolha = input(f"{msg}\n{opcoes}\n-> ")
    return escolha

# Essa função pega o nome de um time pelo id

def pega_nome_time(id_time):
    for t in times:
        if t['id'] == id_time:
            return t['nome']
    return "Time desconhecido"

# Essa função printa a logo da Passa a bola

def logo():
    print("=======================================")
    print("         ⚽ PASSA A BOLA ⚽")
    print("           Futebol Feminino")
    print("=======================================")


#Essa função mostra listas/dicionários

def mostrar_lista(titulo, lista_itens):
    print(f"\n--- {titulo} ---")
    if len(lista_itens) == 0:
        print(f"Nenhum {titulo.lower()} encontrado.")
        return
    for i in range(len(lista_itens)):
        item = lista_itens[i]
        if type(item) == dict:
            print(str(i+1) + ".")
            for chave in item:
                print("   " + chave + ": " + str(item[chave]))
        else:
            print(str(i+1) + ". " + str(item))

# =========================================
# 2. Funções de usuário em geral
# =========================================


# Essa função cadastra novos usuários do sistema

def cadastrar_usuario():
    while True:
        print("\n--- Cadastro de Usuário ---")
        username = input("Escolha um nome de usuário: ")

        # verifica se já existe
        if username in usuarios:
            print("Erro: nome de usuário já existe!")
            continue

        novo_usuario_input = {
            "senha": "Digite a sua senha: ",
            "nome": "Digite o seu nome: ",
            "sobrenome": "Digite o seu sobrenome: ",
            "idade": "Digite a sua idade: ",
            "email": "Digite o seu email: ",
        }

        novo_usuario = {
            "amigos": [],
            "favoritos": {"jogadoras": [], "times": []}
        }

        for key in novo_usuario_input.keys():
            if key == "idade":
                dado = verifica_numero(novo_usuario_input[key])
                novo_usuario[key] = dado
            else:
                dado = input(novo_usuario_input[key])
                novo_usuario[key] = dado

        # tipo de usuário (comum ou jogadora ou admin)
        tipo = forca_opcao("Escolha o tipo de usuário:", ["comum", "jogadora", "administrador"])
        novo_usuario["tipo"] = tipo

        # Se for jogadora

        if tipo == "jogadora":

            rg = input("Digite o seu RG: ")

            # categoria automática pela idade
            idade = novo_usuario["idade"]
            if idade <= 15:
                categoria = "Sub-15"
            elif idade <= 17:
                categoria = "Sub-17"
            else:
                categoria = "Adulta"

            novo_usuario["rg"] = rg
            novo_usuario["categoria"] = categoria

        usuarios[username] = novo_usuario
        print(f"Usuário {username} cadastrado com sucesso!")
        break

# Essa função faz o login do usuário

def login_usuario():
    print("\n--- Login de Usuário ---")
    username_email = input("Digite o seu username ou o seu email: ")
    senha = input("Digite a sua senha: ")

    # Verificar login por username
    if username_email in usuarios:
        if usuarios[username_email]["senha"] == senha:
            print("✅ Login realizado com sucesso!")
            return usuarios[username_email]  # retorna o dict do usuário
        else:
            print("❌ Senha incorreta.")
            return None

    # Verificar login por email
    for user, dados in usuarios.items():
        if dados["email"] == username_email:
            if dados["senha"] == senha:
                print("✅ Login realizado com sucesso!")
                return dados  # retorna o dict do usuário
            else:
                print("❌ Senha incorreta.")
                return None

    # Se não achou nem username nem email
    print("❌ Usuário ou e-mail não encontrado.")
    return None


# Essa função permite que o usuário veja o seu perfil

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

        escolha = forca_opcao("\nAdicionar ou apagar(Amigos, Jogadoras, Times): ", ["Apagar", "Adicionar", "Voltar"] )
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

        elif escolha == "Apagar":
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
        else:
            break

# =========================================
# 3. Funções de manipulação de listas e dicionários
# =========================================


# Essa função apaga itens de listas e dicionários - modo ADM

def apagar_item(lista, tipo):
    if not lista:
        print(f"Nenhum {tipo} cadastrado.")
        return

    for item in lista:
        print(f"ID: {item['id']} | {item.get('titulo', item.get('nome', 'Sem nome'))}")

    try:
        id_item = verifica_numero(f"Digite o ID do {tipo} que deseja apagar: ")
        for i, item in enumerate(lista):
            if item["id"] == id_item:
                lista.pop(i)
                print(f"✅ {tipo.capitalize()} apagado com sucesso!")
                return
        print(f"⚠️ {tipo.capitalize()} não encontrado.")
    except ValueError:
        print("ID inválido.")


# Essa função apaga itens de listas e dicionários - modo usuário

def apagar_item_simples(lista, tipo):
    if not lista:
        print(f"Nenhum {tipo} encontrado.")
        return

    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")

    try:
        pos = verifica_numero(f"Digite o número do {tipo} que deseja apagar: ")
        if 1 <= pos <= len(lista):
            removido = lista.pop(pos - 1)
            print(f"✅ {tipo.capitalize()} '{removido}' apagado com sucesso!")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("ID inválido.")


# Essa função adiciona itens para listas e dicionários

def adicionar_item(usuario, lista_opcoes, chave, nome_lista):

    print(f"\n--- Adicionar {nome_lista} ---")
    mostrar_lista(f"Opções de {nome_lista}", lista_opcoes)

    escolha = input(f"Digite o nome do {nome_lista[:-1]} que deseja adicionar: ")

    # Verifica se existe na lista de opções
    if escolha not in lista_opcoes:
        print(f"❌ {nome_lista[:-1].capitalize()} não encontrado.")
        return

    # Navega pelo dicionário, criando subdicionários se necessário
    keys = chave.split(".")
    d = usuario
    for k in keys[:-1]:
        if k not in d or not isinstance(d[k], dict):
            d[k] = {}
        d = d[k]

    final_key = keys[-1]
    if final_key not in d or not isinstance(d[final_key], list):
        d[final_key] = []

    # Verifica duplicados
    if escolha in d[final_key]:
        print(f"⚠️ {nome_lista[:-1].capitalize()} já está na sua lista de {nome_lista}.")
        return

    # Adiciona
    d[final_key].append(escolha)
    print(f"✅ {nome_lista[:-1].capitalize()} adicionado com sucesso!")


# =========================================
# 4. Funções de jogos
# =========================================


# Essa função regista novos jogos

def registrar_jogo():
    print("\n--- Registrar Novo Jogo ---")

    tipo = forca_opcao("Escolha o tipo de jogo:", ["amador", "profissional"])

    quadra_id = verifica_numero("Digite o ID da quadra: ")

    id = verifica_numero("Digite o ID do jogo: ")
    data = input("Digite a data do jogo (DD-MM-AAAA): ")
    hora = input("Digite a hora do jogo (HH:MM): ")

    if tipo == "amador":
        categoria = input("Digite a categoria (ex: Sub-17, Adulta, etc): ")
        taxa = float(input("Digite a taxa de inscrição: "))
        novo_jogo = {
            "id": id,
            "tipo": "amador",
            "status": "agendado",
            "quadra": quadra_id,
            "data": data,
            "hora": hora,
            "categoria": categoria,
            "inscritas": [],
            "taxa": taxa,
            "resultado": None
        }
    else:  # profissional
        print("\nTimes disponíveis:")
        for t in times:
            print(f"{t['id']} - {t['nome']}")
        time1 = verifica_numero("Digite o ID do primeiro time: ")
        time2 = verifica_numero("Digite o ID do segundo time: ")

        campeonato_id = input("Digite o ID do campeonato (ou deixe vazio se não houver): ")
        campeonato_id = int(campeonato_id) if campeonato_id.strip() else None

        novo_jogo = {
            "id": id,
            "tipo": "profissional",
            "status": "agendado",
            "quadra": quadra_id,
            "data": data,
            "hora": hora,
            "times": [time1, time2],
            "campeonato": campeonato_id,
            "resultado": None
        }

    jogos.append(novo_jogo)
    print("✅ Jogo registrado com sucesso!")


# Essa função altera o status dos jogos

def alterar_status_jogo():
    if not jogos:
        print("Nenhum jogo cadastrado.")
        return

    for jogo in jogos:
        print(f"ID: {jogo['id']} | {jogo['data']} {jogo['hora']} - Status: {jogo['status']}")

    try:
        id_jogo = verifica_numero("Digite o ID do jogo que deseja alterar: ")
        for jogo in jogos:
            if jogo["id"] == id_jogo:
                novo_status = forca_opcao(
                    "Escolha o novo status: ",
                    ["agendado", "ao vivo", "encerrado"]
                )
                jogo["status"] = novo_status
                print("✅ Status alterado com sucesso!")
                return
        print("⚠️ Jogo não encontrado.")
    except ValueError:
        print("ID inválido.")


# Essa função printa os jogos de forma bonitinha

def listar_jogos():
    logo()
    print("\n--- Jogos ---")
    for jogo in jogos:
        if jogo['tipo'] == 'profissional':
            time1 = pega_nome_time(jogo['times'][0])
            time2 = pega_nome_time(jogo['times'][1])
            print(f"{jogo['data']} {jogo['hora']} - {time1} x {time2} | Status: {jogo['status']}")
        else:
            print(f"{jogo['data']} {jogo['hora']} - Jogo amador ({jogo['categoria']}) | Status: {jogo['status']}")


# =========================================
# 5. Funções de campeonatos
# =========================================

# Essa função registra novos campeonatos

def registrar_campeonato():
    print("\n--- Adicionar Campeonato ---")
    id = verifica_numero("Digite o ID do campeonato: ")
    nome = input("Digite o nome do campeonato: ")
    data = input("Digite a data do campeonato (AAAA): ")
    local = input("Digite o local do campeonato: ")

    campeonato = {
        "id": id,
        "nome": nome,
        "data": data,
        "local": local,
        "times": [],
        "fase": "agendado"
    }

    campeonatos.append(campeonato)
    print(f"✅ Campeonato '{nome}' adicionado com sucesso!")

# Essa função atualiza a fase de um campeonato

def atualizar_fase_campeonato():
    mostrar_lista("Campeonatos", campeonatos)
    try:
        id_camp = verifica_numero("\nDigite o ID do campeonato que deseja atualizar: ")
        campeonato = next((c for c in campeonatos if c['id'] == id_camp), None)

        if campeonato:
            nova_fase = forca_opcao("Selecione a nova fase: ", ["agendado", "quartas", "semifinal", "final", "encerrado"])
            campeonato['fase'] = nova_fase
            print(f"✅ Campeonato '{campeonato['nome']}' atualizado para fase: {nova_fase}")
        else:
            print("❌ Campeonato não encontrado.")
    except ValueError:
        print("❌ ID inválido.")


# =========================================
# 6. Funções de notícias
# =========================================

# Essa função registra novas notícias

def registrar_noticia():

    id = verifica_numero("Digite o ID da notícia: ")
    titulo = input("Digite o título da notícia: ")
    conteudo = input("Digite o conteúdo da notícia: ")
    data = input("Digite a data da notícia (DD-MM-AAAA): ")

    nova_noticia = {
        "id": id,
        "titulo": titulo,
        "conteudo": conteudo,
        "data": data
    }

    noticias.append(nova_noticia)
    print("✅ Notícia registrada com sucesso!")


# Essa função printa as notícias de forma bonitinha

def listar_noticias():
    logo()
    print("\n--- Notícias ---")
    for noticia in noticias:
        print(f"{noticia['data']} - {noticia['titulo']}")
        print(f"   {noticia['conteudo']}\n")


# =========================================
# 7. Funções de times
# =========================================

# Função para adicionar time

def adicionar_time():
    print("\n--- Adicionar Time ---")
    id =  verifica_numero("Digite o ID do time: ")
    nome = input("Nome do time: ")

    # verifica se já existe
    for t in times:
        if t["nome"].lower() == nome.lower():
            print("⚠️ Esse time já está cadastrado!")
            return

    tipo = forca_opcao("Tipo do time:", ["profissional", "amador"])

    novo_time = {
        "id": id,
        "nome": nome,
        "jogadoras": [],
        "tipo": tipo
    }
    times.append(novo_time)
    print(f"✅ Time '{nome}' adicionado com sucesso!")


# =========================================
# 8. Funções de jogadora
# =========================================

# Essa função gera o menu profissional para as jogadoras profissionais

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

# Essa função gera um formulário para as jogadoras se tornarem profissionais

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


# Essa função verifica se a jogadora é ou não profissional

def profissional(usuario):
    if usuario.get("nivel") == "profissional":
        menu_profissional(usuario,campeonatos)
    else:
        formulario_profissional(usuario)



# Essa função mostra os jogos em que a jogadora pode se inscrever

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



# Essa função mostra o calendario de jogos das jogadoras

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


# =========================================
# 9. Funções de menus
# =========================================


# menus de ADM

# Essa função mostra um menu de opções para o adm mexer com os dados dos times

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

# Essa função mostra um menu de opções para o adm mexer com os dados dos jogos

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

# Essa função mostra um menu de opções para o adm mexer com os dados dos campeonatos

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

# Essa função mostra um menu de opções para o adm mexer com os dados das notícias

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


# Menus principais

# Essa é a função que mostra o menu principal do ADM

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

# Essa função é do menu para usuários comuns

def menu_comum(usuario):
    while True:
        logo()
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

# Essa função é do menu para jogadoras

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

# Essa é a função principal - HOME

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


# Essa função é de um menu para usuários que não estão logados

def menu_visitante():
    while True:
        logo()
        escolha = forca_opcao(
            "\nEscolha uma opção: ",
            ["Ver notícias", "Calendário de jogos", "Criar conta", "Login", "Sair"]
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
                break
        elif escolha == "Login":
            usuario_logado = login_usuario()
            if usuario_logado:
                if usuario_logado['tipo'] == "administrador":
                    menu_admin(usuario_logado)
                    break
                else:
                    home(usuario_logado)
                    break
            else:
                print("Não foi possível realizar o login. Tente novamente ou cadastre-se.")
                break
        else:
            print("Saindo do modo visitante...")
            break
