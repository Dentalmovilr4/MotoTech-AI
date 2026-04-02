import os
import sys
from google import genai
from google.genai import types

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ Error: Configura 'GOOGLE_API_KEY'")
    sys.exit(1)

client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
Eres el experto multimodal de MotoTech-DMR4. 
- Si recibes una FOTO: Analiza piezas (bujías, sensores, desgaste de llantas, fugas de aceite).
- Si recibes un AUDIO: Escucha ruidos de motor (cascabeleo, válvulas sueltas, biela, cadena de distribución).
- Da un diagnóstico técnico basado en lo que ves o escuchas en la Pulsar NS200.
"""

def analizar_multimedia(ruta_archivo, tipo):
    print(f"🔄 Analizando {tipo} de la Pulsar...")
    
    # Abrimos el archivo (imagen o audio)
    with open(ruta_archivo, "rb") as f:
        archivo_data = f.read()

    # Determinamos el mime_type según la extensión
    mime_type = "image/jpeg" if tipo == "foto" else "audio/mp3"

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config={"system_instruction": SYSTEM_PROMPT},
        contents=[
            types.Part.from_bytes(data=archivo_data, mime_type=mime_type),
            "Basado en este archivo, dime qué falla ves o escuchas y cómo arreglarla."
        ]
    )
    print("\n🛠️ DIAGNÓSTICO MULTIMEDIA:")
    print(response.text)

def main():
    print("\n📸👂 BIENVENIDO A MOTOTECH SENSORIAL")
    opcion = input("¿Qué quieres analizar? (1: Texto, 2: Foto, 3: Audio): ")

    if opcion == "1":
        falla = input("Describe la falla: ")
        # ... (Tu código anterior de texto)
    elif opcion == "2":
        ruta = input("Ruta de la imagen (ej: bujia.jpg): ")
        analizar_multimedia(ruta, "foto")
    elif opcion == "3":
        ruta = input("Ruta del audio (ej: motor.mp3): ")
        analizar_multimedia(ruta, "audio")

if __name__ == "__main__":
    main()

