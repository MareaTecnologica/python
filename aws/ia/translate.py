import boto3

translate = boto3.client('translate', region_name='us-east-1')

texto_original = "Hello, world! Learning AWS with Python is amazing."

response = translate.translate_text(
    Text=texto_original,
    SourceLanguageCode='en',
    TargetLanguageCode='es'
)

print(f"Texto traducido: {response['TranslatedText']}")