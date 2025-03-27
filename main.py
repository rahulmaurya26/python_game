import pygame
import random

pygame.init()
screen_width=1150
screen_hight=800
antiquewhite4=(240,100,240)
white = (255, 255, 255)
red = (255, 0, 0)
yellow=(227,207,87)
green=(127,255,0)
aqua=(0,255,255)
pink=(255,187,255)
blue=(0,127,255)
black=(0,0,0)
color_list=['white','red','yellow','green','aqua','pink','blue','black']
font = pygame.font.SysFont(None, 55)
gamewindow=pygame.display.set_mode((screen_width,screen_hight))
gamewindow=pygame.display.set_mode((screen_width,screen_hight))
welcome_image=pygame.image.load("welcome2.jpg")
welcome_image=pygame.transform.scale(welcome_image,(screen_width,screen_hight)).convert_alpha()
game_image=pygame.image.load("birdimage2.jpg")
game_image=pygame.transform.scale(game_image,(screen_width,screen_hight)).convert_alpha()

def random_color():
   return random.choice(color_list)

def text_screen(text,color,x,y):
  screec_text=font.render(text,True,color)
  gamewindow.blit(screec_text,[x,y])



def plumb():
  exit_game = False
  game_over = False
  score=0
  with open("bird_hiscore",'r') as f:
    hiscore=f.read()
  # upper
  plumb_uy = 0
  plumb_ux1 = 1100
  plumb_ux2 = 1300
  plumb_ux3 = 1500
  plumb_ux4 = 1700
  plumb_ux5 = 1900
  plumb_ux6 = 2100
  plumb_hightu1=random.randint(200,300)
  plumb_hightu2=random.randint(200,300)
  plumb_hightu3=random.randint(200,300)
  plumb_hightu4=random.randint(200,300)
  plumb_hightu5=random.randint(200,300)
  plumb_hightu6=random.randint(200,300)
  
  
  
  # lower
  plumb_hightl=550  
  plumb_lx1=1100
  plumb_lx2=1300
  plumb_lx3=1500
  plumb_lx4=1700
  plumb_lx5=1900
  plumb_lx6=2100
  plumb_ly1=random.randint(400,600)
  plumb_ly2=random.randint(400,600)
  plumb_ly3=random.randint(400,600)
  plumb_ly4=random.randint(400,600)
  plumb_ly5=random.randint(400,600)
  plumb_ly6=random.randint(400,600)

  cir_y=300
  cir_x=300
 
  plumb_size=50
  velocity_x = 0
  velocity_y = 0
  init_velocity = -10
  clock = pygame.time.Clock()
  fps=20
  a=random_color()
  d=18
  
  while not exit_game:
    if game_over:
      gamewindow.fill(white)
      with open("bird_hiscore",'w') as f:
        f.write(str(hiscore))
      text_screen("over",red,300,300)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
             exit_game = True
          if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
             plumb()
    else:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
             exit_game = True
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
              velocity_x=init_velocity
            if event.key == pygame.K_SPACE:
              velocity_x=0
              velocity_y=0
            if event.key == pygame.K_DOWN:
              velocity_y=-init_velocity
            if event.key == pygame.K_UP:
              velocity_y=init_velocity
      
      if plumb_ux1==0:
        plumb_ux1=screen_width
        plumb_lx1=screen_width
        plumb_ly1=random.randint(400,600)
        plumb_hightu1=random.randint(200,300)

      elif plumb_ux2==0:
        plumb_ux2=screen_width
        plumb_lx2=screen_width
        plumb_ly2=random.randint(400,600)
        plumb_hightu2=random.randint(200,300)
        
        
      elif plumb_ux3==0:
        plumb_ux3=screen_width
        plumb_lx3=screen_width
        plumb_ly3=random.randint(400,600)
        plumb_hightu3=random.randint(200,300)
        
        
      elif plumb_ux4==0:
        plumb_ux4=screen_width
        plumb_lx4=screen_width
        plumb_ly4=random.randint(400,600)
        plumb_hightu4=random.randint(200,300)
        
        
      elif plumb_ux5==0:
        plumb_ux5=screen_width
        plumb_lx5=screen_width
        plumb_ly5=random.randint(400,600)
        plumb_hightu5=random.randint(200,300)
        
                
      elif plumb_ux6==0:
        plumb_ux6=screen_width
        plumb_lx6=screen_width
        plumb_ly6=random.randint(400,600)
        plumb_hightu6=random.randint(200,300)
        
        
        
      cir_y = cir_y + velocity_y
      
      plumb_ux1 = plumb_ux1 + velocity_x
      plumb_lx1 = plumb_lx1 + velocity_x

      plumb_ux2 = plumb_ux2 + velocity_x
      plumb_lx2 = plumb_lx2 + velocity_x
      
      plumb_ux3 = plumb_ux3 + velocity_x
      plumb_lx3 = plumb_lx3 + velocity_x
      
      plumb_ux4 = plumb_ux4 + velocity_x
      plumb_lx4 = plumb_lx4 + velocity_x
      
      plumb_ux5 = plumb_ux5 + velocity_x
      plumb_lx5 = plumb_lx5 + velocity_x
      
      plumb_ux6 = plumb_ux6 + velocity_x
      plumb_lx6 = plumb_lx6 + velocity_x
      
      # upper
      
      for i in range(1,plumb_hightu1+1):
        if (abs(plumb_ux1 - cir_x)<d and abs((plumb_uy+i)- cir_y)<d) or (abs(plumb_ux2 - cir_x)<d and abs((plumb_uy+i)- cir_y)<d) or (abs(plumb_ux3 - cir_x)<d and abs((plumb_uy+i)- cir_y)<d) or (abs(plumb_ux4 - cir_x)<d and abs((plumb_uy+i)- cir_y)<d) or (abs(plumb_ux5 - cir_x)<d and abs((plumb_uy+i)- cir_y)<d) or (abs(plumb_ux6 - cir_x)<d and abs((plumb_uy+i)- cir_y)<d) or (cir_y==0) or (cir_y==screen_hight)  :
          game_over=True
          
      # lower
          
      for i in range(1,plumb_hightl):
        if (abs(plumb_lx1 - cir_x)<d and abs((plumb_ly1+i)- cir_y)<d) or (abs(plumb_lx2 - cir_x)<8 and abs((plumb_ly2+i)- cir_y)<d) or (abs(plumb_lx3 - cir_x)<d and abs((plumb_ly3+i)- cir_y)<d) or (abs(plumb_lx4 - cir_x)<d and abs((plumb_ly4+i)- cir_y)<d) or (abs(plumb_lx5 - cir_x)<d and abs((plumb_ly5+i)- cir_y)<d) or (abs(plumb_lx6 - cir_x)<d and abs((plumb_ly6+i)- cir_y)<d):
          game_over=True
      
      if (plumb_ux1==290) or (plumb_ux2==290) or (plumb_ux3==290) or (plumb_ux4==290) or (plumb_ux5==290) or (plumb_ux6==290):
        score+=10
        a=random_color()
        if score>int(hiscore):
          hiscore=score
      
      gamewindow.blit(game_image,(0,0))

      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_ux1,plumb_uy,plumb_size,plumb_hightu1])
      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_lx1,plumb_ly1,plumb_size,plumb_hightl])
      

      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_ux2,plumb_uy,plumb_size,plumb_hightu2])
      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_lx2,plumb_ly2,plumb_size,plumb_hightl]) 
      
      
      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_ux3,plumb_uy,plumb_size,plumb_hightu3])
      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_lx3,plumb_ly3,plumb_size,plumb_hightl]) 
      
      
      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_ux4,plumb_uy,plumb_size,plumb_hightu4])
      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_lx4,plumb_ly4,plumb_size,plumb_hightl])
      
       
      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_ux5,plumb_uy,plumb_size,plumb_hightu5])
      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_lx5,plumb_ly5,plumb_size,plumb_hightl])
      
       
      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_ux6,plumb_uy,plumb_size,plumb_hightu6])
      pygame.draw.rect(gamewindow,antiquewhite4,[plumb_lx6,plumb_ly6,plumb_size,plumb_hightl]) 
      
      text_screen("Score:  "+str(score) + "  Highscore: "+str(hiscore), red, 10,50)
      pygame.draw.circle(gamewindow,a,[cir_x,cir_y],30)
      
      
    pygame.display.update()
    clock.tick(fps)
  pygame.quit()
  quit()


def welcome():
    exit_game =False
    gamewindow.fill(white)
    gamewindow.blit(welcome_image,(0,0))    
    text_screen("Play Game ! Press Enter ",red,300,650)
    text_screen("Bird Game ",aqua,400,500)
    pygame.display.update()
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    plumb()
        pygame.display.update()
welcome()
