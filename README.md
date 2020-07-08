# pickLang
Sometimes we need to translate the text written on the images while keeping the background same. This is generally the case when we are dealing with a foreign language based powerpoint
presentation or any image with foreign context.
pickLang is an AI based web app to translate the text from one language to other on your image while keeping the background of the image same as original. 
Most of the available apps show the translate text of the image in a separate window which degrades the experience and understanding of the user. In this app, the translated text is shown 
right on the original picture thus maintaining the originality. 

# Technical stuff of the project
In this project, I've leveraged advanced Computer Vision based **EdgeConnect Inpainting** method to regenrate the background of the image in order to maintain the overall meaning of 
the subject. **AWS Textract** is used for OCR and **AWS Translate** is used for Language Translation. **Streamlit** is used to deploy the project in form of webapp, working with which 
was really exciting.

# Dependencies
`requirements.txt` should be referred to but some packages that you might miss are:-
* Torch
* Tensorflow 1.12
* Streamlit 0.62

`corerequirements.txt` contains all the packages that were installed on my environment during development of the project.

# How to use the repo
After cloning the repo, download weight files from [here](https://drive.google.com/drive/folders/1cGwDaZqDcqYU7kDuEbMXa9TP3uDJRBR1) and place them in the `./psv` directory. These are the weights 
of pretrained model of EdgeConnect and are required while program performs inpainting. 

**You would require AWS credentials to run the program.** 

Once ready with credentials, type command **streamlit run app.py**  
pickLang will open in your browser!!
