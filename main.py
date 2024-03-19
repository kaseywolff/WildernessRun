import pygame
import os

pygame.init()

# global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT) # defines display where game will be shown

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