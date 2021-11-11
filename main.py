import random  # For generating random numbers
import sys  # We will use sys.exit to exit the program
import pygame
from pygame.locals import *  # Basic pygame imports

# Global Variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'images/bird.png'
BACKGROUND = 'images/background.png'
PIPE = 'images/pipe.png'


def welcomeScreen():
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    msgx = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    msgy = int(SCREENHEIGHT*0.13)
    base_x = 0

    # event handling
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.type==K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type==KEYDOWN and (event.type==K_UP or event.type==K_SPACE): #return to main game event
                return

            else:
                SCREEN.blit(GAME_SPRITES['bg'],(0 , 0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx , playery))
                SCREEN.blit(GAME_SPRITES['message'],( msgx, msgy))
                SCREEN.blit(GAME_SPRITES['base'],( base_x, GROUNDY))
                pygame.display.update()
                clock.tick(FPS)

def Game():
    score=0
    playerx=int(SCREENWIDTH/5) #initial position
    playery=int(SCREENWIDTH/2)
    base_x=0
    
def getRandomPipe():
    offset=SCREENHEIGHT/4
    pipeHeight=GAME_SPRITES['pipe'][0].get_height()
    


if __name__ == "__main__":   
    pygame.init()  
    clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird Game')
    # pygame.display.set_icon(pygame.image.load(PLAYER))
    GAME_SPRITES['numbers'] = (
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] = pygame.image.load(
        'images/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load(
        'images/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                            pygame.image.load(PIPE).convert_alpha()
                            )

    # Game GAME_GAME_GAME_SOUNDS
    GAME_SOUNDS['die'] = pygame.mixer.Sound('audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('audio/wing.wav')

    GAME_SPRITES['bg'] = pygame.image.load('images/background.png').convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    welcomeScreen()
    Game()