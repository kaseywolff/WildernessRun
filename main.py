import pygame
import os
import random

pygame.init()

# global constants
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # defines display where game will be shown

# LOAD IN IMAGES - HIKER
RUNNING = [
            pygame.image.load(os.path.join('assets/hiker', 'hiker_run3.png')),
            pygame.image.load(os.path.join('assets/hiker', 'hiker_run2.png')),
            pygame.image.load(os.path.join('assets/hiker', 'hiker_run1.png'))
          ]
JUMPING = pygame.image.load(os.path.join('assets/hiker', 'hiker_jump.png'))
DUCKING = [
            pygame.image.load(os.path.join('assets/hiker', 'hiker_duck1.png')), 
            pygame.image.load(os.path.join('assets/hiker', 'hiker_duck2.png'))
          ]

# LOAD IN IMAGES - OBSTACLES
SMALL_CACTUS = [
                pygame.image.load(os.path.join('assets/obstacles', 'cactus_small1.png')),
                pygame.image.load(os.path.join('assets/obstacles', 'cactus_small2.png'))
              ]
SMALL_CAMPFIRE = [
                  pygame.image.load(os.path.join('assets/obstacles', 'campfire_small1.png')),
                  pygame.image.load(os.path.join('assets/obstacles', 'campfire_small2.png'))
                ]
SNAKE = [
          pygame.image.load(os.path.join('assets/obstacles', 'snake1.png')),
          pygame.image.load(os.path.join('assets/obstacles', 'snake2.png'))
        ]
# BIRD = [pygame.image.load(os.path.join('assets/bird', 'bird1.png')),
#         pygame.image.load(os.path.join('assets/bird', 'bird2.png'))]

# # BACKGROUND
CLOUD = pygame.image.load(os.path.join('assets/background', 'cloud.png'))
BACKGROUND = pygame.image.load(os.path.join('assets/background', 'ground.png'))


