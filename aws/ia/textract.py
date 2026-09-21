import boto3

textract = boto3.client('textract', region_name='us-east-1')

# Lee un documento escaneado en formato de bytes
with open('2.png', 'rb') as document_file:
    document_bytes = document_file.read()

response = textract.detect_document_text(
    Document={'Bytes': document_bytes}
)

print("Texto extraído:")
for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print(block['Text'])