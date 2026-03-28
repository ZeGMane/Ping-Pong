from pygame import *

win = display.set_mode((600,500))
display.set_caption('Ping-Pong')

bg = transform.scale(image.load('bg.png'), (600,500))

game = True
while game:
    win.blit(bg, (0,0))
    
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    display.update()
            
