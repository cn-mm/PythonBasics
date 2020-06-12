import pygame
import random
from p8_Blob import Blob

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)  # 0,0,0 will be BLACK
BLUE = (0, 0, 255)
RED = (255, 0, 0)

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

game_display = pygame.display.set_mode((WIDTH, HEIGHT))  # setmode take a tuple
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()  # used to handle frames per second

class BlueBlob(Blob):   # inherits from Blob class
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        self.color = BLUE

    def move_fast(self):
        self.x += random.randrange(-5, 5)
        self.y += random.randrange(-5, 5)

def draw_environment(blobs_list):
    game_display.fill(WHITE)  # clearing the frame\
    for blob_dict in blobs_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display,  # where the circle will be drawn
                               blob.color,  # color
                               [blob.x, blob.y],  # location of the blob
                               blob.size)  # radius
            blob.move_fast()
            blob.check_bounds()
    pygame.display.update()  # sends everything to the screen


def main():
    # red_blob = Blob(color=RED)
    blue_blobs = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))    # dict enum to give the blobs
    red_blobs = dict(enumerate([BlueBlob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))    # an id
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if someone clicks on the X in the corner
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs])
        clock.tick(60)  # 60 frames per second


if __name__ == '__main__':
    main()
