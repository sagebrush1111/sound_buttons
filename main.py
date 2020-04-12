# Audio play based on button input
# Copyright (C) 2020  sagebrush1111
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
# RC 4-2

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' #Needed to suppress welcome to pygame print
from gpiozero import Button #GPIO interaction library
import pygame                #Music playing library
import json                  #Storage system
pygame.mixer.init()

arerecord = bool()
buf=[]
pinselect=[]
b0 = Button(18)
b1 = Button(23)
b2 = Button(24)
b3 = Button(25)
b4 = Button(12)
b5 = Button(16)
b6 = Button(20)
b7 = Button(21)
bof = Button(4)
    
#The dictionaries below map each button object to the corresponding GPIO pin or sound file
#so the user knows what pin they hit and play the correct sound file
buttons = {b0:18,b1:23,b2:24,b3:25,b4:12,b5:16,b6:20,b7:21}
sound_mapb={b0:"b0.wav",b1:"b1.wav",b2:"b2.wav",b3:"b3.wav",b4:"b4.wav",b5:"b5.wav",b6:"b6.wav",b7:"b7.wav"}
sound_mapp={18:"b0.wav",23:"b1.wav",24:"b2.wav",25:"b3.wav",12:"b4.wav",16:"b5.wav",20:"b6.wav",21:"b7.wav"}
#play_sound function
#Plays music based on mutton input
#Takes button object argument
#Uses which button pressed to play corresponding sound
#Returns nothing to caller

def play_sound(b,which_dict):
    if which_dict=='b':
        pygame.mixer.music.load("sound/"+sound_mapb[b]) #Pulls in a dictionary to find the sound mapping to each button
    elif which_dict=='p':
        pygame.mixer.music.load("sound/"+sound_mapp[b]) #Pulls in a dictionary to find the sound mapping to each button
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
        
#record_button function
#Records which button was pressed
#Takes button object argument
#Records the button pressed, informed the user which one, and provides auditory feedback
#Returns nothing to caller

def record_button(b):
    if not arerecord:
        raise Exception("Invalid operation during a nonrecord mode. Exiting...")
    buf.append(b);
    print("Pin selected: ", buttons[b]);
    play_sound(b,'b');

#Record function
#Runs when the user wants to record music
#Takes no arguments
#Runs the recording and saving system
#Returns nothing to caller

def record():
    print("Select D4 to stop.")    
    print("Recording will begin.")
    while bof.value==0: #Loop until off pin activated to move to playback
        continue
    for o in buf:  #Creating human readable list of buttons pressed, so they know what is being played
        pinselect.append(buttons[o])
    with open("recording","w") as fw:
        json.dump(pinselect, fw)
    if not fw.closed:
        raise Exception("Warning biological force detected in main cooling system!")
    select=input("Do you want to (e)xit or (p)layback? (e)")
    if select=='p':
        playback()
        exit()
    else:
        exit()

#Playback function
#Runs when user wants to hear playback of melody they created
#Takes no arguments
#Runs the playback system
#Returns nothing to caller

def playback():
    with open("recording","r") as fr:
        buf=json.load(fr)
    if not fr.closed:
        raise Exception("Warning! Cross-dimensional power field detected in main reactor core!")
    print("Now playing sounds selected: ", buf)
    for n in buf:              #Play recorded melody back
        play_sound(n,'p')
    exit()

print("Sound Buttons Copyright (C) 2020 sagebrush1111\nThis program comes with ABSOLUTELY NO WARRANTY; for details, see the LICENSE file with the repo.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions; see the LICENSE file with repo for details.")
for b in buttons:
    b.when_pressed=record_button

while(1) { #Infinite while loop until exit
        select=input("Select option from (R)ecord, (P)layback, or (E)xit:(E)  ") #Option list to select record, play, or exit
if select=='R' or select=='r':
    arerecord=bool(1)
    record()
elif select=='P' or select =='p':
    playback()
else:
    exit()    
}
