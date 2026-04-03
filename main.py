from pygame import *

win = display.set_mode((600,500))
display.set_caption('Ping-Pong')

bg = transform.scale(image.load('bg.png'), (600,500))

class GameSprite(sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 355:
            self.rect.y += self.speed
    
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 355:
            self.rect.y += self.speed
            
raketka_sprite = transform.scale(image.load('raletka.png'), (30, 140))
ball_sprite = transform.scale(image.load('ball.png'), (40,40))


raketka1 = Player(raketka_sprite, 20, 100, 8)
raketka2 = Player(raketka_sprite, 550, 100, 8)

ball = GameSprite(ball_sprite, 200, 250, 10)

clock = time.Clock()


ball_speed_x = 3
ball_speed_y = 3

font.init()
font1 = font.Font(None, 70)

lose1 = font1.render("1 PLAYER LOSE!", True, (255, 0, 0))
lose2 = font1.render("2 PLAYER LOSE!", True, (255, 0, 0))
    
game = True
finish = False
while game:
    win.blit(bg, (0,0))
    
    if not finish:
    
        raketka1.update_left()
        raketka1.reset()
        
        raketka2.update_right()
        raketka2.reset()
        

        if ball.rect.y < 0 or ball.rect.y > 450:
            ball_speed_y *= -1
    
    
        if sprite.collide_rect(ball, raketka1):
            ball_speed_x *= -1
            
        if sprite.collide_rect(ball, raketka2):
            ball_speed_x *= -1
            
        ball.reset()
        
        if ball.rect.x <= 0:
            win.blit(lose1, (100,250))
            finish = True
        
        if ball.rect.x >= 550:
            win.blit(lose2, (100,250))
            finish = True
        

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
        display.update()
        
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    clock.tick(60)
    
            
