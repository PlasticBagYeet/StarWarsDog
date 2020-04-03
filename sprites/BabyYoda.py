import pygame


class BabyYoda(pygame.sprite.Sprite):
    """
        This is the baby
    """
    is_in_cut_scene = True
    x_velocity = 10
    y_velocity = 10
    images = []

    def __init__(self, screen_rectangle):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.SCREENRECT = screen_rectangle

        self.image = self.images[0]

        self.image_size = self.image.get_size()

        self.scale_images()

        self.rect = self.image.get_rect(midright=(200, 100))

    def scale_images(self):
        # image is too big. scale down
        self.image_size = (
            int(self.image_size[0]*.2), int(self.image_size[1]*.2)
        )

        image_count = len(self.images)

        for image_counter in range(image_count):
            self.images[image_counter] = pygame.transform.scale(
                self.images[image_counter], self.image_size)

    def visibility(self, can_show):
        if(can_show is True):
            self.image = self.images[1]
        else:
            self.image = self.images[0]

    def move(self, x_velocity, y_velocity):
        self.rect.move_ip(x_velocity, y_velocity)

    def update(self):
        """
        needs to handle cut scene and game play
        """
        if(self.is_in_cut_scene is True):
            pass
        else:
            pass

