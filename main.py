import pygame
from constants import *

def main():
   #print("Starting asteroids!")
   #print(f"Screen width: {SCREEN_WIDTH}")
   #print(f"Screen height: {SCREEN_HEIGHT}")

   pygame.init()
   clock = pygame.time.Clock()
   dt = 0
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   while True:
      screen.fill((0,0,0))

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
      
      # 
      dt = clock.tick(60)/1000
      print(dt)
      pygame.display.flip()

if __name__ == "__main__":
   main()