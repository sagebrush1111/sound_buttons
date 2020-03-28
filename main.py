# Audio play based on button input
# Released under GNU Public License v3
# Absolutely No WARRANTY
# Alpha 270320-14

import board
import digitalio
import json
import pygame

def play_sound(i):
    pygame.mixer.init()
    if i==0:
        pygame.mixer.music.load("b0.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif i==1:
        pygame.mixer.music.load("b1.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif i==2:
        pygame.mixer.music.load("b2.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif i==3:
        pygame.mixer.music.load("b3.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif i==4:
        pygame.mixer.music.load("b4.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif i==5:
        pygame.mixer.music.load("b5.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif i==6:
        pygame.mixer.music.load("b6.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif i==7:
        pygame.mixer.music.load("b7.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    else:
        print("You fail!")
    
buf=[]
b0 = digitalio.DigitalInOut(board.D18)
b1 = digitalio.DigitalInOut(board.D23)
b2 = digitalio.DigitalInOut(board.D24)
b3 = digitalio.DigitalInOut(board.D25)
b4 = digitalio.DigitalInOut(board.D21)
b5 = digitalio.DigitalInOut(board.D16)
b6 = digitalio.DigitalInOut(board.D20)
b7 = digitalio.DigitalInOut(board.D21)
bof = digitalio.DigitalInOut(board.D8) #Need to settle on gpio port
buttons = {b0:1,b1:1,b2:1,b3:1,b4:1,b5:1,b6:1,b7:1,bof:1}
for b in buttons:
    b.direction = digitalio.Direction.INPUT
    b.pull=digitalio.Pull.UP
while bof.value==1:
    pass
with open('recording','w') as f:
    print("Recording will begin")
    print("Press <insert pin> to stop")
    while bof.value==1:
        try:
            for b in buttons:
                buttons[b]=b.value
            buf.append(list(buttons.values()).index(0))
        except:
            print("All personal should leave now!")
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
        
