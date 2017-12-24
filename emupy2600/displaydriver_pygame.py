import pygame


class DisplayDriverPyGame(object):

    def __init__(self, width, height):

        self.size = (width, height)
        self.screen = pygame.display.set_mode(self.size)


    def draw_horizontal_line(
            self, xstart, xend, y, colour):

        pygame.draw.line(
                pygame.display.get_surface(), 
                colour, 
                (xstart,y), 
                (xend - xstart, y))


    def end_frame(self):
        pygame.display.flip()

