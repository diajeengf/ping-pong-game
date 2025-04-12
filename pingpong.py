from pygame import *

class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
 
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# main player class
class Player(GameSprite):
    # method to comtrol the sprite with up down keys
    def update_r(self):
        keys = key.get_pressed()
        # up boundary
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        # down boundary
        if keys[K_DOWN] and self.rect.y < win_height-150:
            self.rect.y += self.speed

# method to control the sprite with up down keys
    def update_l(self):
        keys = key.get_pressed()
        # up boundary
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        # down boundary
        if keys[K_s] and self.rect.y < win_height-150:
            self.rect.y += self.speed

#game scene:
back = (200, 255, 255) #background color (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

#flags responsible for game state
game = True
finish = False
clock = time.Clock()
FPS = 60
#creating ball and paddles   
racket1 = Player('racket.png', 30, 200, 50, 150, 4) 
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('ball.png', 200, 200, 50, 50, 4)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_r()
        racket2.update_l()

        # make the ball moves automatically
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # if the ball reaches screen edges (top or bottom), changes its movement direction
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        # if the ball bourcing the paddles
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        
        # if ball files behind this paddle, display loss condition for player 1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = True

        # if ball files behind this paddle, display loss condition for player 2
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game = True



        racket1.reset()
        racket2.reset()
        ball.reset()
    
    display.update()
    clock.tick(FPS)
