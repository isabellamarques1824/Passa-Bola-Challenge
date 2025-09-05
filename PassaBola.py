# =========================================
# Funções Básicas para validar dados inseridos pelos usuários
# =========================================

def verifica_numero(msg):
    """Solicita que o usuário digite um número e valida a entrada."""
    num = input(msg)
    while not num.isnumeric():
        print('Valor inválido. Tente novamente.')
        num = input(msg)
    return int(num)

def forca_opcao(msg, lista_opcoes, msg_erro='Erro'):
    """Força o usuário a escolher uma opção dentro da lista fornecida."""
    opcoes = ', '.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n-> ")
    while escolha not in lista_opcoes:
        print(msg_erro)
        escolha = input(f"{msg}\n{opcoes}\n-> ")
    return escolha

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
        "email": "isa@gmail.com",
        "categoria": None,
        "nivel": None,
        "amigos": [],
        "favoritos": {"jogadoras": [], "times": []}
    },
    "maria456": {
        "senha": "abcd",
        "tipo": "comum",
        "nome": "Maria",
        "sobrenome": "Silva",
        "email": "maria@gmail.com",
        "categoria": None,
        "nivel": None,
        "amigos": [],
        "favoritos": {"jogadoras": [], "times": []}
    },
    "jogadora_paula": {
        "senha": "paula123",
        "tipo": "jogadora",
        "nivel": "profissional",
        "categoria": None,
        "nome": "Paula",
        "sobrenome": "Alves",
        "email": "paula@gmail.com",
        "amigos": [],
        "favoritos": {"jogadoras": [], "times": []}
    },
    "jogadora_luiza": {
        "senha": "lu456",
        "tipo": "jogadora",
        "nivel": "profissional",
        "categoria": None,
        "nome": "Luiza",
        "sobrenome": "Carvalho",
        "email": "lu@gmail.com",
        "amigos": [],
        "favoritos": {"jogadoras": [], "times": []}
    },
    "jogadora_ana": {
        "senha": "ana123",
        "tipo": "jogadora",
        "nivel": "amador",
        "categoria": "Sub-17",
        "nome": "Ana",
        "sobrenome": "Santos",
        "email": "ana@gmail.com",
        "amigos": [],
        "favoritos": {"jogadoras": [], "times": []}
    },
    "jogadora_gi": {
        "senha": "gi123",
        "tipo": "jogadora",
        "nivel": "amador",
        "categoria": "Sub-20",
        "nome": "Giovana",
        "sobrenome": "Mendes",
        "email": "giovana@gmail.com",
        "amigos": [],
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


