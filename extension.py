import platform
from pynput import keyboard
from pynput.mouse import Controller, Button
from os import system, environ
from subprocess import run

mouse = Controller()

home_directory = '{}\\AppData\\Roaming\\talon\\.venv\\Scripts\\repl.bat'.format(
    environ.get('USERPROFILE')) if platform.system() == 'Windows' else '~/.talon/bin/repl'


def run_talon_command(command: str, repl_home: str):
    if platform.system() == 'Windows':
        run(repl_home, text=True, input=command)

    if platform.system() == 'Linux':
        system('echo "{}"| {}'.format(command, home_directory))


def disable_microphone():
    print('Disabling microphone...')
    run_talon_command('from talon_plugins import speech; speech.actions.sound.set_microphone(name=\'None\');',
                      home_directory)


def toggle_eye_tracking():
    print('Toggling eye tracking...')
    run_talon_command('from talon_plugins import eye_mouse; eye_mouse.control_mouse.toggle();', home_directory)


def calibrate():
    print('Calibrating...')
    run_talon_command('from talon_plugins import eye_mouse; eye_mouse.calib_start()', home_directory)


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
