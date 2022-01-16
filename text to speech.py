#text to speech converter.
from gtts import gTTS
import os
import PyPDF2
print("Enter your choice:")
print("1. Text")
print("2. Audio book / text file")
ch=int(input())
if(ch==1):
    txt=input("Enter the text : ")
    ln = 'en'
    e=gTTS(text=txt,lang = ln,slow = False)
    file_location=input("Enter the file location where you want to save the file : ")
    e.save(file_location)
    print("I am going to speak.....")
    os.system(file_location)
else:
    txt=input("Enter the filename : ")
    folder=input("Enter the folder destination : ")
    m=folder
    m+=txt
    p=m
    m+=".pdf"
    pageFileObj = open(m,'rb')
    pdfReader = PyPDF2.PdfFileReader(pageFileObj)
    t=pdfReader.getPage(0)
    q=t.extractText()
    e=gTTS(text=q,lang = 'en',slow = False)
    p=p+'welcome4.mp3'
    print("The file is ready to be read. Please plug into the headphones for better experience...")
    os.system(p)
    
    
    
    
