from PIL import ImageGrab
from datetime import datetime
import keyboard
import time
from windowcapture import WindowCapture


wincap = WindowCapture('Hero Siege')
region = (wincap.offset_x, wincap.offset_y, wincap.w, wincap.h-50)
def ss:
    while 1:
        im = ImageGrab.grab(region)
        dt = datetime.now()
        fname = "pic_{}.{}.png".format(
            dt.strftime("%H%M_%S"), dt.microsecond // 100000)
        im.save('screenshots_for_training/' + fname, 'png')
        time.sleep(60)
