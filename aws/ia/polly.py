import boto3

polly = boto3.client('polly', region_name='us-east-1')

texto = "Hola, bienvenido al uso de servicios de inteligencia artificial de AWS con Python."

response = polly.synthesize_speech(
    Text=texto,
    OutputFormat='mp3',
    VoiceId='Mia',     # Voz en español (también disponible: 'Lupe', 'Mia', etc.)
    Engine='neural'      # Usa el motor neuronal para voz más natural
)

# Guarda el flujo de audio en un archivo MP3 local
if "AudioStream" in response:
    with open("audio_salida.mp3", "wb") as file:
        file.write(response["AudioStream"].read())
    print("Archivo 'audio_salida.mp3' generado con éxito.")