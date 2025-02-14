import time
import threading
from pynput.mouse import Button, Controller

# pynput.keyboard is used to watch events of keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode

# four variables to control the auto-clicker
delay = 0.5
#Button.right for right-click, but it's LMB for now
button = Button.left
start_stop_key = KeyCode(char='`')
stop_key = KeyCode(char='\')

# threading.Thread is used to control clicks


class ClickMouse(threading.Thread):

    # delay and button is passed in class
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    #Using same button to pause and not terminate program
    def stop_clicking(self):
        self.running = False

    #Hard exit program
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # double loop method
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

# instance of mouse controller is created
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


# on_press method takes key as argument
def on_press(key):
    # start_stop_key will stop clicking if flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

#exit method terminates auto clicker
    elif key == stop_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
