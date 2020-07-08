import boto3
import io
from PIL import Image
import base64

def text_extractor(bucket, document, path, region_name):

    client = boto3.client('textract', region_name= region_name)

    with open(path, 'rb') as ima:
        response = client.detect_document_text(Document={'Bytes': ima.read()})

        image= Image.open(ima).convert('RGB')
        blocks=response['Blocks']
        width, height =image.size 
        print ('Detected Document Text')

        #Getting the text and lower right coordinates of each LINE
        text= []
        coord= []
        for block in blocks:
            
            if block['BlockType']=='LINE':
                text.append(block['Text'])
                coord.append(((int(block['Geometry']['BoundingBox']['Left']*720)),
                int((block['Geometry']['BoundingBox']['Top']+block['Geometry']['BoundingBox']['Height'])*512)))
        
        print(text)

    return len(blocks), text, coord
