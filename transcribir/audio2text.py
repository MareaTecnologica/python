import os
from faster_whisper import WhisperModel
import ollama


def transcribir_audio(ruta_audio, modelo_whisper="base"):
    """
    Transcribe un archivo de audio local usando Faster-Whisper.
    Modelos disponibles: 'tiny', 'base', 'small', 'medium', 'large-v3'
    """
    if not os.path.exists(ruta_audio):
        print(f"❌ Error: El archivo '{ruta_audio}' no existe.")
        return None

    print(f"📦 Cargando modelo Whisper ({modelo_whisper})...")
    # Usa "cuda" si tienes tarjeta gráfica Nvidia compatible, de lo contrario "cpu"
    model = WhisperModel(modelo_whisper, device="auto", compute_type="int8")

    print(f"🎙️ Procesando audio: {ruta_audio}...")
    segments, info = model.transcribe(ruta_audio, beam_size=5)

    print(f"🌐 Idioma detectado: {info.language} (probabilidad: {info.language_probability:.2f})")

    texto_completo = []
    print("\n--- Transcripción en progreso ---")
    for segment in segments:
        # Imprime el texto conforme se va procesando
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s]: {segment.text}")
        texto_completo.append(segment.text)

    return " ".join(texto_completo)


def procesar_con_ollama(texto_transcrito, modelo_ollama="llama3.2"):
    """
    Envía el texto extraído a un modelo de Ollama para resumirlo o analizarlo.

    El Prompt se puede personalizar según la tarea que queramos realizar (resumen, análisis, etc.).
    """
    print(f"\n🤖 Enviando texto a Ollama ({modelo_ollama}) para resumir...")

    prompt = f"""Instrucción OBLIGATORIA: Responde ÚNICAMENTE en español. No uses inglés en ninguna parte del resumen.

    Tarea: Genera un resumen claro y estructurado del siguiente texto transcrito.

    Texto a resumir:
    {texto_transcrito}

    Recuerda: Escribe la respuesta totalmente en español."""

    try:
        response = ollama.generate(model=modelo_ollama, prompt=prompt)
        print("\n📝 Resumen de Ollama:")
        print(response['response'])
    except Exception as e:
        print(f"❌ Error al conectar con Ollama: {e}. ¿Está el servicio ejecutándose?")


if __name__ == "__main__":
    # ─── CONFIGURACIÓN ───
    ARCHIVO_AUDIO = "fileaudio.mp3"  # Cambiar esto por la ruta del archivo (.mp3, .wav, .m4a, etc.)
    MODELO_WHISPER = "base"  # 'tiny' (más rápido), 'base' (equilibrio), 'small' o 'medium' (más preciso)
    MODELO_OLLAMA = "llama3.2"  # El modelo que tengamos descargado en Ollama (ej. llama3, llama3.2, mistral, phi3)
    # ─────────────────────

    # 1. Extraer texto del audio
    texto_final = transcribir_audio(ARCHIVO_AUDIO, MODELO_WHISPER)

    # 2. Guardar el texto en un archivo local
    if texto_final:
        with open("transcripcion.txt", "w", encoding="utf-8") as f:
            f.write(texto_final)
        print("\n💾 Transcripción completa guardada en 'transcripcion.txt'")

        # 3. Opcional: Procesar con Ollama
        # Descomentar la siguiente línea si queremos que Ollama analice el texto
        procesar_con_ollama(texto_final, MODELO_OLLAMA)
