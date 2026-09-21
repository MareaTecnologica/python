import boto3

comprehend = boto3.client('comprehend', region_name='us-east-2')

texto = "¡Me encanta este servicio! Es extremadamente rápido y fácil de usar."

response = comprehend.detect_sentiment(
    Text=texto,
    LanguageCode='es'
)

print(f"Sentimiento predominante: {response['Sentiment']}")
print("Puntajes:", response['SentimentScore'])