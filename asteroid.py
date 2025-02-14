import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

   def __init__(self, x, y, radius):
      super().__init__(x, y, radius)
   
   def draw(self, screen):
      pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

   def update(self, dt):
      self.position += self.velocity * dt
   
   def split(self):
      self.kill()

      # If it's the smallest one, it's gone
      if self.radius <= ASTEROID_MIN_RADIUS:
         return
      
      split_angle = random.uniform(20, 50)
      split_velocity1 = self.velocity.rotate(split_angle)
      split_velocity2 = self.velocity.rotate(-split_angle)

      new_radius = self.radius - ASTEROID_MIN_RADIUS

      asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
      
      asteroid1.velocity = split_velocity1 * 1.2
      asteroid2.velocity = split_velocity2 * 1.2

      
