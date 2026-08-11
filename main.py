from consultas import (
    consulta_consolidada,
    consulta_por_fecha,
    consulta_por_sticker,
    exportar_a_xlsx,
)


def mostrar_tabla(registros):
    if not registros:
        print("No se encontraron registros.")
        return

    encabezados = [
        "Fecha de Movimiento",
        "Sticker",
        "Número de identificación",
        "Número de Formulario",
        "Valor",
    ]
    filas = [encabezados] + [list(registro) for registro in registros]
    anchos = [max(len(str(fila[i])) for fila in filas) for i in range(len(encabezados))]

    for fila in filas:
        print(" | ".join(str(valor).ljust(anchos[i]) for i, valor in enumerate(fila)))


def mostrar_consolidado(tipo_horario):
    cantidad, suma = consulta_consolidada(tipo_horario)
    print(f"\nConsolidado horario {tipo_horario}:")
    print(f"  Cantidad de registros: {cantidad}")
    print(f"  Suma de valores:       {suma}")


def consultar_por_fecha():
    fecha = input("\nIngrese la fecha (YYYY-MM-DD): ").strip()
    registros = consulta_por_fecha(fecha)
    print(f"\nRegistros para la fecha {fecha}:")
    mostrar_tabla(registros)


def consultar_por_sticker():
    sticker = input("\nIngrese el sticker: ").strip()
    try:
        sticker = int(sticker)
    except ValueError:
        print("El sticker debe ser un número entero.")
        return

    registro = consulta_por_sticker(sticker)
    if registro is None:
        print(f"No se encontró información para el sticker {sticker}.")
        return

    fecha_movimiento, tipo_horario, fecha_recaudo, nro_id, nro_form, valor = registro
    print(f"\nInformación del sticker {sticker}:")
    print(f"  Fecha de movimiento: {fecha_movimiento}")
    print(f"  Tipo de horario:     {tipo_horario}")
    print(f"  Fecha de recaudo:    {fecha_recaudo}")
    print(f"  Número de ID:        {nro_id}")
    print(f"  Número de formulario:{nro_form}")
    print(f"  Valor:               {valor}")


def exportar_reporte():
    fecha = input("\nIngrese la fecha para exportar (YYYY-MM-DD): ").strip()
    registros = consulta_por_fecha(fecha)

    if not registros:
        print(f"No hay registros para la fecha {fecha}.")
        return

    nombre_archivo = "reporte.xlsx"
    exportar_a_xlsx(registros, nombre_archivo)
    print(f"Reporte exportado a {nombre_archivo} ({len(registros)} registros).")


def mostrar_menu():
    print("\n=== Prueba Impuestos ===")
    print("1. Consultar por fecha")
    print("2. Consolidado horario N")
    print("3. Consolidado horario A")
    print("4. Consultar por sticker")
    print("5. Exportar consulta por fecha a reporte.xlsx")
    print("0. Salir")


def main():
    opciones = {
        "1": consultar_por_fecha,
        "2": lambda: mostrar_consolidado("N"),
        "3": lambda: mostrar_consolidado("A"),
        "4": consultar_por_sticker,
        "5": exportar_reporte,
    }

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "0":
            print("Hasta luego.")
            break

        accion = opciones.get(opcion)
        if accion is None:
            print("Opción no válida.")
            continue

        accion()


if __name__ == "__main__":
    main()
