from datetime import datetime
from pathlib import Path

from db import crear_tabla, get_connection

DATOS_PATH = Path(__file__).parent / "datos.txt"


def convertir_fecha(fecha_str):
    return datetime.strptime(fecha_str.strip(), "%Y%m%d").strftime("%Y-%m-%d")


def cargar_datos():
    crear_tabla()

    if not DATOS_PATH.exists():
        print(f"No se encontró el archivo {DATOS_PATH}")
        return

    conn = get_connection()
    insertados = 0
    omitidos = 0

    try:
        with open(DATOS_PATH, encoding="utf-8") as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                if not linea:
                    continue

                sticker = "desconocido"
                try:
                    campos = [campo.strip() for campo in linea.split(",")]
                    if len(campos) != 7:
                        raise ValueError(
                            f"se esperaban 7 campos, se encontraron {len(campos)}"
                        )

                    sticker, fecha_mov, fecha_recaudo, tipo_horario, nro_id, nro_form, valor = campos

                    cursor = conn.execute(
                        """
                        INSERT OR IGNORE INTO impuestos
                            (sticker, fecha_movimiento, fecha_recaudo, tipo_horario,nro_id, nro_form, valor)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            int(sticker),
                            convertir_fecha(fecha_mov),
                            convertir_fecha(fecha_recaudo),
                            tipo_horario,
                            nro_id,
                            nro_form,
                            int(valor),
                        ),
                    )
                    insertados += cursor.rowcount
                except Exception as error:
                    omitidos += 1
                    print(
                        f"Advertencia: línea {numero_linea}, sticker {sticker} - {error}"
                    )

        conn.commit()
        print("\nResumen de carga:")
        print(f"  Registros insertados: {insertados}")
        print(f"  Líneas omitidas por errores: {omitidos}")
    finally:
        conn.close()


if __name__ == "__main__":
    cargar_datos()
