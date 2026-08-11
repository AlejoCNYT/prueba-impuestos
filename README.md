# Prueba Impuestos

Aplicación de línea de comandos (CLI) desarrollada en Python para consultar, consolidar y exportar información de impuestos a partir de movimientos almacenados en una base de datos SQLite.

## Requisitos

- Python 3.
- `venv` para crear un entorno virtual aislado.
- La biblioteca `openpyxl` para generar archivos de Excel.

## Instalación

1. Clona el repositorio y entra en su directorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd prueba-impuestos
   ```

2. Crea un entorno virtual:

   ```bash
   python3 -m venv venv
   ```

3. Activa el entorno virtual:

   En Linux o macOS:

   ```bash
   source venv/bin/activate
   ```

   En Windows (PowerShell):

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. Instala la dependencia necesaria:

   ```bash
   pip install openpyxl
   ```

## Carga de datos

Ubica el archivo `datos.txt` en la raíz del proyecto. Cada línea debe contener siete campos separados por comas, en el siguiente orden:

```text
sticker,fecha_movimiento,fecha_recaudo,tipo_horario,nro_id,nro_form,valor
```

Las fechas deben estar en formato `YYYYMMDD`. Por ejemplo:

```text
ABC123,20240115,20240116,N,1001,FORM001,25000
```

Para cargar la información en la base de datos, ejecuta:

```bash
python3 cargar_datos.py
```

El script crea o utiliza la base de datos `PRUEBA01.db` y carga los registros de `datos.txt` en la tabla `impuestos`.

## Uso

Inicia la aplicación con:

```bash
python3 main.py
```

El menú principal ofrece las siguientes opciones:

1. **Consultar por fecha:** consulta los movimientos correspondientes a una fecha.
2. **Consolidado horario N:** genera el consolidado de los registros cuyo tipo de horario es `N`.
3. **Consolidado horario A:** genera el consolidado de los registros cuyo tipo de horario es `A`.
4. **Consultar por sticker:** busca la información asociada a un sticker específico.
5. **Exportar consulta por fecha a `reporte.xlsx`:** consulta los movimientos de una fecha y exporta el resultado a un archivo de Excel.
0. **Salir:** cierra la aplicación.

## Estructura del proyecto

```text
prueba-impuestos/
├── main.py             # Menú principal e interacción con el usuario.
├── consultas.py        # Consultas, consolidados y exportación a Excel.
├── db.py               # Conexión SQLite y creación de la tabla impuestos.
├── cargar_datos.py     # Carga datos.txt en la base de datos.
├── datos.txt           # Archivo de entrada con registros separados por comas.
├── PRUEBA01.db         # Base de datos SQLite generada por la aplicación.
├── reporte.xlsx        # Reporte Excel generado por una consulta por fecha.
└── README.md           # Documentación del proyecto.
```

### Componentes principales

- `main.py`: presenta el menú CLI y dirige cada opción seleccionada.
- `consultas.py`: contiene `consulta_por_fecha`, `consulta_consolidada`, `consulta_por_sticker` y `exportar_a_xlsx`; esta última utiliza `openpyxl`.
- `db.py`: administra la conexión con `PRUEBA01.db` y crea la tabla `impuestos` con las columnas `sticker`, `fecha_movimiento`, `fecha_recaudo`, `tipo_horario`, `nro_id`, `nro_form` y `valor`.
- `cargar_datos.py`: lee `datos.txt` y almacena sus siete campos en la base de datos.

### Captura menú

<img width="784" height="2265" alt="image" src="https://github.com/user-attachments/assets/271cdda0-cca7-46a2-870f-b08b543d6dd8" />

## Autor

Daniel
