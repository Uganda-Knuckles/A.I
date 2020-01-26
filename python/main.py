#-*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr
import os

r = sr.Recognizer()

bot = Chatbot('A.I', read+_only=True)

bot.set_trainer(ListTrainer)

for _file in os.listdir('chat'):
  lines = open('chat+/' + _file, 'r').readlines()

bot.train(lines)
  

with sr.Microphone() as s:
  r.adjust_for_ambient_noise(s)
  
  while True:
    audio = r.listen(s)
    
    speech = r.recognize_google(audio, language='en')
    
    print('You spoke :', speech)
    
