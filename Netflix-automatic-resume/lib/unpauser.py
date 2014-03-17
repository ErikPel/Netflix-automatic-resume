import win32api, win32con
import Image
import ImageGrab
import os
import ConfigParser
import time
class UnpauserClass():
    def __init__(self, config_path):
        self.config_path = config_path

    def average(self,num1,num2):
        total = num1+num2
        return total / 2

    def get_screen_resolution(self):
    	width = win32api.GetSystemMetrics (0)
    	height = win32api.GetSystemMetrics (1)
    	return width,height

    def convert_list_items(self,items):
        converted = []
        for item in items:
            converted.append(int(item))
        return converted

    def get_coordinates(self):
        screen_resolution = self.get_screen_resolution()
        resolution_str = str(screen_resolution[0]) + "x" + str(screen_resolution[1])
        config = ConfigParser.ConfigParser()
        with open(os.path.dirname(os.path.dirname(__file__)) + self.config_path,'r') as configfile:
            config.readfp(configfile)
            coordinates = config.get("Play-icon Position", resolution_str).split(",")
        coordinates = self.convert_list_items(coordinates)

        return coordinates

    def screenGrab(self,coordinates):
        coordinates
        im = ImageGrab.grab(coordinates)
        return im

    def leftClick(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    def mousePos(self,cord):
        win32api.SetCursorPos((cord[0],cord[1]))

    def average_image_color(self,i):
    	h = i.histogram()

    	# split into red, green, blue
    	r = h[0:256]
    	g = h[256:256*2]
    	b = h[256*2: 256*3]
     
    	# perform the weighted average of each channel:
    	# the *index* is the channel value, and the *value* is its weight
    	return (
    		sum( i*w for i, w in enumerate(r) ) / sum(r),
    		sum( i*w for i, w in enumerate(g) ) / sum(g),
    		sum( i*w for i, w in enumerate(b) ) / sum(b)
    	)

    def get_click_position(self,coordinates):
        x_coordinate = self.average(coordinates[0],coordinates[2])
        y_coordinate = self.average(coordinates[1],coordinates[3])
        return x_coordinate,y_coordinate
