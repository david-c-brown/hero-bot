# this script is computationally expensive, so for the most part we are only importing what we need from each library
from time import time
import asyncio
from num2words import num2words
import pyautogui as pg
import constant_vars as cvars
from random import uniform, sample, randint
from pydirectinput import press, click
from pynput.keyboard import Listener, KeyCode
from win32api import SetCursorPos, mouse_event
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_RIGHTUP
from os import _exit
from math import floor

center = {"x":floor(cvars.wincap.offset_x + cvars.wincap.w * .5), "y":floor(cvars.wincap.offset_y + cvars.wincap.h*.5)}
iteration = 1
background_tasks = set()
top = {"x": center["x"], "y": center["y"] - 115 + iteration}
top_right = {"x": center["x"] + 115 + iteration, "y": center["y"] - 125 - iteration}
right = {"x": center["x"] + 125 + iteration, "y": center["y"]}
bottom_right = {"x": center["x"] + 135 + iteration, "y": center["y"] + 135 + iteration}
bottom = {"x": center["x"], "y": center["y"] + 145 + iteration}
bottom_left = {"x": center["x"] - 145 - iteration, "y": center["y"] + 155 + iteration}
left = {"x": center["x"] - 155 - iteration, "y": center["y"]}
top_left = {"x": center["x"] - 165 - iteration, "y": center["y"] - 165 - iteration}
direction = [top, top_right, right, bottom_right, bottom, bottom_left, left, top_left]

target = {"x": cvars.wincap.offset_x, "y": cvars.wincap.offset_y + 5}
get_off_wp = {"x": center["x"], "y" : center["y"] - 70}

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

async def shrinking_circle(number_of_seconds):
    t_end = time() + number_of_seconds
    iteration = 1
    while time() < t_end:
        duration = (number_of_seconds + iteration) / 8
        [await radial_movement(i["x"], i["y"], duration) for i in reversed(direction)]
        iteration += 1
    return 0
    

async def detect_and_attack(number_of_seconds):
    t_end = time() + number_of_seconds
    while time() > number_of_seconds:
        pic = pg.screenshot(region=cvars.region)
        width, height = pic.size
        await asyncio.sleep(0.5)
        for x in range(0, width, 3):
            for y in range(0, height, 3):
                r, g, b = pic.getpixel((x, y))
                if (b in range(0, 10)) and (r in range(200, 255)) and (g in range(0, 10)):
                    await left_click(x + target['x'], y + target['y'])
                    await right_click(x + target['x'], y + target['y'])
                    press('f')
                    print('call me ishmael')
                    await asyncio.sleep(0.22)
    return 0


async def vote_reset():
    press("escape")
    await asyncio.sleep(0.8)
    await left_click(cvars.reset_coord["x"], cvars.reset_coord["y"])
    await left_click(cvars.reset_coord["x"], cvars.reset_coord["y"])
    await left_click(cvars.reset_coord["x"], cvars.reset_coord["y"])
    await asyncio.sleep(6)
    
async def roam_then_attack_strategy():
    iteration = 1 
    attack_task = asyncio.create_task(detect_and_attack())
    background_tasks.add(attack_task)
    attack_task.add_done_callback(background_tasks.discard)
    await widening_circle(uniform(0,2)+ iteration)
    iteration += 1

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
            waypoint = pg.locateCenterOnScreen(r'D:\herobot\assets\waypoint_b.png', grayscale=True,confidence = 0.4)
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
                    detect_and_attack(5)
                    await asyncio.sleep(0.6)
                    print(f'think not, is my {num2words(i-1, to = "ordinal")} commandment; and sleep when you can, is my {num2words(i, to = "ordinal")}')
                    await vote_reset()              
            else:
                flag +=1
                if flag >= 5:
                    press('[')
                print('i only am escaped alone to tell thee')
                await vote_reset()

while 1:
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        asyncio.run(main())
        listener.join()

