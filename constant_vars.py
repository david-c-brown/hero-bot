import math
# import random
from windowcapture import WindowCapture

# Once wincap is called any resizing or movement of the window will be fucky


def get_real_x(ratio):
    return math.floor(wincap.offset_x + wincap.w * ratio)


def get_real_y(ratio):
    return math.floor(wincap.offset_y + wincap.h * ratio)
# wincap.start()


wincap = WindowCapture('Hero Siege')
region = (wincap.offset_x, wincap.offset_y, wincap.w, wincap.h-50)
# wp = waypoint
start_wp_center = {"x": get_real_x(.515), "y": get_real_y(.277)}
start_wp = {"x": get_real_x(.515), "y": get_real_y(.277),
            "r": 68, "g": 46, "b": 52}

# best farm locations
deep_space_wp = {"x": get_real_x(0.8625), "y": get_real_y(.20115)}
event_horizon_wp = {
    "x": get_real_x(.902), "y": get_real_y(.323), "r": 33, "g": 155, "b": 224}
fields_of_battle_wp = {"x": get_real_x(.187), "y": get_real_y(.58)}

pyramid_2_wp = {"x": math.floor(
    wincap.offset_x + wincap.w * .541), "y": get_real_y(.388)}

# mapping mm
minimap = {"top_left": {"x": get_real_x(.848), "y": get_real_y(.022)},
           "top_right": {"x": get_real_x(.997), "y": get_real_y(.022)},
           "bottom_left": {"x": get_real_x(.848), "y": get_real_y(.305)},
           "bottom_right": {"x": get_real_x(.997), "y":  get_real_y(.305)}}

minimap_width = minimap["top_right"]["x"] - minimap["top_left"]["x"]
minimap_height = minimap["bottom_left"]["y"] - minimap["top_left"]["y"]


player_dot = {"r": 199, "g": 179, "b": 119}
minimap_center = {"x": (minimap["top_left"]["x"] + minimap_width / 2),
                  "y": (minimap["top_left"]["y"] + minimap_height / 2)}

reset_coord = {"x":  math.floor(
    wincap.offset_x + wincap.w * .648), "y":  get_real_y(.12)}
top = {"x":  get_real_x(.507),
       "y":  get_real_y(.303)}
top_right = {"x":  get_real_x(.645),
             "y":  get_real_y(.407)}
right = {"x":  get_real_x(.726),
         "y":  get_real_y(.531)}
bottom_right = {"x":  math.floor(
    wincap.offset_x + wincap.w * .711), "y":  get_real_y(.908)}
bottom = {"x":  get_real_x(.652),
          "y":  get_real_y(.975)}
bottom_left = {"x":  math.floor(
    wincap.offset_x + wincap.w * .501), "y":  get_real_y(.963)}
left = {"x":  get_real_x(.309),
        "y":  get_real_y(.557)}
top_left = {"x":  get_real_x(.383),
            "y": get_real_y(.232)}
get_off_wp = {"x":  get_real_x(.519),
              "y":  get_real_y(.742)}

constant_vars = {
    "wincap": wincap,
    "region": region,
    "start_wp_center": start_wp_center,
    "start_wp": start_wp,
    "deep_space_wp": deep_space_wp,
    "event_horizon_wp": event_horizon_wp,
    "fields_of_battle_wp": fields_of_battle_wp,
    "pyramid_2_wp": pyramid_2_wp,
    "minimap": minimap,
    "minimap_width": minimap_width,
    "minimap_height": minimap_height,
    "player_dot": player_dot,
    "minimap_center": minimap_center,
    "reset_coord": reset_coord,
    "top": top,
    "top_right": top_right,
    "right": right,
    "bottom_right": bottom_right,
    "bottom": bottom,
    "bottom_left": bottom_left,
    "left": left,
    "top_left": top_left,
    "get_off_wp": get_off_wp
}
