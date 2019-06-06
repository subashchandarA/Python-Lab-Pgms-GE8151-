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
import pygame
import math
import sys

pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Elliptical orbit")

clock = pygame.time.Clock()
count=0
while(count < 2):       
    xRadius = 250
    yRadius = 100 
    count=count+1
    for degree in range(0,360,10):
        x1 = int(math.cos(degree * 2 * math.pi / 360) * xRadius) + 300
        y1 = int(math.sin(degree * 2 * math.pi / 360) * yRadius) + 150
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), [300, 150], 35)
        pygame.draw.ellipse(screen, (255, 255, 255), [50, 50, 500, 200], 1)
        pygame.draw.circle(screen, (0, 0, 255), [x1, y1], 15)
        
        pygame.display.flip()
        clock.tick(5)
        
sys.exit()    
