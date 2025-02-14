import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
   """
   Player class
   """

   def __init__(self, x, y):
      super().__init__(x, y, PLAYER_RADIUS)
      self.rotation = 0
      self.cannon_timer = 0

   def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right 
      return [a, b, c]
   
   def draw(self, screen):
      pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

   def rotate(self, dt):
      """
         Apply rotation
      """
      self.rotation += PLAYER_TURN_SPEED * dt # Multiplica o tempo que passou pelo turnspeed (300 rad/s?)

   def update(self, dt):
      keys = pygame.key.get_pressed()
      self.cannon_timer += dt
      # Rotates left if A is pressed
      if keys[pygame.K_a]:
         self.rotate(-dt)

      # Rotates Right if D is pressed
      if keys[pygame.K_d]:
         self.rotate(dt)

      if keys[pygame.K_w]:
         self.move(dt)
      
      if keys[pygame.K_s]:
         self.move(-dt)
      
      if keys[pygame.K_SPACE] and self.cannon_timer > PLAYER_SHOOT_COOLDOWN:
         self.shoot()

   def move(self, dt):
      #  We start with a unit vector pointing straight up from (0, 0) to (0, 1).
      #  We rotate that vector by the player's rotation, so it's pointing in the direction the player is facing.
      #  We multiply by PLAYER_SPEED * dt. A larger vector means faster movement.
      #  Add the vector to our position to move the player.

      #(x,y)->(0,1) = v / |v| = 1
      forward_vector = pygame.Vector2(0, 1)
      # Makes it point to the front of the player
      forward_vector = forward_vector.rotate(self.rotation)

      # Lembrar que position é um **VETOR POSIÇÃO**. Um vetor que aponta para o centro do player
      # A linha abaixo adiciona um vetor apontando para a FRENTE do player com magnitude PLAYERS_SPEED * dt ao vetor POSIÇÃO
      self.position += forward_vector * PLAYER_SPEED * dt

   def shoot(self):
      bullet = Shot(self.position.x, self.position.y)
      # Set shot facing direction and speed (i.e velocity) (Que baita exemplo da diferença entre velocidade e rapidez. Só com rapidez temos um tiro que vai, mas vai pra onde?)
      # Creates the unit vector
      bullet_velocity = pygame.Vector2(0, 1)
      # Sets it's direction to the same as player's
      bullet_velocity = bullet_velocity.rotate(self.rotation)
      # Set it's speed
      bullet_velocity = bullet_velocity * PLAYER_SHOT_SPEED
      
      bullet.velocity = bullet_velocity
      self.cannon_timer = 0
      