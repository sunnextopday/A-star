import pygame
import sys
from time import sleep
white = (255,255,255)
green = (0,255,0)

size = [800, 600]

class MAZE:

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(size)
        pygame.display.set_caption('maze')
        self.fps = pygame.time.Clock()

        self.player_x = 30
        self.player_y = 10

        self.x = 0
        self.y = 1
        self.font = pygame.font.SysFont("Arial", 20)


    def maze(self):
        maze_x = 17
        maze_y = 11
        self.make_maze=[[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                       [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                       [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
                       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        start_point = (0, 1)
        end_point = (16, 10)

        mx = 0
        my = 0
        for i in range(0,maze_x*maze_y):
            if self.make_maze[my][mx] ==1:
                pygame.draw.rect(self.display, white, (mx*20, my*20, 20, 20),1)
            mx +=1
            if mx == maze_x:
                mx=0
                my+=1



    def char(self):
        self.player = pygame.Rect(self.player_x,self.player_y,10,10)

    def move(self):
        key=pygame.key.get_pressed()
        speed = 0.1

        if key[pygame.K_RIGHT]:
            if self.make_maze[self.x][self.y + 1] == 1:
                pass
            else:
                pygame.draw.circle(self.display,white,(self.player_x,self.player_y),10)
                self.player_x += 20
                self.y+=1
                sleep(speed)

        elif key[pygame.K_LEFT]:
            if self.make_maze[self.x][self.y - 1] == 1:
                pass
            else:
                pygame.draw.circle(self.display, white, (self.player_x, self.player_y), 10)
                self.player_x -= 20
                self.y-=1
                sleep(speed)

        elif key[pygame.K_UP]:
            if self.make_maze[self.x - 1][self.y] == 1:
                pass
            else:
                pygame.draw.circle(self.display, white, (self.player_x, self.player_y), 10)
                self.player_y -= 20
                self.x-=1
                sleep(speed)

        elif key[pygame.K_DOWN]:
            if self.make_maze[self.x + 1][self.y] == 1:
                pass
            else:
                pygame.draw.circle(self.display, white, (self.player_x, self.player_y), 10)
                self.player_y += 20
                self.x+=1
                sleep(speed)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.fps.tick(30)
            self.move()

            self.maze()
            self.char()

            pygame.draw.circle(self.display,green,(self.player.left,self.player.top),10)

            pygame.display.flip()

if __name__=="__main__":
    MAZE().run()
