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
        "categoria": None,
        "nivel": None,
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
        "categoria": None,
        "nivel": None,
        "amigos": ["isa123"],
        "favoritos": {"jogadoras": ["jogadora_paula"], "times": ["Flamengo"]}
    },
    "jogadora_paula": {
        "senha": "paula123",
        "tipo": "jogadora",
        "nivel": "profissional",
        "categoria": None,
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
        "categoria": None,
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
        "categoria": None,
        "nivel": None
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
    {"id": 1, "titulo": "Novo campeonato anunciado!", "conteudo": "O novo campeonato vai...", "data": "2025-09-01"},
    {"id": 2, "titulo": "Entrevista com jogadora X", "conteudo": "A jogadora X comentou...", "data": "2025-09-02"}
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
    {"id": 1, "nome": "Copa Feminina 2025", "times": [1, 2], "jogos": [2]}
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

def forca_opcao(msg, lista_opcoes, msg_erro='Erro'):
    opcoes = ', '.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n-> ")
    while escolha not in lista_opcoes:
        print(msg_erro)
        escolha = input(f"{msg}\n{opcoes}\n-> ")
    return escolha

# Função de cadastro de usuário

def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    username = input("Escolha um nome de usuário: ")

    # verifica se já existe
    if username in usuarios:
        print("Erro: nome de usuário já existe!")
        return

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
        "email": email
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