import pygame
import os

pygame.init()

# global constants
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # defines display where game will be shown

# LOAD IN IMAGES - HIKER
RUNNING = [pygame.image.load(os.path.join('assets/hiker', 'hiker-run1.png')), 
           pygame.image.load(os.path.join('assets/hiker', 'hiker-run2.png'))]
JUMPING = pygame.image.load(os.path.join('assets/hiker', 'hiker-jump.png'))
# DUCKING = [pygame.image.load(os.path.join('assets/hiker', 'hiker-duck1.png')), 
#            pygame.image.load(os.path.join('assets/hiker', 'hiker-duck2.png'))]

# # LOAD IN IMAGES - OBSTACLES
# SMALL_OBSTACLE = [pygame.image.load(os.path.join('assets/obstacles', 'campfire-small.png')),
#                   pygame.image.load(os.path.join('assets/obstacles', 'cactus-small.png')),
#                   pygame.image.load(os.path.join('assets/obstacles', 'snake-small.png'))]
# LARGE_OBSTACLE = [pygame.image.load(os.path.join('assets/obstacles', 'campfire-large.png')),
#                   pygame.image.load(os.path.join('assets/obstacles', 'cactus-large.png')),
#                   pygame.image.load(os.path.join('assets/obstacles', 'snake-large.png'))]
# BIRD = [pygame.image.load(os.path.join('assets/bird', 'bird1.png')),
#         pygame.image.load(os.path.join('assets/bird', 'bird2.png'))]

# # BACKGROUND
# CLOUD = pygame.image.load(os.path.join('assets/background', 'cloud.png'))
# BACKGROUND = pygame.image.load(os.path.join('assets/background', 'track.png'))


class Hiker:
  # position of hiker - remains stationary throughout game
  X_POS = 80
  Y_POS = 310

  def __init__(self):
    # self.duck_img = DUCKING
    self.run_img = RUNNING
    self.jump_img = JUMPING

    self.hiker_duck = False
    self.hiker_run = True
    self.hiker_jump = False

    self.step_index = 0
    self.image = self.run_img[0]
    # hit box
    self.hiker_rect = self.image.get_rect()
    self.hiker_rect.x = self.X_POS
    self.hiker_rect.y = self.Y_POS


  def update(self, userInput):
    if self.hiker_duck:
      self.duck()
    if self.hiker_run:
      self.run()
    if self.hiker_jump:
      self.jump()

    # step index to help animate hiker
    if self.step_index >= 10:
      self.step_index = 0
    
    # jumping and ducking functionality
    if userInput[pygame.K_UP] and not self.hiker_jump:
      self.hiker_duck = False
      self.hiker_run = False
      self.hiker_jump = True
    elif userInput[pygame.K_DOWN] and not self.hiker_jump:
      self.hiker_duck = True
      self.hiker_run = False
      self.hiker_jump = False
    elif not (self.hiker_jump or userInput[pygame.K_DOWN]):
      self.hiker_duck = False
      self.hiker_run = True
      self.hiker_jump = False

  def duck(self):
    pass

  # run animation
  def run(self):
    self.image = self.run_img[self.step_index // 5]
    self.hiker_rect = self.image.get_rect()
    self.hiker_rect.x = self.X_POS
    self.hiker_rect.y = self.Y_POS
    self.step_index += 1

  def jump(self):
    pass

  def draw(self, SCREEN):
    SCREEN.blit(self.image, (self.hiker_rect.x, self.hiker_rect.y))


def main():
  run = True
  clock = pygame.time.Clock()
  player = Hiker()

  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    SCREEN.fill((255, 255, 255))
    userInput = pygame.key.get_pressed()

    player.draw(SCREEN) # draws hiker on the screen
    player.update(userInput) # updates the hiker on every while loop iteration

    clock.tick(30)
    pygame.display.update()



main()