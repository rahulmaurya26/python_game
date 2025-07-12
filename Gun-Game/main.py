import pygame
import random
pygame.init()
pygame.mixer.init()
screen_width=900
screen_hight=600
black=(0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow=(227,207,87)
green=(127,255,0)
aqua=(0,255,255)
pink=(255,187,255)
blue=(0,127,255)
color_list=['aqua','black','white','red','yellow','green','pink','blue']
gamewindow=pygame.display.set_mode((screen_width,screen_hight))
wlimg=pygame.image.load('welcome2.jpg')
wlimg=pygame.transform.scale(wlimg,(screen_width,screen_hight)).convert_alpha()
bkimg=pygame.image.load('img1.jpg')
bkimg=pygame.transform.scale(bkimg,(screen_width,screen_hight)).convert_alpha()
eximg=pygame.image.load('exit.jpg')
eximg=pygame.transform.scale(eximg,(400,100))
font=pygame.font.SysFont(None,50)
clock=pygame.time.Clock()
pygame.mixer.music.load('scout_sniper.mp3')
def random_color():
    return random.choice(color_list)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True, color)
    gamewindow.blit(screen_text,[x,y])
def welcome():
   exit_game=False
   gamewindow.fill(white)
   gamewindow.blit(wlimg,(0,0))
   pygame.display.set_caption('Gun Game')
   text_screen("Play Game ! Press Enter ",red,200,500)
   text_screen("Bouble Shoot ",aqua,300,400)
   pygame.display.update()
   while not exit_game:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            exit_game=True
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
               gameloop() 
def gameloop():
  exit_game=False
  game_over=False
  velocity_goli=0
  velocity_y=0
  counter=3
  goli_x=220
  cir_x=760
  cir_y=10
  goli_y=325
  fps=40
  a=random_color()
  pygame.display.set_caption('Gun Game')
  with open("goli.txt","r") as f:
    hiscore=f.read()
  score=0
  while not exit_game:
      if game_over:
           with open("goli.txt","w")as f:
             f.write(str(hiscore))
           gamewindow.fill(white)
           gamewindow.blit(eximg,(200,400))
           text_screen("GAME OVER!",red,200,200)
           text_screen("Press enter to continue!",red,200,300)
           text_screen("Press Space to exit  ",red,200,400)
           for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 exit_game=True
              if event.type==pygame.KEYDOWN:
                  if event.key==pygame.K_SPACE:
                     exit_game=True
                  if event.key==pygame.K_RETURN:
                     gameloop()
      else:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            exit_game=True
            with open("goli.txt","w")as f:
             f.write(str(hiscore))
          if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_SPACE:
                velocity_goli=20
                pygame.mixer.music.play()
             if event.key==pygame.K_q:
                score+=20
             if event.key==pygame.K_RETURN:
                velocity_y=5
               
        goli_x=goli_x+velocity_goli
        cir_y=cir_y+velocity_y       
        gamewindow.blit(bkimg,(0,0))
       #   gun up
        pygame.draw.line(gamewindow,red,[110,300],[300,300],10)
        pygame.draw.line(gamewindow,red,[100,350],[300,350],10)
        pygame.draw.line(gamewindow,red,[300,355],[300,296],10)
        pygame.draw.line(gamewindow,red,[110,300],[100,350],10)
       #   gun down
        pygame.draw.line(gamewindow,red,[110,350],[90,420],10)
        pygame.draw.line(gamewindow,red,[140,350],[120,420],10)
        pygame.draw.line(gamewindow,red,[90,420],[120,420],10)
        pygame.draw.line(gamewindow,red,[170,350],[160,390],10)
        pygame.draw.line(gamewindow,red,[165,390],[125,390],10)
        #  goli
        pygame.draw.circle(gamewindow,black,[goli_x,goli_y],20)
        if goli_x==900:
           goli_x=220
           velocity_goli=0
        if cir_y==600:
           counter-=1
           cir_y=10
           velocity_y=0
        if abs(goli_x - cir_x)<40 and abs(goli_y - cir_y)<40:
           score+=10
           pygame.mixer.music.play()
           goli_x=220
           velocity_goli=0
           cir_y=10
           cir_y=cir_y+velocity_y
           counter=3
           a=random_color()
           if score>int(hiscore):
             hiscore=score
        if counter==0:
           game_over=True
        text_screen("Remaining : " +  str(counter), red, 5, 50)    
        text_screen("Score: " + str(score) + "  Hiscore: " +   str(hiscore), red, 5, 5)    
        pygame.draw.circle(gamewindow,a,[cir_x,cir_y],40)
      pygame.display.update()
      clock.tick(fps)
  pygame.quit()
  quit()
welcome()
