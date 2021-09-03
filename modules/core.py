import numpy as np
import pyautogui
import time
import Xlib.threaded
from PIL import ImageGrab
from pebble import concurrent
import jsonMaker
import config as cfg
import keyboard
from python_imagesearch.imagesearch import imagesearcharea
# https://stackoverflow.com/questions/54789250/q-terminate-a-process-called-in-a-function-from-another-function-in-python
# https://youtu.be/fKl2JW_qrso?t=583
# https://www.youtube.com/watch?v=CRJOQtaRT_8

# https://stackoverflow.com/questions/62111046/use-python-to-identify-elements-at-screen
# https://medium.com/@martin.lees/image-recognition-for-automation-with-python-711ac617b4e5


#     pyautogui.screenshot('chase.png', region=(1895, 190, 17, 17))


def doRandomPause(a, b):
    seconds = round(np.random.randint(a, b) / 1000, 2)
    time.sleep(seconds)


@concurrent.process(name='hunting')
def killandwalk():
    _arrayPos = 0
    while True:
        time.sleep(.3)
        # if R==0
        if  ImageGrab.grab().getpixel((cfg.battleListX, cfg.battleListY))[0] == 0 and  ImageGrab.grab().getpixel((cfg.monsterRedX, cfg.monsterRedY))[0] != 255:
            print('Attacking')          
            pyautogui.press(cfg.attackKey)
            time.sleep(2)
            if ImageGrab.grab().getpixel(cfg.looted)[0]  == 240 or ImageGrab.grab().getpixel(cfg.looted2)[0] == 240:
                    pyautogui.keyDown('shift')
                    pyautogui.click(221,241,button='right')
                    time.sleep(.1)
                    pyautogui.click(187,241,button='right')
                    time.sleep(.1)
                    pyautogui.click(190,213,button='right')
                    time.sleep(.1)
                    pyautogui.click(193,186,button='right')
                    time.sleep(.1)
                    pyautogui.click(221,196,button='right')
                    time.sleep(.1)
                    pyautogui.click(248,193,button='right')
                    time.sleep(.1)
                    pyautogui.click(253,215,button='right')
                    time.sleep(.1)
                    pyautogui.click(257,243,button='right')
                    time.sleep(.1)
                    pyautogui.moveTo(221,218)
                    time.sleep(.1)
                    pyautogui.keyUp('shift')
        elif ImageGrab.grab().getpixel((cfg.battleListX, cfg.battleListY))[0] != 0:
            # pos(x,y) must be around 1804,105 if so then char pyautogui.pixel(is in the middle of mark
            if _arrayPos < len(jsonMaker.json):
                print(f"Walking to {jsonMaker.json[_arrayPos]}")
                icon = pyautogui.locateCenterOnScreen(
                    jsonMaker.json[_arrayPos])
                # icon = imagesearcharea(jsonMaker.json[_arrayPos], 792, 6, 50, 50)
                pyautogui.click(icon)
                x, y = icon
                # if ImageGrab.grab().getpixel(cfg.looted)[0]==240:
                #     pyautogui.keyDown('shift')
                #     pyautogui.click(221,241,button='right')
                #     time.sleep(.1)
                #     pyautogui.click(187,241,button='right')
                #     time.sleep(.1)
                #     pyautogui.click(180,202,button='right')
                #     time.sleep(.1)
                #     pyautogui.click(193,160,button='right')
                #     time.sleep(.1)
                #     pyautogui.click(221,156,button='right')
                #     time.sleep(.1)
                #     pyautogui.click(250,156,button='right')
                #     time.sleep(.1)
                #     pyautogui.click(253,215,button='right')
                #     time.sleep(.1)
                #     pyautogui.click(257,243,button='right')
                #     time.sleep(.1)
                #     pyautogui.keyUp('shift')
                # pos(x,y) must be around 1804,105
                print(cfg.xPosBetween[0] > x > cfg.xPosBetween[1] and cfg.yPosBetween[0] > y > cfg.yPosBetween[1])
                if cfg.xPosBetween[0] < x < cfg.xPosBetween[1] and cfg.yPosBetween[0] < y < cfg.yPosBetween[1]:
                    _arrayPos += 1
            else:
                _arrayPos = 0

@concurrent.process(name='chase')
def chase():
    while True:

        """R==92 if chase is clcked."""
        if ImageGrab.grab().getpixel(cfg.chasePos)[0] != 92:
            pyautogui.click(cfg.chasePos)
            print('chase')
        time.sleep(10)


@concurrent.process(name='heal')
def heal():
    while True:
        # R==0 if heal is almost full
        if  ImageGrab.grab().getpixel((cfg.healXpos, cfg.healYpos))[0] != 0:
            keyboard.press(cfg.healingKey)
        print('chase')


# def stopProgram():
#     if keyboard.is_pressed('esc'):
#         sys.exit()

# def main():
#     time.sleep(5)
#     # with ProcessPool(max_workers=10) as pool:
#     #     # activateHunting(pool)
#     #     # activateChase(pool)
#     #     pass


# if __name__ == '__main__':
#     main()
#  if gw.isVisible('Tibia Tibia - Don Szpermix'):
# else:
#         print('Brak okna')