import pygame
from pygame import*
import sys
import random
import time



SCREEN_WIDTH = 790
SCREEN_HEIGHT = 590

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
play = pygame.image.load('C:\\Users\\leon8\\Desktop\\VS Code Projects\\rock_paper_scissors\\Play.png').convert_alpha()
title = pygame.image.load('C:\\Users\\leon8\\Desktop\\VS Code Projects\\rock_paper_scissors\\title.png').convert_alpha()
rock = pygame.image.load('C:\\Users\\leon8\\Desktop\\VS Code Projects\\rock_paper_scissors\\Rock.png').convert_alpha()
paper = pygame.image.load('C:\\Users\\leon8\\Desktop\\VS Code Projects\\rock_paper_scissors\\Paper.png').convert_alpha()
scissors = pygame.image.load('C:\\Users\\leon8\\Desktop\\VS Code Projects\\rock_paper_scissors\\Scissors.png').convert_alpha()
choice = pygame.image.load('C:\\Users\\leon8\\Desktop\\VS Code Projects\\rock_paper_scissors\\choice.png').convert_alpha()

#game icon images
rock_icon = pygame.image.load('C:\\Users\\leon8\\Desktop\VS Code Projects\\rock_paper_scissors\\game_icons\\rock_icon.png').convert_alpha()
paper_icon = pygame.image.load('C:\\Users\\leon8\\Desktop\VS Code Projects\\rock_paper_scissors\\game_icons\\paper_icon.png').convert_alpha()
scissors_icon = pygame.image.load('C:\\Users\\leon8\\Desktop\VS Code Projects\\rock_paper_scissors\\game_icons\\scissors_icon.png').convert_alpha()

#scale down
rock_scale_down = pygame.transform.scale(rock_icon, (250,250))
paper_scale_down = pygame.transform.scale(paper_icon, (250,250))
scissor_scale_down = pygame.transform.scale(scissors_icon, (250,250))
#outcomes

win = pygame.image.load('C:\\Users\\leon8\\Desktop\\VS Code Projects\\rock_paper_scissors\\win.png').convert_alpha()
lose = pygame.image.load('C:\\Users\\leon8\\Desktop\VS Code Projects\\rock_paper_scissors\\lose.png').convert_alpha()
draw = pygame.image.load('C:\\Users\\leon8\\Desktop\VS Code Projects\\rock_paper_scissors\\draw.png').convert_alpha()
#game background
background = pygame.image.load('C:\\Users\\leon8\\Desktop\\VS Code Projects\\rock_paper_scissors\\background.png')
background = pygame.transform.scale(background,(800,600))


pygame.display.set_caption('Rock paper scissors')

class Button():
   def __init__(self, x,y, image):
      self.image = image
      self.rect = self.image.get_rect()
      self.rect.topleft = (x,y)
      self.clicked = False

   def draw(self):
      action = False

      #mouse position
      pos = pygame.mouse.get_pos()
      
      #check if mouse is on top of button and 
      if self.rect.collidepoint(pos):
         if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            action = True
      if pygame.mouse.get_pressed()[0] == 0:
         self.clicked = False
      #draws buttons
      screen.blit(self.image, (self.rect.x, self.rect.y))

      return action
#menu buttons
play_button = Button(100, 300, play)
title = Button(150,20, title)
play_again_button = Button(100, 300, play)

#Select buttons
rock_button = Button(350, 410, rock)
paper_button = Button(350, 210, paper)
scissor_button = Button(350, 10, scissors)
choice = Button(10, 10, choice)

#game icons

scissors_logo = Button(350, 410, scissors_icon)
rock_logo = Button(350, 410, rock_icon)
paper_logo = Button(350, 410, paper_icon)

#outcome
draw_outcome = Button(370, 410, draw)
win_outcome = Button(370, 410, win)
lose_outcome = Button(370, 410, lose)

run = True
selection = 0
number = (random.randint(1, 3))

pygame.init()

def game_choice():
   number = (random.randint(1, 3))
   if number == 1:
      rock_logo.draw()
   elif number == 2:
      paper_logo.draw()
   else:
      scissors_logo.draw()


   


#all outcomes of rock paper scissors
def outcomes(selection):
   
   while True:
       
       screen.blit(background, (0,0))
       
       
#ROCK
       if selection == 1: 
          
          screen.blit(rock_scale_down, (50,70)) #user choice
          # number is a random int between 1 - 3 each number has corresponding action
          if number == 1:
           screen.blit(rock_scale_down, (500,70))
          elif number == 2:
           screen.blit(paper_scale_down, (500,70))
          else:
           screen.blit(scissor_scale_down, (500,70))
#Paper
       if selection == 2:
          screen.blit(paper_scale_down, (50,70))

          if number == 1:
           screen.blit(rock_scale_down, (500,70))
          elif number == 2:
           screen.blit(paper_scale_down, (500,70))
          else:
           screen.blit(scissor_scale_down, (500,70))
#scissor
       if selection == 3:
          screen.blit(scissor_scale_down, (50,70))
          
          if number == 1:
           screen.blit(rock_scale_down, (500,70))
          elif number == 2:
           screen.blit(paper_scale_down, (500,70))
          else:
           screen.blit(scissor_scale_down, (500,70))
          
#ROCK CHOICES
          
       if selection == 1 and number == 2:
         lose_outcome.draw()
       elif selection == 1 and number == 3:
         win_outcome.draw()

       elif selection == 1 and number == 1:
         
         draw_outcome.draw()
       

#PAPER CHOICES

       if selection == 2 and number == 2:
          
          draw_outcome.draw()
       elif selection == 2 and number == 1:
         win_outcome.draw()
       elif selection == 2 and number == 3:
         lose_outcome.draw()

#SCISSOR CHOICES           
       if selection == 3 and number == 3:
          
          draw_outcome.draw()
          
       elif selection == 3 and number == 1:
         lose_outcome.draw()
       elif selection == 3 and number == 2:
         win_outcome.draw()

       for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          pygame.display.update()
   
def select():
   
   while True:
       screen.blit(background, (0,0))
       choice.draw()
       
       
# DO WHAT EVER IF USER CLICKS ROCK
       if rock_button.draw() == True:
          pygame.display.update()
          selection = 1
          outcomes(selection)
          return selection
          
       
          
          

       if paper_button.draw() == True:
          pygame.display.update()
          selection = 2
          outcomes(selection)
          
          
          return selection
          
       if scissor_button.draw() == True:
          pygame.display.update()
          selection = 3
          outcomes(selection)
          
          
          return selection
       

       for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       pygame.display.update()



   

def main_menu():
    

    while True:
       
       screen.blit(background, (0,0))
       title.draw()
       # IF PLAY BUTTON IS CLICKED DO...
       if play_button.draw() == True:
          # PLAY BUTTON STUFF
          select()

       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       pygame.display.update()

   
if __name__ == '__main__':
   main_menu()
   

