# API de Tasas de Cambio

Este proyecto es una sencilla API construida con Flask que proporciona tasas de cambio y transacciones basadas en monedas y SKU. Permite obtener todas las tasas de cambio, una tasa específica por código de moneda, todas las transacciones para una moneda dada y todas las transacciones por SKU y código de moneda.

## Configuración

Para poner en marcha este proyecto en tu máquina local, sigue estos pasos:

1. **Clonar el repositorio:** Usa el comando `git clone [enlace-del-repositorio]` para clonar el repositorio a tu máquina local.
   
2. **Configurar un entorno virtual:** Es recomendable utilizar un entorno virtual para manejar las dependencias.
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # En Windows usa: myenv\Scripts\activate
    ```

3. **Instalar los requerimientos:** Si se especifican dependencias en un archivo `requirements.txt`, instálalas usando:
    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecutar la aplicación:** Puedes ejecutar la API con el siguiente comando:
    ```bash
    python app.py
    ```

## Pruebas

El proyecto viene con pruebas unitarias para asegurar su correcto funcionamiento.

Para ejecutar las pruebas:
```bash
python -m unittest test_app.py
