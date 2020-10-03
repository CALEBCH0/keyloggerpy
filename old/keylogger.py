# records keyboard presses and logs it in a text file.
from pynput.keyboard import Key, Listener
import time


#def keypressed():
#    keyboard.is_pressed 

def log(filepath):
    open(filepath, 'w').write(on_pressed())


def on_press(key):
    print('{0} pressed'.format(key))
    if key == Key.esc:
        return False


def on_release(key):
    print('{0} pressed'.format(key))
    if key == Key.esc:
        return False


with Listener(on_press=on_press #, on_release=on_release
        ) as listener:
    listener.join()


#def main():
#    Listener()
#time.sleep(5)
#pynput.keyboard.Listener.stop


#if __name__ == '__main__':
#    main()


