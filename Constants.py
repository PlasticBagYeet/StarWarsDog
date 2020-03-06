import os
import pygame
from pygame.locals import Rect

current_directory = os.getcwd()
home_path = os.environ._data["HOMEDRIVE"] + os.environ._data["HOMEPATH"]

DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 768
GOLD = (255, 215, 0)
IMAGES_PATH = "data\\images"
SCREEN_RECTANGLE = Rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT)
STAR_JEDI_LARGE_FONT = home_path + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Starjedi.ttf"
MAIN_DIRECTORY =os.path.split(os.path.abspath(__file__))[0]
