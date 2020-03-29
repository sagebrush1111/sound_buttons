# Audio play based on button input
# Released under GNU Public License v3
# Copyright 2020 sagebrush1111
# Absolutely No WARRANTY Expressed or Implied
# IOFaster Beta v1.3

from gpiozero import Button
import json
import pygame

buf=[]

def play_sound(i):
    pygame.mixer.init()
    if i==b0:
        pygame.mixer.music.load("b0.wav")
        pygame.mixer.music.play()
    elif i==b1:
        pygame.mixer.music.load("b1.wav")
        pygame.mixer.music.play()
    elif i==b2:
        pygame.mixer.music.load("b2.wav")
        pygame.mixer.music.play()
    elif i==b3:
        pygame.mixer.music.load("b3.wav")
        pygame.mixer.music.play()
    elif i==b4:
        pygame.mixer.music.load("b4.wav")
        pygame.mixer.music.play()
    elif i==b5:
        pygame.mixer.music.load("b5.wav")
        pygame.mixer.music.play()
    elif i==b6:
        pygame.mixer.music.load("b6.wav")
        pygame.mixer.music.play()
    elif i==b7:
        pygame.mixer.music.load("b7.wav")
        pygame.mixer.music.play()
    else:
        print("You fail!")
    while pygame.mixer.music.get_busy() == True:
        continue
    
def record_button(b):
    print(b)
    buf.append(b)
    
b0 = Button(18)
b1 = Button(23)
b2 = Button(24)
b3 = Button(25)
b4 = Button(12)
b5 = Button(16)
b6 = Button(20)
b7 = Button(21)
bof = Button(4)
buttons = {b0:1,b1:1,b2:1,b3:1,b4:1,b5:1,b6:1,b7:1}
for b in buttons:
    b.when_pressed=record_button
print("Select D4 to stop.")    
print("Recording will begin.")
with open('recording', 'r') as f:
    while bof.value==0:
        continue
    try:
        json.dump(buf,f)
    except:
        buf.append("I don't know that!")
        json.dump(buf, f)
buf.clear()
if not f.closed:
    raise Exception('Cross-dimensional power field detected in main reactor core!')
with open('recording','r') as fr:
    buf=json.load(fr)
if not fr.closed:
    raise Exception("Warning biological force detected in main cooling system!")
print(buf)
for n in buf:
    play_sound(n)
        
