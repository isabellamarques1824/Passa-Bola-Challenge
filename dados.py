"""
dados.py

Contém todas as estruturas de dados do sistema PassaBola:
- Usuários
- Jogos
- Campeonatos
- Times
- Notícias

Este arquivo centraliza os dicionários e listas que armazenam
as informações do sistema, sendo importado em funcoes.py.
"""

# =========================================
# Estruturas de dados do sistema
# =========================================

# Dicionário que armazena os dados dos usuários registrados do sistema Passa a Bola

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
        "posicao": "goleira",
        "experiencia": "não",
        "cidade": "São Paulo",
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
        "posicao": "atacante",
        "experiencia": "sim",
        "cidade": "São Paulo",
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

# Lista de dicionários que armazena os dados dos times registrados do sistema Passa a Bola

times = [
    {"id": 1, "nome": "Flamengo", "jogadoras": ["jogadora_paula"], "tipo": "profissional"},
    {"id": 2, "nome": "Fluminense", "jogadoras": ["jogadora_luiza"], "tipo": "profissional"}
]

# Lista de dicionários que armazena os dados das quadras que acontecem os jogos e campeonatos do sistema Passa a Bola

quadras = [
    {"id": 1, "nome": "Quadra Central", "local": "Rua A, nº 123"},
    {"id": 2, "nome": "Arena Zona Sul", "local": "Av. B, nº 456"}
]

# Lista de dicionários que armazena os dados das notícias do sistema Passa a Bola

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

# Lista de dicionários que armazena os dados dos jogos do sistema Passa a Bola

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

# Lista de dicionários que armazena os dados dos campeonatos do sistema Passa a Bola

campeonatos = [
    {
    "id": 1,
    "nome": "Copa feminina 2025",
    "data": 2025,
    "local": "Brasil",
    "times": [1,2],
    "fase": "agendado"}
]


