from time import time
import asyncio
from num2words import num2words # this is for my cheeky moby dick quotes, specifically loop counter
import pyautogui as pg
import constant_vars as cvars
from random import uniform, sample, randint
from pydirectinput import press, click
from pynput.keyboard import Listener, KeyCode
from win32api import SetCursorPos, mouse_event
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_RIGHTUP
from os import _exit
from math import floor

# defining clicks for async operations. using pyautogui had some performance weirdness
async def left_click(x, y, hold_time = 0.1):
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    await asyncio.sleep(hold_time)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

async def right_click(x, y, hold_time = 0.1):
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0)
    await asyncio.sleep(hold_time)
    mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0)

async def click_click(x, y, hold_time):
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0)
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    press("f", presses = floor(hold_time+1), interval = floor(1/hold_time) )
    await asyncio.sleep(hold_time)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)
    mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0)

# here is how we control the character
# because the maps and monster groups are randomly generated, we go with a simple circular exploration

async def radial_movement(x,y, hold_time):
    await click_click(x, y, hold_time)
    press('f', interval = .5, presses = floor(hold_time*2))

async def widening_circle(number_of_seconds):
    t_end = time() + number_of_seconds
    iteration = 5
    while time() < t_end:
        duration = (number_of_seconds + iteration) / 8
        [await radial_movement(i["x"], i["y"], duration) for i in direction]
        iteration += 25
    return 0

# this function I'm not too sure on keeping. the original intent was to try and pick up any loot left behind, but i think there are probably better solutions
async def shrinking_circle(number_of_seconds):
    t_end = time() + number_of_seconds
    iteration = 1
    while time() < t_end:
        duration = (number_of_seconds + iteration) / 8
        [await radial_movement(i["x"], i["y"], duration) for i in reversed(direction)]
        iteration += 1
    return 0
    
# resets the seed
async def vote_reset():
    press("escape")
    await asyncio.sleep(0.8)
    await left_click(cvars.reset_coord["x"], cvars.reset_coord["y"])
    await left_click(cvars.reset_coord["x"], cvars.reset_coord["y"])
    await left_click(cvars.reset_coord["x"], cvars.reset_coord["y"])
    await asyncio.sleep(6)
    
# here are different common places to gain exp/gold. i've also introduced a random map.
async def fields_of_battle():
    press('d', interval = .2, presses = 2)
    press('f')
    print('i know not all that may be coming, but be it what it will, i will go to it laughing')
    await asyncio.sleep(3)

async def glacial_trail():
    press('d', interval = .2, presses = 11)
    press('f')
    print('i know not all that may be coming, but be it what it will, i will go to it laughing')
    await asyncio.sleep(3)    

async def event_horizon():
    press('a', interval = .2, presses = 9)
    press('f')
    print('i know not all that may be coming, but be it what it will, i will go to it laughing')
    await asyncio.sleep(3)
    
async def pyramid_2():
    press('d', interval= .2, presses = 17)
    print('i know not all that may be coming, but be it what it will, i will go to it laughing')
    await asyncio.sleep(3)
  
async def to_battle():
    g = randint(1,4)
    if g == 1:
        await fields_of_battle()
    if g == 2:
        await glacial_trail()
    if g == 3:
        await event_horizon()
    if g == 4:
        await pyramid_2()

# ctrl-C doesn't always like to work. probably asyncio's fault. here's how we quit
def on_press(key):
    quit_char = KeyCode.from_char('[')
    if key == quit_char:
        print('i turn my body from the sun. what [a] ho')


def on_release(key):
    quit_char = KeyCode.from_char('[')
    if key == quit_char:
        print('from hells heart I stab at thee')
        _exit(0)

async def main():
        i = 1
        flag = 0
        while 1:
            # for whatever reason, absolute reference seems to be required here
            waypoint = pg.locateCenterOnScreen(r'D:\hero-bot\assets\waypoint_b.png', grayscale=True,confidence = 0.4)
            end_time = time() + uniform(40, 50)
            if waypoint:
                flag = 0
                await right_click(waypoint[0], waypoint[1])
                print("squeeze! squeeze! squeeze! all the morning long; i squeezed that sperm till i myself almost melted into it")
                await asyncio.sleep(1.9)
                press("f")
                await asyncio.sleep(0.5)
                await fields_of_battle()
                # await to_battle()
                
                await right_click(get_off_wp['x'], get_off_wp['y'])
                await asyncio.sleep(0.5)
                i= i+1
                while time() < end_time:
                    await widening_circle(uniform(0,1))
                    await shrinking_circle(uniform(0,1))
                else:
                    await asyncio.sleep(0.6)
                    print(f'think not, is my {num2words(i-1, to = "ordinal")} commandment; and sleep when you can, is my {num2words(i, to = "ordinal")}')
                    await vote_reset()              
            else:
                flag +=1
                if flag >= 5:
                    press('[')
                print('i only am escaped alone to tell thee')
                await vote_reset()

# easy instant process kill
while 1:
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        asyncio.run(main())
        listener.join()

