'''
Run the  follwing command im commmand prompt ,after downloading pygame
python -m pip install pygame

Collecting pygame
  Downloading https://files.pythonhosted.org/packages/ed/56/b63ab3724acff69f4080e54c4bc5f55d1fbdeeb19b92b70acf45e88a5908/pygame-1.9.6-cp37-cp37m-win_amd64.whl (4.3MB)
    100% |████████████████████████████████| 4.3MB 361kB/s
Installing collected packages: pygame
Successfully installed pygame-1.9.6
You are using pip version 10.0.1, however version 19.1.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
'''

'''
This proggram needs "ball.bmp" ,
So, store a ball picture in the working direcctory in the name ball.bmp
'''


import sys
import  pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
bg = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit();
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1] 

        screen.fill(bg)
        screen.blit(ball, ballrect)
        pygame.display.flip()
