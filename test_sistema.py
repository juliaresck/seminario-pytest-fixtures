import sqlite3
import pytest
from sistema import UsuarioRepository


# ==============================================================================
# DEMONSTRAÇÃO 1: O ERRO (Cenário sem Fixture / Falha)
# ==============================================================================
def test_inserir_usuario_falha():
    conn = sqlite3.connect(":memory:")
    repo = UsuarioRepository(conn)
    # Tenta inserir sem ter rodado 'criar_tabela' antes
    repo.adicionar_usuario("Ana", "ana@email.com")


# ==============================================================================
# DEMONSTRAÇÃO 2: A SOLUÇÃO (Fixture com Setup e Teardown via yield)
# ==============================================================================
@pytest.fixture
def db_connection():
    # SETUP: Abre o banco em memória
    conn = sqlite3.connect(":memory:")
    yield conn
    # TEARDOWN: Fecha a conexão
    conn.close()


@pytest.fixture
def repo(db_connection):
    repository = UsuarioRepository(db_connection)
    repository.criar_tabela()
    return repository


def test_adicionar_e_buscar_usuario(repo):
    usuario_id = repo.adicionar_usuario("Carlos", "carlos@email.com")
    resultado = repo.buscar_por_id(usuario_id)

    assert resultado is not None
    assert resultado[1] == "Carlos"
    assert resultado[2] == "carlos@email.com"


def test_isolamento_de_dados(repo):
    resultado = repo.buscar_por_id(1)
    assert resultado is None