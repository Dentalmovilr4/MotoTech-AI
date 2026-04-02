import os
import sys
from google import genai

# Recuperar la clave desde GitHub Secrets
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: Configura 'GOOGLE_API_KEY' en los Secrets de tu Repo/Codespace.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
Eres el Asistente Técnico MotoTech-DMR4, experto en la Bajaj Pulsar NS200.
Tu base de conocimientos incluye:
- Sensor O2: 10-20 Ohms.
- Sensor EOT (Aceite): 2.45 kΩ a 20°C.
- Sensor TPS: 0.6V a 4.5V.
- Presión de llantas: 25 PSI (Del) / 28-32 PSI (Tras).
- Holgura de válvulas: Admisión 0.05mm / Escape 0.08mm.

Instrucciones:
1. Si el usuario da un código de error, explica qué sensor es.
2. Da pasos lógicos de diagnóstico.
3. Responde de forma técnica pero fácil de entender.
"""

def main():
    print("\n🏍️  BIENVENIDO A MOTOTECH-DMR4 AI")
    print("---------------------------------")
    pregunta = input("¿Qué falla presenta la Pulsar NS200?: ")

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            config={"system_instruction": SYSTEM_PROMPT},
            contents=pregunta,
        )
        print("\n🛠️ DIAGNÓSTICO SUGERIDO:")
        print(response.text)
    except Exception as e:
        print(f"❌ Error al conectar con Gemini: {e}")

if __name__ == "__main__":
    main()
