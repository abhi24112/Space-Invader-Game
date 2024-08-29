import pygame
import random
import math

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

# Multiple Enemies
enemyImg =[]
enemyx =[]
enemyy =[]
enemyx_change = []
enemyy_change = []
no_of_enemies = 6

# Enemy Image
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load("monster.png")) 
    # loction of enemy at random at random position in game
    enemyx.append(random.randint(0,800))
    enemyy.append(random.randint(50,150))
    enemyx_change.append(0.9) # enemy movement in x-axis
    enemyy_change.append(35) # to get ememy auto move and get near the player(enemy move down)

def enemy(x,y,i):   #blit is used to draw the enemy to screen
    screen.blit(enemyImg[i],(x,y))


# Bullet Image
bulletImg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 1.5
# 'Ready' means the bullet is at the rest state
# 'fire' means the bullet is at the moving state
bullet_state = 'ready'

def bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg,(x+16,y+10)) # bullet is appearing little off to its supposed position So, add the 16 in x and 10 in y

# Colliosion of bullet and enemy using distance formula
def Collision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt((math.pow(enemyx-bulletx,2)) + (math.pow(enemyy-bullety,2)))
    if distance < 27:
        return True
    else:
        return False

# Score 
score = 0


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
                playerx_change = -1
            if event.key == pygame.K_RIGHT:
                playerx_change = 1

            if bullet_state == 'ready': # Adding the so bullet only fire if it is in 'ready' state
                if event.key == pygame.K_SPACE or pygame.K_SPACE:
                    bulletx = playerx
                    bullet(bulletx,bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

     
    # if we need anything persist in the game screen
    # it should be inside of the (while loop)

    # bullet movement

    if bullet_state == 'fire': # fireing the bullet
        bullety -= bullety_change
        bullet(bulletx,bullety)

    if bullety <= 0: # resetting the bullet to the spaceship
        bullety = 480
        bullet_state = 'ready'


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
    for i in range(no_of_enemies):
        enemyx[i] += enemyx_change[i]

        # enemy get closer to player spaceship
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.5
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -0.5
            enemyy[i] += enemyy_change[i]


        # Collision
        collision = Collision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision :
            bullety = 480
            bullet_state = 'ready'
            score+=1
            print(score)
            enemyx[i] = random.randint(0,736) # 736 because of this "elif enemyx >= 736: enemyx_change = -0.5"
            enemyy[i] = random.randint(50,150)

        enemy(enemyx[i],enemyy[i], i)


    # Now our display is not updating
    # To show anything continuesly we have to use (update function)
    pygame.display.update()