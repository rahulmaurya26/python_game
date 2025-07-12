import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
bgimg=pygame.image.load("snake.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
wlimg=pygame.image.load("welcome2.jpg")
wlimg=pygame.transform.scale(wlimg,(screen_width,screen_height)).convert_alpha()
# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcone():
   exit_game=False
   gameWindow.fill(white)
   
   gameWindow.blit(wlimg,(0,0))
   text_screen("Play Game ! Press Enter ",red,200,500)
   text_screen("To Snake Game ",white,300,400)
   
   pygame.display.update()
   while not exit_game:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            exit_game=True
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
               gameloop()
# Game Loop
def gameloop():
  exit_game = False
  game_over = False
  snake_x = 45
  snake_y = 55
  velocity_x = 0
  velocity_y = 0
  snk_list = []
  snk_length = 1
  food_x = random.randint(80, 400)
  food_y = random.randint(80, 400)
  
  with open("hiscore.txt","r") as f:
    hiscore=f.read()
  score = 0
  init_velocity = 5
  snake_size = 20
  fps = 40
  while not exit_game:
    if game_over:
       with open("hiscore.txt","w")as f:
          f.write(str(hiscore))
       gameWindow.fill(white)
       text_screen("Game over ! press enter to continue",red,180,300)
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
               exit_game = True
         if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
               gameloop()
    else:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
               exit_game = True

         if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RIGHT:
                  velocity_x = init_velocity
                  velocity_y = 0

               if event.key == pygame.K_LEFT:
                  velocity_x = - init_velocity
                  velocity_y = 0

               if event.key == pygame.K_UP:
                  velocity_y = - init_velocity
                  velocity_x = 0

               if event.key == pygame.K_DOWN:
                  velocity_y = init_velocity
                  velocity_x = 0

      snake_x = snake_x + velocity_x
      snake_y = snake_y + velocity_y

      if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
         score +=10
         food_x = random.randint(20, screen_width)
         food_y = random.randint(20, screen_height)
         snk_length +=5
         if score>int(hiscore):
            hiscore=score

      # gameWindow.fill(white)
      gameWindow.blit(bgimg,(0,0))
      text_screen("Score: " + str(score) + "  Hiscore: " +   str(hiscore), red, 5, 5)
      pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

      head = []
      head.append(snake_x)
      head.append(snake_y)
      snk_list.append(head)

      if len(snk_list)>snk_length:
         del snk_list[0]
      
      if head in snk_list[:-1]:
         game_over=True         
      if snake_y<0 or snake_x<0 or snake_x>screen_width or snake_y>screen_height:
         game_over=True
         
      plot_snake(gameWindow, white, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)

  pygame.quit()
  quit()
  
welcone()


