# Guía de Instalación y ejecución en nativo:

Sigue estos pasos para configurar el entorno de desarrollo.

## Requisitos previos
* Python 3.10 o superior.
* Acceso a internet (para las APIs).

## Paso a paso
0. Ejecución de grobid de manera previa:
  ```bash
  docker run --rm --gpus all --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.2-full
  ```
1. Clona el repositorio:
   ```bash
   git clone [git@github.com:alejandro-f-d/practica-1-inteligencia-artificial-software-abierto.git](git@github.com:alejandro-f-d/practica-1-inteligencia-artificial-software-abierto.git)
   cd practica-1-inteligencia-artificial-software-abierto
   ```
2. Creación de un entorno virtual (Recomendado)
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. Configuración de las variables de entorno: (.env)
  ```env
  INPUT_DIR=data/input
  OUTPUT_DIR=data/output
  CANTIDAD_PALABRAS=10
  GROBID_API_URL=http://localhost:8070/api/processFulltextDocument
  ```
4. Ejecución de los scripts de python:
  ```bash
  python python-scripts/main.py
  ```
Con esto, en la carpeta especificada de output tendremos los resultados.

