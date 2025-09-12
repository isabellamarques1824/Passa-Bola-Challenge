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
# 2. Funções de cadastro e login de usuário
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
