import cv2
import numpy as np
import os
import google.cloud
from google.cloud import texttospeech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/amari/OneDrive/Documents/Data science projects/Prescription-Label-Reader/backend/centered-flow-407119-b4e5527bb781.json"

def preprocess_image(img):
    # Prepocessing image for better visibility
    gray = cv2.cvtColor(np.array(img), 
                        cv2.COLOR_BGR2GRAY)   
    resized = cv2.resize(gray, 
                         None, 
                         fx=2, 
                         fy=2, 
                         interpolation=cv2.INTER_LINEAR) 
    processed_img = cv2.adaptiveThreshold(resized, 
                                          255, 
                                          cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 
                                          61, 
                                          11) 
    return processed_img


def text2speech(message_text):
    #converting text me
    client = texttospeech.TextToSpeechClient()                                         #instantiate the client object
    synthesis_input = texttospeech.SynthesisInput(text = message_text)                  #set the input text to be synthesized
    voice = texttospeech.VoiceSelectionParams(language_code='en-US',                    #Build voice &
                                        name='en-US-wavenet-C',
                                        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)  #specify audio file type to return
    
    response = client.synthesize_speech(input=synthesis_input,                               #perform the text to speech request
                                 voice=voice,
                                 audio_config=audio_config)
    
    with open('output.mp3', 'wb') as out:                                                  #write the response to an output file
        out.write(response.audio_content)
    print('Audio content written to output file "output.mp3"')
    
    
    
    
    