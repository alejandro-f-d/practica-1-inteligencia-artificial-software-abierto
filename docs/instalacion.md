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
git clone git@github.com:alejandro-f-d/practica-1-inteligencia-artificial-software-abierto.git
cd practica-1-inteligencia-artificial-software-abierto
```
2. Creación de un entorno virtual (Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Configuración de las variables de entorno: (En la ruta: ./python-scripts/.env)
```env
INPUT_DIR=data/input
OUTPUT_DIR=data/output
CANTIDAD_PALABRAS=10
GROBID_API_URL=http://localhost:8070/api/processFulltextDocument
```
  Significado de las variables de entorno:
    INPUT_DIR: Directorio de entrada con los pdfs.
    OUTPUT_DIR: Directorio de salida con los resultados de los pdf. Este tiene presente los diferentes XML de los pdf. Las imagenes con lás gráficas que se han generado y un reporte en formato markdown con los enlaces de cada documento.
    CANTIDAD_PALABRAS: Cantidad de palabras a mostrar en la nube de palabras del abstract. Esta nube filtra las palabras/conectores más cómunes para evitar que salgan en el gráfico.
    GROBID_API_URL: Dirección URL del servicio de grobid al que se le van a realizar las peticiones. 
4. Ejecución de los scripts de python:
```bash
python python-scripts/main.py
```
Con esto, en la carpeta especificada de output tendremos los resultados.


# Guía de instalación del programa en entorno Docker:

## Requisitos previos:
Para la instalación del programa en este método se debe disponer de las siguientes herramientas en el sistema:
  - Docker Engine instalado en el sistema.

## Paso a paso:
Pasos a seguir para la ejecución: 
1. Clonar el repositorio:
```bash
git clone git@github.com:alejandro-f-d/practica-1-inteligencia-artificial-software-abierto.git
cd practica-1-inteligencia-artificial-software-abierto/docker/python_docker
```
2. Creación de la carpeta de input para el programa:
```bash
  mkdir input/
```
En esta carpeta deberás copiar o mover los papers a analizar.

3. Creación de las variables de entorno para la ejecución. En un fichero con nombre .env debes configurar:
```env
GROBID_EXTERNAL_PORT=8070
CANTIDAD_PALABRAS=30
```
La primera variable de entorno es el puerto de la máquina nativa donde escuchará grobid para peticiones. De esta manera tras la ejecución del programa, grobid seguirá corriendo y podrás utilizar grobid por tu cuenta desde ese puerto.
CANTIDAD_PALABRAS: Cantidad de palabras a mostrar en la nube de palabras del abstract. Esta nube filtra las palabras/conectores más cómunes para evitar que salgan en el gráfico.

4. Posteriormente desde la carpeta: `practica-1-inteligencia-artificial-software-abierto/docker/` podrás ejecutar el mandato: `docker compose up` y al terminar dejará los resultados en la carpeta `practica-1-inteligencia-artificial-software-abierto/docker/python_docker/output`. Este tiene presente los diferentes XML de los pdf. Las imagenes con lás gráficas que se han generado y un reporte en formato markdown con los enlaces de cada documento.

## Limpieza:
Para la limpieza del programa e imágenes docker puedes ejecutar: `docker compose down -v --rmi all`.

### Troubleshooting:

#### Error con healt_check:
En caso de tener el siguiente error:
```bash
  Container grobid_ia_1 Error dependency grobid failed to start
  dependency failed to start: container grobid_ia_1 is unhealthy
```
Debe modificar en el docker-compose.yml en `practica-1-inteligencia-artificial-software-abierto/docker` el start_period por un valor mayor en tiempo para permitir a grobid inicializarse de manera correcta. 






