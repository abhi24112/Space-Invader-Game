import pygame
import random

# initializing the pygame
pygame.init()

# game window of width=800 height=600
screen = pygame.display.set_mode((800, 600))

# Background image
background = pygame.image.load("background.jpg")

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player Image
playerImg = pygame.image.load("spaceship.png")
#loction of player
playerx = 370
playery = 480
playerx_change = 0

def player(x,y):   #blit is used to draw the player to screen
    screen.blit(playerImg,(x,y))


# Enemy Image
enemyImg = pygame.image.load("monster.png")
# loction of enemy at random at random position in game
enemyx = random.randint(0,800)
enemyy = random.randint(50,150)
enemyx_change = 0.5
enemyy_change = 40   # to get ememy near to the player(enemy move down)

def enemy(x,y):   #blit is used to draw the enemy to screen
    screen.blit(enemyImg,(x,y))


# loop screen to open it as much as we want
running = True
while running:

    #screen color
    screen.fill((0,0,0)) #black

    # Background persist 
    # after adding background the process become slow because the 
    # while loop uploding this heavy background again and again  
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if keystroke is press check whether its right or left
        if event.type == pygame.KEYDOWN: # key is press down
            if event.key == pygame.K_LEFT:
                playerx_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

     
    # if we need anything persist in the game screen
    # it should be inside of the (while loop)

    # playerx += 0.1 for movment mechanics
    # display player and change its location
    playerx += playerx_change

    # giving the spaceship a boundary to stay in game
    if playerx <=0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    player(playerx,playery)


    # enemy movement
    enemyx += enemyx_change

    # enemy get closer to player spaceship
    if enemyx <= 0:
        enemyx_change = 0.5
        enemyy += enemyy_change
    elif enemyx >= 736:
        enemyx_change = -0.5
        enemyy += enemyy_change
    enemy(enemyx,enemyy)


    # Now our display is not updating
    pygame.display.update()