# =========================================
# Estruturas de dados do sistema
# =========================================

# Dicionário - Usuários

usuarios = {
    "isa123": {
        "senha": "1234",
        "tipo": "comum",
        "nome": "Isabella",
        "sobrenome": "Marques",
        "idade": 18,
        "email": "isa@gmail.com",
        "amigos": ["maria456"],
        "favoritos": {"jogadoras": ["jogadora_luiza"], "times": ["Flamengo"]}
    },
    "maria456": {
        "senha": "abcd",
        "tipo": "comum",
        "nome": "Maria",
        "sobrenome": "Silva",
        "idade": 20,
        "email": "maria@gmail.com",
        "amigos": ["isa123"],
        "favoritos": {"jogadoras": ["jogadora_paula"], "times": ["Flamengo"]}
    },
    "jogadora_paula": {
        "senha": "paula123",
        "tipo": "jogadora",
        "nivel": "profissional",
        "categoria": "Adulta",
        "nome": "Paula",
        "sobrenome": "Alves",
        "idade": 21,
        "email": "paula@gmail.com",
        "rg": "21785046",
        "amigos": ["jogadora_luiza","jogadora_ana","jogadora_gi"],
        "favoritos": {"jogadoras": [], "times": []}
    },
    "jogadora_luiza": {
        "senha": "lu456",
        "tipo": "jogadora",
        "nivel": "profissional",
        "categoria": "Adulta",
        "nome": "Luiza",
        "sobrenome": "Carvalho",
        "idade": 23,
        "email": "lu@gmail.com",
        "rg": "34567891",
        "amigos": ["jogadora_paula","jogadora_ana","jogadora_gi"],
        "favoritos": {"jogadoras": [], "times": []}
    },
    "jogadora_ana": {
        "senha": "ana123",
        "tipo": "jogadora",
        "nivel": "amador",
        "categoria": "Sub-17",
        "nome": "Ana",
        "sobrenome": "Santos",
        "idade": 17,
        "email": "ana@gmail.com",
        "rg": "93458651",
        "amigos": ["jogadora_luiza","jogadora_paula","jogadora_gi"],
        "favoritos": {"jogadoras": [], "times": []}
    },
    "jogadora_gi": {
        "senha": "gi123",
        "tipo": "jogadora",
        "nivel": "amador",
        "categoria": "Adulta",
        "nome": "Giovana",
        "sobrenome": "Mendes",
        "idade": 20,
        "email": "giovana@gmail.com",
        "rg": "43217690",
        "amigos": ["jogadora_luiza","jogadora_ana","jogadora_paula"],
        "favoritos": {"jogadoras": [], "times": []}
    },
    "admin01": {
        "senha": "admin123",
        "tipo": "administrador",
        "nome": "Administrador",
        "sobrenome": None,
        "email": "admin@gmail.com",
    }
}

# Lista de times
times = [
    {"id": 1, "nome": "Flamengo", "jogadoras": ["jogadora_paula"], "tipo": "profissional"},
    {"id": 2, "nome": "Fluminense", "jogadoras": ["jogadora_luiza"], "tipo": "profissional"}
]

# Quadras disponíveis
quadras = [
    {"id": 1, "nome": "Quadra Central", "local": "Rua A, nº 123"},
    {"id": 2, "nome": "Arena Zona Sul", "local": "Av. B, nº 456"}
]

# Notícias e artigos
noticias = [
    {
        "id": 1,
        "titulo": "Novo campeonato anunciado!",
        "conteudo": "A Confederação anunciou a realização da Copa Feminina 2025, \nque contará com times profissionais e amadores de todo o país. As inscrições começam na próxima semana e o \n torneio terá jogos espalhados por diversas quadras, prometendo movimentar o futebol feminino.",
        "data": "2025-09-01"
    },
    {
        "id": 2,
        "titulo": "Entrevista com jogadora X",
        "conteudo": "A jogadora Paula Alves, destaque do Flamengo, comentou sobre a\n importância do esporte feminino e como os campeonatos ajudam a revelar novos talentos. Ela também falou \nsobre sua preparação para os próximos jogos e deu dicas para jovens que querem se profissionalizar.",
        "data": "2025-09-02"
    }
]

