import pygame
import Constants
from sprites.BabyYoda import BabyYoda
from sprites.Doge import Doge
import Utility



class StarWarsDog:
    show_cut_scene = True
    all_game_rects = pygame.sprite.RenderUpdates()
    Doge.containers = all_game_rects
    BabyYoda.containers = all_game_rects

    cut_scene_background = pygame .Surface(Constants.SCREEN_RECTANGLE.size)

    def main(self):
        if(pygame.get_sdl_version()[0] ==2):
            pygame.mixer.pre_init(44100, 32, 2, 1024)

        pygame.init()

        bestdepth = pygame.display.mode_ok(Constants.SCREEN_RECTANGLE.size, 0, 32)
        screen = pygame.display.set_mode(Constants.SCREEN_RECTANGLE.size, 0, bestdepth)

        self.set_game_obj_images(screen)
        
        pygame.display.flip()

        clock = self.do_cut_scene(screen)

    def do_cut_scene(self, screen):
        clock = self.do_shoot_out_scene(screen)

        clock =  self.do_rocket_launch_scene(screen, clock)

        return clock

    def do_shoot_out_scene(self, screen):
        doge = Doge(Constants.SCREEN_RECTANGLE)
        babyYoda = BabyYoda(Constants.SCREEN_RECTANGLE)

        while True is True:
            pass

    def set_game_obj_images(self, screen):
        doge_image = Utility.load_image_transparent_background("doge-walk left1.png")
        Doge.images = [doge_image]
        baby_yoda_image = Utility.load_image_transparent_background("baby yoda.png")
        BabyYoda.images = [baby_yoda_image]


if(__name__== "__main__"):
    StarWarsDog().main()
