#!/usr/bin/python3
import pyautogui
from random import randint
import time
import subprocess

prompt = pyautogui.confirm(text=f'What ore would you like to mine?', title='AutoMiner', buttons=['Necrite','Phasmatite','Gold','Rune','Light Animica','Dark Animica','Next','Exit'])
found=[]

if prompt == "Necrite":
    ore='nec.png'
elif prompt == "Phasmatite":
    ore='phas.png'
elif prompt == "Gold":
    ore='gold.png'
elif prompt == "Gems":
    ore='gemstone.png'
elif prompt == "Rune":
    ore='rune.png'
elif prompt == "Light Animica":
    ore='lanim.png'
elif prompt =="Dark Animica":
    ore='danima.png'
elif prompt == "Bane":
    ore='bane.png'
elif prompt == 'Next':
    prompt = pyautogui.confirm(text=f'What ore would you like to mine?', title='AutoMiner', buttons=['Luminite','Exit'])
    if prompt == 'Exit':
        exit()
    elif prompt == 'Luminite':
        ore='lum.png'
    pass
elif prompt == "Exit":
    exit()



def locate(object): # passes the .png file as an argument to shorten code
    global found
    found=None
    while found is None:
        found = pyautogui.locateOnScreen(object,confidence=.88) # can add a region where to search given x,y,width,height format x,y is the top left of the box to get the bottom righ of the box use formula x.left+x.width, x.top + x.height
    return found


def move(result):
    
    result_right = result.left + result.width - 10
    result_bottom = result.top + result.height - 10
    pyautogui.moveTo((randint(result.left,result_right),randint(result.top,result_bottom)),duration=1,tween=pyautogui.easeInBounce)
    

def move_rand(result):
    
    result_right = result.left + result.width # finds the right wall of the found object
    result_bottom = result.top + result.height # finds the bottom of the found object
    pyautogui.moveTo((randint(result.left + 100,result_right + 200),randint(result.top - 200,result_bottom - 100)),duration=1,tween=pyautogui.easeOutExpo)


def click():
    pyautogui.click()

try:
    while True:
        try:
            bot_timer = time.time()
            stam = None
            while stam != None:
                stam = pyautogui.locateAllOnScreen("stam.png",confidence=.95)
            while stam is None:
                locate(object=ore)
                move(result=found)
                click()
                move_rand(result=found)

            
        except KeyboardInterrupt:
            break
except KeyboardInterrupt:
    exit()
