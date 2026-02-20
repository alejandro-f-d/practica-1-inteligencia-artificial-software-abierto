import os
from dotenv import load_dotenv
from src.api_client import send_to_grobid
from pathlib import Path
from src.run_cloud import run_cloud 

script_dir = Path(__file__).resolve().parent
env_path = script_dir.parent / '.env'
load_dotenv(dotenv_path=env_path)


raw_input = os.getenv("INPUT_DIR", "./data/input")
raw_output = os.getenv("OUTPUT_DIR", "./data/output")

INPUT_DIR = (script_dir / raw_input).resolve()
OUTPUT_DIR = (script_dir / raw_output).resolve()
CANTIDAD_PALABRAS = int(os.getenv("CANTIDAD_PALABRAS", 2))


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    if not os.path.exists(f"{OUTPUT_DIR}/images"):
        os.makedirs(f"{OUTPUT_DIR}/images")
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.pdf')]
    
    if not files:
        print(f"No hay PDFs en ese directorio. {INPUT_DIR}")
        return

    print(f"Se han encontrado: {len(files)} pdfs")

    for filename in files:
        pdf_path = os.path.join(INPUT_DIR, filename)
        print(f"Empezamos a procesar: {filename}")

        xml_data = send_to_grobid(pdf_path)

        if xml_data:
            xml_filename = filename.replace(".pdf", ".xml")
            save_path = os.path.join(OUTPUT_DIR, xml_filename)
            
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(xml_data)
            
            print(f"Salvado el XML en: {save_path}")
        else:
            print(f"Fallo al generar el XML de: {filename}")
    run_cloud(OUTPUT_DIR, f"{OUTPUT_DIR}/images", CANTIDAD_PALABRAS) 

if __name__ == "__main__":
    main()
