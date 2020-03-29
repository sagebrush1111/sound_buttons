# Audio play based on button input
# Released under GNU Public License v3
# Copyright 2020 sagebrush1111
# Absolutely No WARRANTY Expressed or Implied
# IOFaster Beta v1.8

from gpiozero import Button
import json
import pygame

buf=[]

def play_sound(i):
    pygame.mixer.init()
    if i==0:
        pygame.mixer.music.load("b0.wav")
        pygame.mixer.music.play()
    elif i==1:
        pygame.mixer.music.load("b1.wav")
        pygame.mixer.music.play()
    elif i==2:
        pygame.mixer.music.load("b2.wav")
        pygame.mixer.music.play()
    elif i==3:
        pygame.mixer.music.load("b3.wav")
        pygame.mixer.music.play()
    elif i==4:
        pygame.mixer.music.load("b4.wav")
        pygame.mixer.music.play()
    elif i==5:
        pygame.mixer.music.load("b5.wav")
        pygame.mixer.music.play()
    elif i==6:
        pygame.mixer.music.load("b6.wav")
        pygame.mixer.music.play()
    elif i==7:
        pygame.mixer.music.load("b7.wav")
        pygame.mixer.music.play()
    else:
        print("You fail!")
    while pygame.mixer.music.get_busy() == True:
        continue
    
def record_button(b):
    if b.pin.number==18:
        buf.append(0)
    elif b.pin.number==23:
        buf.append(1)
    elif b.pin.number==24:
        buf.append(2)
    elif b.pin.number==25:
        buf.append(3)
    elif b.pin.number==12:
        buf.append(4)
    elif b.pin.number==16:
        buf.append(5)
    elif b.pin.number==20:
        buf.append(6)
    elif b.pin.number==21:
        buf.append(7)
    else:
        pass
b0 = Button(18)
b1 = Button(23)
b2 = Button(24)
b3 = Button(25)
b4 = Button(12)
b5 = Button(16)
b6 = Button(20)
b7 = Button(21)
bof = Button(4)
buttons = [b0,b1,b2,b3,b4,b5,b6,b7]
for b in buttons:
    b.when_pressed=record_button
print("Select D4 to stop.")    
print("Recording will begin.")
with open('recording', 'w') as f:
    while bof.value==0:
        continue
    try:
        json.dump(buf,f)
    except:
        buf.append(99)
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
        
