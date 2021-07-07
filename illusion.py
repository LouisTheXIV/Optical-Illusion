import pygame
import random
import time


pygame.init()

white = (255,255,255)
black = (0,0,0)
gray = (190,190,190)
blue = (0,0,255)
yellow = (200,200,0)

w_height = 600
w_width = 800

clock = pygame.time.Clock()

display = pygame.display.set_mode((w_width ,w_height))
pygame.display.set_caption('Illusion')

def main():
    isgray = False
    cube1 = cube(blue, 200, 266)
    cube2 = cube(yellow, 200*2, 266)
    over = False
    
    while not over:

        clock.tick(60)
                
        for event in pygame.event.get():                
            if event.type == pygame.QUIT:
                pygame.quit()
                over = True
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                isgray = not isgray

        drawGrid(isgray)
        cube1.draw()
        cube2.draw()

        pygame.display.update()    

    
def drawGrid(isgray=False):
    if isgray == True:
        color1 = gray
        color2 = gray
    else:
        color1 = white
        color2 = black
    color = white
    o = 0
    diff = 10
    for x in range(80):
        iseven = bool((o % 2) == 0)
        if iseven:
            color = color1
        else:
            color = color2
        pygame.draw.line(display, color, (0+o*diff,0), (0+o*diff, 600), diff)
        o += 1


class cube:
    def __init__(self, color, ypos, xpos):
        self.color = color
        self.y = ypos
        self.x = xpos
        self.width = 100
        self.height = 50
        self.speed = 1
        self.direction = "right"

    def draw(self):
        cube = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(display, self.color, cube, 0)
        self.move()

    def move(self):
        if self.x > 700:
            self.direction = "left"
        elif self.x < 50:
            self.direction = "right"

        if self.direction == "right":
            self.x += self.speed
        else:
            self.x -= self.speed


main()
