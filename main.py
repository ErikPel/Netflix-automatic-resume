from lib.unpauser import UnpauserClass
import Image
import time
import os
def main():
    while True:
        unpause_netflix()
        time.sleep(1)

def unpause_netflix():
    unpause = UnpauserClass("/data/config.cfg")
    coordinates = unpause.get_coordinates()
    screenshot = unpause.screenGrab(coordinates)
    original = Image.open(os.path.dirname(__file__)+'/data/play_icon.png')
    if unpause.average_image_color(screenshot) == unpause.average_image_color(original):
        print "[" + time.strftime('%X') + "] Netflix Paused automatically"
        mouse_position = unpause.get_click_position(coordinates)
        unpause.mousePos(mouse_position)
        unpause.leftClick()
        print "[" + time.strftime('%X') + "] resumed playback"
if __name__ == '__main__':
        main()