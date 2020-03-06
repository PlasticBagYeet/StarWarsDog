import pygame
import Constants

class StarWarsDog:
    show_cut_scene = True
    all_game_rects = pygame.sprite.RenderUpdates()
    cut_scene_background = pygame .Surface(Constants.SCREEN_RECTANGLE.size)

    def main(self):
        if(pygame.get_sdl_version()[0] ==2):

        pygame.init()




if(__name__== "__main__"):
    StarWarsDog().main()