class Hiker:
  # position of hiker - remains stationary throughout game
  X_POS = 80
  Y_POS = 330
  Y_POS_DUCK = 356
  JUMP_VELOCITY = 8.5

  def __init__(self):
    self.duck_img = DUCKING
    self.run_img = RUNNING
    self.jump_img = JUMPING

    self.hiker_duck = False
    self.hiker_run = True
    self.hiker_jump = False

    self.step_index = 0
    self.jump_velocity = self.JUMP_VELOCITY
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
    self.image = self.duck_img[self.step_index // 4 % len(self.duck_img)]
    self.hiker_rect = self.image.get_rect()
    self.hiker_rect.x = self.X_POS
    self.hiker_rect.y = self.Y_POS_DUCK
    self.step_index += 1

  # run animation
  def run(self):
    self.image = self.run_img[self.step_index // 4 % len(self.run_img)]
    self.hiker_rect = self.image.get_rect()
    self.hiker_rect.x = self.X_POS
    self.hiker_rect.y = self.Y_POS
    self.step_index += 1

  def jump(self):
    self.image = self.jump_img
    if self.hiker_jump:
      self.hiker_rect.y -= self.jump_velocity * 4 ## decrease y position of hiker (top left corner is (0,0))
      self.jump_velocity -= 0.8
    
    if self.jump_velocity < -self.JUMP_VELOCITY:
      self.hiker_jump = False
      self.jump_velocity = self.JUMP_VELOCITY

  def draw(self, SCREEN):
    SCREEN.blit(self.image, (self.hiker_rect.x, self.hiker_rect.y))


# BACKGROUND CLASSES (cloud)
class Cloud:
  def __init__(self):
    self.x = SCREEN_WIDTH + random.randint(800, 1000)
    self.y = random.randint(50, 100)
    self.image = CLOUD
    self.width = self.image.get_width()

  # move cloud from right of screen to left
  def update(self, game_speed):
    self.x -= game_speed

    # reset cloud when it moves off screen
    if self.x < -self.width:
      self.x = SCREEN_WIDTH + random.randint(2500, 3000)
      self.y = random.randint(50, 100)
  

  def draw(self, SCREEN):
    SCREEN.blit(self.image, (self.x, self.y))


# OBSTACLE CLASSES (campfire, cactus, snake)
class Obstacle:
  def __init__(self, image, type):
    self.image = image
    # gets type of obstacle (campfire, cactus, snake)
    self.type = type
    self.rect = self.image[self.type].get_rect()
    # image is just off the edge of the screen
    self.rect.x = SCREEN_WIDTH

  def update(self):
    self.rect.x -= game_speed
    if self.rect.x < -self.rect.width:
      obstacles.pop()
  
  def draw(self, SCREEN):
    SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
  def __init__(self, image):
    self.type = random.randint(0, 1)
    super().__init__(image, self.type)
    self.rect.y = 345


class SmallCampfire(Obstacle):
  def __init__(self, image):
    self.type = 0
    super().__init__(image, self.type)
    self.rect.y = 345
    self.index = 0 # used for animation
  
  def draw(self, SCREEN):
    if self.index >= 9:
      self.index = 0
    SCREEN.blit(self.image[self.index // 5], self.rect)
    self.index += 1

class Snake(Obstacle):
  def __init__(self, image):
    self.type = 0
    super().__init__(image, self.type)
    self.rect.y = 367
    self.index = 0 # used for animation
  
  def draw(self, SCREEN):
    if self.index >= 40:
      self.index = 0
    frame_index = self.index // 5
    frame_index %= len(self.image)  # ensure index stays within the range of the image list
    SCREEN.blit(self.image[frame_index], self.rect)
    self.index += 1


def main():
  global game_speed, x_pos_background, y_pos_background, points, obstacles
  run = True
  clock = pygame.time.Clock()
  player = Hiker()
  cloud = Cloud()
  game_speed = 14
  x_pos_background = 0
  y_pos_background = 410
  points = 0
  font = pygame.font.Font('freesansbold.ttf', 20)
  obstacles = []

  def score():
    global points, game_speed
    points += 1
    # game becomes increasingly fast the longer you stay alive
    if points % 100 == 0:
      game_speed += 1
    
    text = font.render('Points: ' + str(points), True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (1000, 40)
    SCREEN.blit(text, text_rect)


  def background():
    global x_pos_background, y_pos_background
    image_width = BACKGROUND.get_width()
    SCREEN.blit(BACKGROUND, (x_pos_background, y_pos_background))
    # second background image
    SCREEN.blit(BACKGROUND, (image_width + x_pos_background, y_pos_background))
    # when first background image moves off the screen, add second image
    if x_pos_background <= -image_width:
      SCREEN.blit(BACKGROUND, (image_width + x_pos_background, y_pos_background))
      x_pos_background = 0
    # subtract game speed from position of background so it moves
    x_pos_background -= game_speed

  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    SCREEN.fill((255, 255, 255))
    userInput = pygame.key.get_pressed()

    background()

    if len(obstacles) == 0:
      if random.randint(0, 3) == 0:
        obstacles.append(SmallCactus(SMALL_CACTUS))
      elif random.randint(0, 3) == 1:
        obstacles.append(SmallCampfire(SMALL_CAMPFIRE)) 
      elif random.randint(0, 3) == 2:
        # obstacles.append(Bird(BIRD))
        obstacles.append(Snake(SNAKE)) 
      elif random.randint(0, 3) == 3:
        # obstacles.append(LargeObstacle(LARGE_OBSTACLE))
        obstacles.append(Snake(SNAKE)) 

    
    for obstacle in obstacles:
      obstacle.draw(SCREEN)
      obstacle.update()
      if player.hiker_rect.colliderect(obstacle.rect):
        pygame.draw.rect(SCREEN, (255, 0, 0), player.hiker_rect)
    

    cloud.draw(SCREEN)
    cloud.update(game_speed)

    score()

    player.draw(SCREEN) # draws hiker on the screen
    player.update(userInput) # updates the hiker on every while loop iteration


    clock.tick(30)
    pygame.display.update()



main()