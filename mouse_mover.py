import pyautogui
import time
import random
import yaml

#       ==== CONFIG ====
with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.Loader)

WINDOW_SIZE     =   pyautogui.size()

RUN_LENGTH      =   cfg['run_length']
LEADING_SLEEP   =   cfg['leading_sleep']
MOV_DURATION    =   cfg['movement']['duration']
MOV_INTERVAL    =   cfg['movement']['interval_between']
PAUSE_FOR_USER  =   cfg['movement']['pause_on_mouse_move']

BASE_X          =   0     # cfg.base_coordinates.x
BASE_Y          =   0     # cfg.base_coordinates.y

START_TIME          =   time.time()
RUN_LENGTH_MINUTES  =   RUN_LENGTH * 60
#       ==== CONFIG ====


# Determine whether to continue with while loop
def should_continue():
    return RUN_LENGTH == -1 or (time.time() - START_TIME) < RUN_LENGTH_MINUTES


# Determine whether the script should move the mouse
def should_mouse_move(mouse_pos):
    return not PAUSE_FOR_USER or not is_mouse_currently_moving(mouse_pos)


# Detect whether the mouse is currently moving
def is_mouse_currently_moving(reference_pos):
    current_pos = pyautogui.position()
    return current_pos.x != reference_pos.x or current_pos.y != reference_pos.y


# Move the mouse to a random location on the screen
def move_mouse():
    x = random.randint(BASE_X, WINDOW_SIZE.width)
    y = random.randint(BASE_Y, WINDOW_SIZE.height)
    pyautogui.moveTo(x, y, duration=MOV_DURATION)


# Main
def main():
    current_pos = pyautogui.position()

    if LEADING_SLEEP == True:
        time.sleep(MOV_INTERVAL)

    while should_continue():
        if should_mouse_move(current_pos):
            move_mouse()

        current_pos = pyautogui.position()
        time.sleep(MOV_INTERVAL)


main()
