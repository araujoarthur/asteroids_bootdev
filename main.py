import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
   #print("Starting asteroids!")
   #print(f"Screen width: {SCREEN_WIDTH}")
   #print(f"Screen height: {SCREEN_HEIGHT}")

   # PyGame Setup
   pygame.init()
   clock = pygame.time.Clock()
   dt = 0

   # Screen Setup
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
   # Groups Setup
   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   bullets = pygame.sprite.Group()

   # Player Class (Shared) Variable setup
   Player.containers = (updatable, drawable)

   # Player Setup
   player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

   # Asteroid Class (Shared) Variable setup
   Asteroid.containers = (asteroids, updatable, drawable)

   # AsteroidField class (shared) variable setup
   AsteroidField.containers = (updatable)

   # AsteroidField setup
   field = AsteroidField()

   # Shot Class (Shared) variable setup
   Shot.containers = (bullets, updatable, drawable)
   while True:
      screen.fill((0,0,0))

      # Updates all members of group updatable
      updatable.update(dt)

      for asteroid in asteroids:
         if asteroid.check_colision(player):
            print("Game Over!")
            exit()
      
      for asteroid in asteroids:
         for bullet in bullets:
            if bullet.check_colision(asteroid):
               bullet.kill()
               asteroid.split()
            
      # Draws each member of drawable
      for member in drawable:
         member.draw(screen)
     

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
      
      
      dt = clock.tick(60)/1000
      pygame.display.flip()

if __name__ == "__main__":
   main()