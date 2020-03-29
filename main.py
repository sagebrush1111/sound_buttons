# Audio play based on button input
# Released under GNU Public License v3
# Copyright 2020 sagebrush1111
# Absolutely No WARRANTY Expressed or Implied
# Prod v1.0.1

import board
import digitalio
import json
import pygame

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
    
buf=[]
hold=8
b0 = digitalio.DigitalInOut(board.D18)
b1 = digitalio.DigitalInOut(board.D23)
b2 = digitalio.DigitalInOut(board.D24)
b3 = digitalio.DigitalInOut(board.D25)
b4 = digitalio.DigitalInOut(board.D21)
b5 = digitalio.DigitalInOut(board.D16)
b6 = digitalio.DigitalInOut(board.D20)
b7 = digitalio.DigitalInOut(board.D21)
bof = digitalio.DigitalInOut(board.D4)
bnx = digitalio.DigitalInOut(board.D17)
buttons = {b0:1,b1:1,b2:1,b3:1,b4:1,b5:1,b6:1,b7:1,bof:1,bnx:1}
for b in buttons:
    b.direction = digitalio.Direction.INPUT
    b.pull=digitalio.Pull.UP
with open('recording','w') as f:
    print("Select D4 to stop.")    
    print("Recording will begin.")
    print("After each selection, please select D17 to continue.")
    while bof.value==1:
        try:
            for b in buttons:
                buttons[b]=b.value
            hold=list(buttons.values()).index(0)
            if hold>7:
                raise Exception('Non-musical button caught')
            buf.append(hold)
            print("Select D17 to continue")
            while bnx.value==1:
                continue
            print("Selection recorded")
        except:
            continue        
    json.dump(buf,f)
    buf.clear()
if not f.closed:
    print("Warning cross-dimensional power field detected in main core!")
    exit()
with open('recording','r') as fr:
    buf=json.load(fr)
if not fr.closed:
    print("Warning biological force detected in main cooling system!")
    exit()
print(buf)
for n in buf:
    play_sound(n)
        
