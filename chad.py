import speech_recognition as sr
import pyttsx3,serial
import os, requests
import wikipedia, wolframalpha
from urllib.request import urlopen
import json
from difflib import get_close_matches
import pygame
pygame.init()
# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
try:
    port = serial.Serial("COM3", 9600)  
except:
    try:
        port = serial.Serial('com4', 9600)
    except:
        try:
            port = serial.Serial('com6', 9600)
        except:
            print('body not connected') 
my_sound = pygame.mixer.Sound('rizz song.mp3')

# Define a function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
          # Adjust for background noise
        audio = recognizer.listen(source)
    
    try:
        query = recognizer.recognize_google(audio).lower()
        print("You:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
        return ""

# Define a function to respond to user input
def respond(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def load_database(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def find_answer(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.7)
    return matches[0] if matches else None

def get_answer(question: str, database: dict) -> str | None:
    for q in database["questions"]:
        if q["question"] == question:
            return q["answer"]

def chatbot():
    database: dict = load_database('database.json')

    ques = query

    best_match: str | None = find_answer(ques, [q["question"] for q in database["questions"]])
        
    if best_match:
        answer: str = get_answer(best_match, database)
        respond(f'{answer}')

    else:
        respond("I don't know the answer to that")


# Main loop
while True:
    query = listen()
    
    if "hello" in query:
        port.write(b'h')
        respond("Hello! How can I assist you?")

    elif 'hands up' in query:
        port.write(b'z')
        respond('sure')
        
        
    elif "bye" in query:
        port.write(b'g')
        respond("Goodbye!")

    elif "who are you" in query:
        my_sound.play()
        respond('my name is chad. but you can call me yours')
            
    elif 'search' in query:
            serch = query.replace('search', '')
            respond('Searching...')                
            try:
                try:
                    client = wolframalpha.Client('RQ6KH2-4R3U7WGKQE')
                    res = client.query(serch)
                    results = next(res.results).text
                    respond(results)
                except:
                    results = wikipedia.summary(serch, sentences=1)
                    port.write(b'e')
                    respond(results)
                    port.write(b't')
            except:
                
                respond('i am unable to search')
            
        
    #calculate is a non-common word. 'What' is a common word but it is used in other queries too
    elif 'calculate' in query:
        try:
            
            app_id = "RALRUL-54GQJU7LYK"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            respond("The answer is " + answer)
            
        except:
            
            respond('I didnt get that')

    elif 'weather' in query:
        wether = query.replace('weather', '')
        client = wolframalpha.Client('RQ6KH2-4R3U7WGKQE')
        res = client.query('weather' + wether)
        results = next(res.results).text
        port.write(b'e')
        respond(results)
        port.write(b't')
            
            

    
        
    else:
        port.write(b'e')
        chatbot()
        port.write(b't')
        
