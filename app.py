import streamlit as st
from PIL import Image
from Textdetect import text_extractor
from Writer import writer
from Translator import translator
from cv2 import cv2
from Inpainter import inpainter
from MaskGen import  mask_generator
from postprocess import postprocess
import time
import webbrowser

def main():
    st.title("picTranslate")
    '''Hii there! We are happy to help you. '''
    '''picTranslate is an AI based app that enables you to intuitively 
       translate the language of the text on your images, so that you can understand your picture completely.'''
    st.subheader('Instructions')
    '''1. Just select the image you want to change the text of.'''
    '''2. Select the source language i.e. the current language on the image.'''
    '''3. Select the target language i.e. the language you want the translated text to be in and Press Start.'''
    '''That's it!!'''
    st.header('Upload the required image')
    
    uploaded_file = st.file_uploader("")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image.save('Uploadedimg.jpg')
        st.image(image, caption='Uploaded Image.', use_column_width= True)
        st.success('Uploaded Successfully!!')

    sl = st.text_input("Source Language", 'en')
    tl= st.text_input("Target Language", 'en')
    if st.button('More Target Languages'):
        webbrowser.open_new_tab(url)
    region= st.text_input("AWS Region name", 'us-east-2')
    url = 'https://docs.aws.amazon.com/translate/latest/dg/what-is.html'

    if st.button('Start Translation'):
    
        path= './Uploadedimg.jpg'
        st.write("(1/4) Generating Mask...")   
        mask_generator(path, region_name= region)

        st.write("(2/4) Inpainting the image (This might take sometime if running on CPU)...")
        inpainter()
    
        postprocess()
        
        bucket = ''
        document = ''
        st.write('(3/4) Detecting text...')
        block_count, text, coord= text_extractor(bucket,document, path, region_name= region)

        #Getting the translated text i.e. ttext
        ttext = translator(text, sl, tl, region_name= region) 

        #Opening the inpainted image
        image= cv2.imread('./results/image.jpg')

        #Writing the text on inpainted image
        st.write("(4/4) Just there...")
        written_img= writer(image, ttext, coord)

        #Output Image
        cv2.imwrite('./Output/Output.jpg', written_img)

        st.success('Finished!!')
        image2 = Image.open('./Output/Output.jpg')
        st.image(image2, caption= 'Output image', use_column_width= True)
        st.warning('Very rich backgrounds might create problems!!')
        st.markdown("<h1 style='text-align: center; color: black; font-size:16px;'>Developed by Vaibhav Tiwari</h1>", unsafe_allow_html=True)

if __name__=='__main__':
    main()
