import os
import time
import speech_recognition as sr
from gtts import gTTS 


import pyttsx3
import PyPDF2
import pikepdf

# Convert text to speech and save it as audiofile.
def speak(text):
    tts = gTTS(text = text, lang="en")
    filename = "audioFile.mp3"
    tts.save(filename)

# Decrypt the pdf and save it.
pdf = pikepdf.open('demo_story.pdf',password='')
pdf.save('demo_story_decrypted.pdf')

# Read every page and create a text file.
with open('demo_story_decrypted.pdf','rb') as pdf_file, open('sample.txt', 'w') as text_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    for page_number in range(number_of_pages):   # use xrange in Py2
        page = read_pdf.getPage(page_number)
        page_content = page.extractText()
        text_file.write(page_content)

# Read the text from the text file and save it in a variable.
with open('sample.txt', 'r') as file:
    text = file.read().replace('\n', '')

# Call text to speech.
speak(text)