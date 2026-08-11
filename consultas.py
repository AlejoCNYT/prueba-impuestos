(.venv) daniel@ASUS-DEV:~/prueba-impuestos$ cat consultas.py
from openpyxl import Workbook

from db import get_connection

ENCABEZADOS_CONSULTA_FECHA = [
    "Fecha de Movimiento",
    "Sticker",
    "Número de identificación",
    "Número de Formulario",
    "Valor",
]


def consulta_por_fecha(fecha):
    conn = get_connection()
    try:
        cursor = conn.execute(
            """
            SELECT fecha_movimiento, sticker, nro_id, nro_form, valor
            FROM impuestos
            WHERE fecha_movimiento = ?
            ORDER BY sticker
            """,
            (fecha,),
        )
        return cursor.fetchall()
    finally:
        conn.close()


def consulta_consolidada(tipo_horario):
    conn = get_connection()
    try:
        cursor = conn.execute(
            """
            SELECT COUNT(*), COALESCE(SUM(valor), 0)
            FROM impuestos
            WHERE tipo_horario = ?
            """,
            (tipo_horario,),
        )
        return cursor.fetchone()
    finally:
        conn.close()


def consulta_por_sticker(sticker):
    conn = get_connection()
    try:
        cursor = conn.execute(
            """
            SELECT fecha_movimiento, tipo_horario, fecha_recaudo, nro_id, nro_form, valor
            FROM impuestos
            WHERE sticker = ?
            """,
            (sticker,),
        )
        return cursor.fetchone()
    finally:
        conn.close()


def exportar_a_xlsx(datos, nombre_archivo):
    libro = Workbook()
    hoja = libro.active
    hoja.append(ENCABEZADOS_CONSULTA_FECHA)

    for fila in datos:
        hoja.append(list(fila))

    libro.save(nombre_archivo)
