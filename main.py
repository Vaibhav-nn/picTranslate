from Textdetect import text_extractor
from Writer import writer
from Translator import translator
import argparse
from cv2 import cv2
from Inpainter import inpainter
from MaskGen import  mask_generator
from postprocess import postprocess

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='path to the image')
    parser.add_argument('--sl', type=str, help='source language')
    parser.add_argument('--tl', type=str, default= 'en', help='target language')
    parser.add_argument('--region',type=str, default= 'us-east-2', help= 'AWS region name')
    args = parser.parse_args()

    path=   args.path
    sl=     args.sl
    tl=     args.tl
    region= args.region

    mask_generator(path=path, region_name= region)

    inpainter()
    postprocess()
    
    bucket = ''
    document = ''
    block_count, text, coord= text_extractor(bucket,document, path, region_name= region)

    #Getting the translated text i.e. ttext
    ttext = translator(text, sl, tl, region_name= region) 

    #Opening the inpainted image
    image= cv2.imread('./results/image.jpg')

    #Writing the text on inpainted image
    written_img= writer(image, ttext, coord)

    #Output Image
    cv2.imwrite('./Output/Output.jpg', written_img)

    print("Blocks detected: " + str(block_count))
   
if __name__ == "__main__":
    main()