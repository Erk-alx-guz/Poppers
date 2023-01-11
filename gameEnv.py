import pygame

class Poppers():
    
    def __init__(self):
        pass


    def render(self):
        pygame.init()

        horizontal = 725
        vertical = 730
        screen = pygame.display.set_mode((horizontal, vertical))

        pygame.display.set_caption("SnakeGame")

        clock = pygame.time.Clock()

        backGround = pygame.image.load('Images/background.jpg')
        backGroundRec = backGround.get_rect(center = (horizontal/2, vertical/2))

        floor = pygame.image.load('Images/floor.jpg')
        floorRec = floor.get_rect(midtop = (horizontal/2, vertical))

        cat = pygame.image.load('Images/cat2.jpg')
        catRec = cat.get_rect(midbottom = (horizontal/2,vertical-45))

        screen.blit(backGround, backGroundRec)
        screen.blit(floor, floorRec)
        screen.blit(cat, catRec)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)