import boto3
import io
from io import BytesIO
import sys
from cv2 import cv2 
import psutil
import time
import boto3 
import math
from PIL import Image, ImageDraw, ImageFont
import base64
import numpy as np

def mask_generator(path, region_name):

    bucket=''
    document=''
    client = boto3.client('textract', region_name= region_name)

    #call the stream values
    with open(path, 'rb') as ima:
        response = client.detect_document_text(Document={'Bytes': ima.read()})
        image= Image.open(ima).convert('RGB')
        mask= Image.open(ima).convert('RGB')
        pixels= image.load()
        pixels_msk= mask.load()

        #Get the text blocks
        blocks=response['Blocks']
        width, height =image.size  
        draw = ImageDraw.Draw(image)  
        print ('Detected Document Text')

        #Mask Creation
        for m in range(0,width):
            for n in range(0,height):
                pixels_msk[m,n]= (0,0,0)

        # Create image showing bounding box/polygon the detected lines/text
        for block in blocks:

                #To see the entire json output, uncomment this section
                '''
                print('Type: ' + block['BlockType'])
                if block['BlockType'] != 'PAGE':
                    print('Detected: ' + block['Text'])
                    print('Confidence: ' + "{:.2f}".format(block['Confidence']) + "%")

                print('Id: {}'.format(block['Id']))
                if 'Relationships' in block:
                    print('Relationships: {}'.format(block['Relationships']))
                print('Bounding Box: {}'.format(block['Geometry']['BoundingBox']))
                print('Polygon: {}'.format(block['Geometry']['Polygon']))
                print() '''

                draw=ImageDraw.Draw(image)
                        
                # Draw box around entire LINE  
                if block['BlockType'] == "LINE":
                    points=[]

                    for polygon in block['Geometry']['Polygon']:
                        points.append((width * polygon['X'], height * polygon['Y']))

                    #Getting coordinates to cut the text part    
                    minXL= min(points[0][0],points[3][0])
                    maxXR= max(points[1][0],points[2][0])
                    minYL= min(points[0][1], points[1][1])
                    maxYU= max(points[2][1], points[3][1])

                    #Putting white color inplace of text
                    for i in range(int(minXL), int(maxXR)):
                        for j in range(int(minYL), int(maxYU)):
                            pixels[i,j]= (255,255,255)
                            pixels_msk[i,j]= (255,255,255)

                    # Uncomment to draw bounding box
                    #box=block['Geometry']['BoundingBox']                    
                    #left = width * box['Left']
                    #top = height * box['Top']           
                    #draw.rectangle([left,top, left + (width * box['Width']), top +(height * box['Height'])],outline='black') 
        
        
        #Saving the mask and final cut image
        image=np.array(image)
        mask= np.array(mask)

        mask= cv2.resize(mask, (720,512), interpolation = cv2.INTER_AREA)     
        image= cv2.resize(image, (720,512), interpolation = cv2.INTER_AREA)
        cv2.imwrite('./Masks/mask.jpg', cv2.cvtColor(mask, cv2.COLOR_RGB2BGR))
        cv2.imwrite('./Images/image.jpg', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        print('Mask and Image are generated')
        print(len(blocks))
