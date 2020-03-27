import pygame


class Doge(pygame.sprite.Sprite):
    """
    this is the player
    """
    is_in_cut_scene = True
    x_velocity = 10
    y_velocity = 10
    images = []

    def __init__(self, screen_rectangle):
        """
        this is the constructor
        """
        pygame.sprite.Sprite.__init__(self,self.containers)

        self.SCREENRECT = screen_rectangle

        self.image = self.images[0]

        self.image_size = self.image.get_size()

        # self.scale_

        self.rect = self.image.get_rect(midright=(100, 100))