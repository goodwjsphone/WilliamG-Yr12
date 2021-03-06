
 
import pygame
import random
import json
 
# -- Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255,0,0)
 
# Screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([5, 5])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
        width = 10
        height = 10
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):

        # enemy constructor
        super().__init__()
        height = 10
        width = 10


        self.image = pygame.Surface([width,height])
        self.image.fill(RED)

        self,rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

  #  def seek(self):
        
        #shortest path algrothim
 
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 


#wall opener algorithm



file = open("maze.JSON","r")

speed = 1

the = json.load(file)

print(the)

file.close()


for i in range (len(the)):
    for j in range (len(the[i])):
        if the[i][j] == 1:
            newwall = Wall(j*10,i*10)
            wall_list.add(newwall)
            all_sprite_list.add(newwall)










# Create the player paddle object
player = Player(10, 10)
player.walls = wall_list
 
all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
done = False
 
while not done:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-speed, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(speed, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -speed)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, speed)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(speed, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-speed, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, speed)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -speed)
            elif event.key ==  pygame.K_q:
                pygame.quit()
 
    all_sprite_list.update()
 
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
