import pygame
import random
import math
from pygame import mixer

#initalise pygame (remember!)
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space shooter game by yass gr")

game_icon = pygame.image.load("enemey.png")
pygame.display.set_icon(game_icon)

font = pygame.font.Font("SPACE.ttf", 15)
font_over = pygame.font.Font("SPACE.ttf", 30)
fontX = 10
fontY = 10

shooting_sound = mixer.Sound("laser.wav")
enemy_down_sound = mixer.Sound("explosion.wav")
mixer.music.load("background.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.7)

def show_score(X, Y):
    scoredisplay = font.render("Score : " + str(score), True,(167,171,242))
    screen.blit(scoredisplay, (X,Y))


#player
player_img = pygame.image.load("spaceship.png")
player_img = pygame.transform.scale(player_img, (50,50))
px = random.randint(0, 768)
py = 520
px_a = 0
def player(x,y):
    screen.blit(player_img,(x,y))

#enemey
enemy_img = pygame.image.load("enemey.png")
enemy_img = pygame.transform.scale(enemy_img, (50,50))
ex = []
ey = []
ex_a = []
ey_a = []
def enemy(x, y, i):
    screen.blit(enemy_img,(x,y))

n_enemys = 7
for i in range(n_enemys):
    ex.append(random.randint(0, 768))
    ey.append(100)
    ex_a.append(0.3)
    ey_a.append(40)


#bullet
bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (32,32))
bx = 0
by = 550
bx_a = 0
by_a = 3
bullet_state = "ready"
def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img,(x + 8,y - 15))

# collision function
def is_collision(ex, ey, bx, by):
    distance = math.sqrt((math.pow(ex - bx, 2)) + (math.pow(ey - by, 2)))
    if distance < 27:
        return True
    else:
        return False
    
#score declaration
score = 0

background = pygame.image.load("bg.png")

#game loop
game_over = False
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    if game_over == True:
        game_over_display = font_over.render("       GAME OVER\nclick 'n' to restart\nclick 'x' to exit",True,(255,0,0))
        screen.blit(game_over_display, (170, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  
                running = False
            if event.key == pygame.K_n and game_over:  
                game_over = False

        if game_over == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    px_a = -0.5
                if event.key == pygame.K_RIGHT:
                    px_a = 0.5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bx = px
                        bullet(bx, by)
                        shooting_sound.play()
                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    px_a = 0
    
    if game_over == False:
        px += px_a

        # setting boundaries for the player
        if px <= 0:
            px = 0 
        elif px >= 768:
            px = 768

    

        #enemeys automatic movement
        for i in range(n_enemys):
            # setting boundaries for the enemey
            if ex[i] <= 0:
                ex[i] = 0 
            elif ex[i] >= 768:
                ex[i] = 768
            if ey[i] <= 0:
                ey[i] = 0 
            elif ey[i] >= 568:
                ey[i] = 568

        
            ex[i] += ex_a[i]
            if ex[i] <= 0:
                ex_a[i] = 0.3
                ey[i] += ey_a[i] 
            elif ex[i] >= 768:
                ex_a[i] = -0.3
                ey[i] += ey_a[i]
        
            #collision detection
            collision = is_collision(ex[i], ey[i], bx, by)
            if collision:
                enemy_down_sound.play()
                by = 550
                score += 1
                bullet_state = "ready"
                
                ex[i] = random.randint(0, 768)
                ey[i] = 50
        
            #creating the enemy
            enemy(ex[i], ey[i], i)
            if ey[i] > 400:
                game_over = True
                for f in range(n_enemys):
                    ey[f] = 100
                

                
   


   
        #bullet logic
        if by <= 0:
            by = 550
            bullet_state = "ready"

        if bullet_state == "fire":
            bullet(bx, by)
            by -= by_a

 

        player(px, py)
        show_score(fontX, fontY)
    
    

    font_info = pygame.font.Font(None, 20)
    info = font_info.render("*Press 'space' to shoot\n*Move with arrow Keys",True , (164,166,161))
    info.set_alpha(120)
    screen.blit(info, (10, 570))

    pygame.display.update()
