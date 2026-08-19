import sqlite3


class UsuarioRepository:
    def __init__(self, db_connection):
        self.conn = db_connection

    def criar_tabela(self):
        query = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """
        self.conn.cursor().execute(query)
        self.conn.commit()

    def adicionar_usuario(self, nome, email):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email)
        )
        self.conn.commit()
        return cursor.lastrowid

    def buscar_por_id(self, usuario_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, nome, email FROM usuarios WHERE id = ?", (usuario_id,)
        )
        return cursor.fetchone()
    