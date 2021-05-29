from pynput import keyboard
from pynput.mouse import Controller, Button
from os import system

mouse = Controller()


def disable_microphone():
    print('Disabling microphone...')
    system(
        'echo "from talon_plugins import speech; speech.microphone.manager.set_microphone(mic=None);"| ~/.talon/bin/repl')


def toggle_eye_tracking():
    print('Toggling eye tracking...')
    system('echo "from talon_plugins import eye_mouse; eye_mouse.control_mouse.toggle();"| ~/.talon/bin/repl')


def calibrate():
    print('Calibrating...')
    system('echo "from talon_plugins import eye_mouse; eye_mouse.calib_start()"| ~/.talon/bin/repl')


def left_click():
    print('left click')
    mouse.click(Button.left)


def right_click():
    print('right click')
    mouse.click(Button.right)


def scroll_up():
    print('scrolling up')
    mouse.scroll(0, 4)


def scroll_down():
    print('scrolling down')
    mouse.scroll(0, -4)


key_combinations = {'<ctrl>+<alt>+1': toggle_eye_tracking,
                    '<ctrl>+<alt>+2': calibrate,
                    '<ctrl>+<alt>+<page_up>': scroll_up,
                    '<ctrl>+<alt>+<page_down>': scroll_down
                    }

disable_microphone()

with keyboard.GlobalHotKeys(key_combinations) as hotkey:
    hotkey.join()
