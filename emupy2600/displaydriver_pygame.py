import pygame


class DisplayDriverPyGame(object):

	def __init__(self, width, height):

        self.size = width, height 
        self.screen = pygame.display.set_mode(self.size)


	def draw_horizontal_line(
			self, xstart, xend, y):

		pygame.draw.line(
                pygame.display.get_surface(), 
                (0,127,0), 
                (0,self.current_scanline), 
                (self.size.width, 200))


	def end_frame(self):
        pygame.display.flip()

