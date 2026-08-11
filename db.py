import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "PRUEBA01.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def crear_tabla():
    conn = get_connection()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS impuestos (
                sticker INTEGER PRIMARY KEY,
                fecha_movimiento DATE NOT NULL,
                fecha_recaudo DATE NOT NULL,
                tipo_horario TEXT,
                nro_id TEXT,
                nro_form TEXT,
                valor INTEGER
            )
        """)
        conn.commit()
    finally:
        conn.close()
