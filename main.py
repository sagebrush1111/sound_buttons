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
# Prod v3.2

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from gpiozero import Button
import pygame
pygame.mixer.init()

buf=[]
pinselect=[]

def play_sound(b):
    pygame.mixer.music.load("sound/"+sound_map[b])
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    
def record_button(b):
    buf.append(b);
    print("Pin selected: ", buttons[b]);
    play_sound(b);

b0 = Button(18)
b1 = Button(23)
b2 = Button(24)
b3 = Button(25)
b4 = Button(12)
b5 = Button(16)
b6 = Button(20)
b7 = Button(21)
bof = Button(4)
buttons = {b0:18,b1:23,b2:24,b3:25,b4:12,b5:16,b6:20,b7:21}
sound_map={b0:"b0.wav",b1:"b1.wav",b2:"b2.wav",b3:"b3.wav",b4:"b4.wav",b5:"b5.wav",b6:"b6.wav",b7:"b7.wav"}
for b in buttons:
    b.when_pressed=record_button
print("Sound Buttons Copyright (C) 2020 sagebrush1111\nThis program comes with ABSOLUTELY NO WARRANTY; for details, see the LICENSE file with the repo.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions; see the LICENSE file with repo for details.")
print("Select D4 to stop.")    
print("Recording will begin.")
while bof.value==0:
    continue
for o in buf:
    pinselect.append(buttons[o])    
print("Now playing sounds selected: ", pinselect)
for n in buf:
    play_sound(n)
        
