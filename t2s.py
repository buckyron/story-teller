import os
import time
import speech_recognition as sr
from gtts import gTTS 
import PyPDF2
import pikepdf
from transformers import pipeline

# Convert text to speech and save it as audiofile.
def speak(text):
    tts = gTTS(text = text, lang="en")
    filename = "audioFile.mp3"
    tts.save(filename)

# Generate story using GPT2 model.
story_gen = pipeline("text-generation", "pranavpsv/gpt2-genre-story-generator")
input_prompt = "<BOS> <horror> ~ In the middle of a "
story = story_gen(input_prompt, max_length=200, do_sample=True,
               repetition_penalty=1.1, temperature=1.2, 
               top_p=0.95, top_k=50)


# Convert the list of dictionaries into a string.
splitSroryString = story[0]["generated_text"].split('~')

# Story part of the string.
storyString = splitSroryString[1]

print(storyString)

# Generate the text file. 
with open('sample.txt', 'w') as text_file:
    text_file.write(str(storyString))


# # Decrypt the pdf and save it.
# pdf = pikepdf.open('demo_story.pdf',password='')
# pdf.save('demo_story_decrypted.pdf')

# # Read every page and create a text file.
# with open('demo_story_decrypted.pdf','rb') as pdf_file, open('sample.txt', 'w') as text_file:
#     read_pdf = PyPDF2.PdfFileReader(pdf_file)
#     number_of_pages = read_pdf.getNumPages()
#     for page_number in range(number_of_pages):   # use xrange in Py2
#         page = read_pdf.getPage(page_number)
#         page_content = page.extractText()
#         text_file.write(page_content)

# # Read the text from the text file and save it in a variable.
# with open('sample.txt', 'r') as file:
#     text = file.read().replace('\n', '')

# Call text to speech.
speak(storyString)