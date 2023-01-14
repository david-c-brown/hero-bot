import math
# import random
from windowcapture import WindowCapture

# Once wincap is called any resizing or movement of the window will messup the bot
def get_real_x(ratio):
    return math.floor(wincap.offset_x + wincap.w * ratio)


def get_real_y(ratio):
    return math.floor(wincap.offset_y + wincap.h * ratio)

# our movement in game. it is set up to get wider and wider
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
# the way point occasionally messes with the bot. included as an explicit direction to solve
get_off_wp = {"x": center["x"], "y" : center["y"] - 70}


wincap = WindowCapture('Hero Siege')
region = (wincap.offset_x, wincap.offset_y, wincap.w, wincap.h-50)

constant_vars = {
    "wincap": wincap,
    "region": region,
    "top": top,
    "top_right": top_right,
    "right": right,
    "bottom_right": bottom_right,
    "bottom": bottom,
    "bottom_left": bottom_left,
    "left": left,
    "top_left": top_left,
    "direction": direction,
    "get_off_wp": get_off_wp
}