# Jogos: amadores e profissionais
jogos = [
    {
        "id": 1,
        "tipo": "amador",
        "status": "agendado",
        "quadra": 1,
        "data": "2025-09-20",
        "hora": "18:00",
        "categoria": "Sub-17",
        "inscritas": ["jogadora_ana"],
        "taxa": 10.0,
        "resultado": None
    },
    {
        "id": 2,
        "tipo": "profissional",
        "status": "finalizado",
        "quadra": 2,
        "data": "2025-09-21",
        "hora": "20:00",
        "times": [1, 2],
        "campeonato": 1,
        "resultado": {"time1": 2, "time2": 1}
    }
]

# Campeonatos
campeonatos = [
    {
    "id": 1,
    "nome": "Copa feminina 2025",
    "data": 2025,
    "local": "Brasil",
    "times": [1,2],
    "fase": "agendado"}
]



# =========================================
# Funções do código
# =========================================


# Solicita que o usuário digite um número e valida a entrada.

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        print('Valor inválido. Tente novamente.')
        num = input(msg)
    return int(num)

# Força o usuário a escolher uma opção dentro da lista fornecida.

def forca_opcao(msg, lista_opcoes, msg_erro='Digite uma opção válida.'):
    opcoes = ', '.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n-> ")
    while escolha not in lista_opcoes:
        print(msg_erro)
        escolha = input(f"{msg}\n{opcoes}\n-> ")
    return escolha

# Função que pega o nome do time pelo id

def pega_nome_time(id_time):
    for t in times:
        if t['id'] == id_time:
            return t['nome']
    return "Time desconhecido"

# Função de cadastro de usuário

def cadastrar_usuario():
    while True:
        print("\n--- Cadastro de Usuário ---")
        username = input("Escolha um nome de usuário: ")

        # verifica se já existe
        if username in usuarios:
            print("Erro: nome de usuário já existe!")
            continue

        senha = input("Digite a senha: ")
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = verifica_numero("Digite a sua idade: ")
        email = input("Email: ")

        # tipo de usuário (comum ou jogadora ou admin)
        tipo = forca_opcao("Escolha o tipo de usuário:", ["comum", "jogadora", "administrador"])

        novo_usuario = {
            "senha": senha,
            "tipo": tipo,
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": idade,
            "email": email,
            "amigos": [],
            "favoritos": {"jogadoras": [], "times": []}
        }

        # Se for jogadora

        if tipo == "jogadora":

            rg = input("Digite o seu RG: ")

            # categoria automática pela idade
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

# Função que faz login

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

#logo passabola

def logo():
    print("=======================================")
    print("         ⚽ PASSABOLA ⚽")
    print("        Futebol Feminino")
    print("=======================================")

#função que mostra listas/ dicionários

def mostrar_lista(titulo, lista_itens):
    print(f"\n--- {titulo} ---")
    if len(lista_itens) == 0:
        print(f"Nenhum {titulo.lower()} encontrado.")
        return
    for i in range(len(lista_itens)):
        item = lista_itens[i]
        if type(item) == dict:  # se for um dicionário
            print(str(i+1) + ".")
            for chave in item:
                print("   " + chave + ": " + str(item[chave]))
        else:  # se for string ou outro tipo
            print(str(i+1) + ". " + str(item))

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

def listar_noticias():
    logo()
    print("\n--- Notícias ---")
    for noticia in noticias:
        print(f"{noticia['data']} - {noticia['titulo']}")
        print(f"   {noticia['conteudo']}\n")

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
    logo()
    print("--- Informações do Perfil ---")
    print(f"Nome: {usuario['nome']} {usuario.get('sobrenome', '')}")
    print(f"Idade: {usuario['idade']}")
    print(f"Email: {usuario['email']}")

    mostrar_lista("Amigos", usuario.get("amigos", []))
    mostrar_lista("Times Favoritos", usuario["favoritos"]["times"])
    mostrar_lista("Jogadoras Favoritas", usuario["favoritos"]["jogadoras"])

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


# Funções de menu
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
            print("aqui vai o profissional(n fiz ainda)")
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


