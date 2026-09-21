import boto3

rekognition = boto3.client('rekognition', region_name='us-east-1')

# Lee una imagen local en formato de bytes
with open('2.png', 'rb') as image_file:
    image_bytes = image_file.read()

response = rekognition.detect_labels(
    Image={'Bytes': image_bytes},
    MaxLabels=5,
    MinConfidence=80
)

print("Etiquetas detectadas:")
for label in response['Labels']:
    print(f"- {label['Name']}: {label['Confidence']:.2f}% de confianza")