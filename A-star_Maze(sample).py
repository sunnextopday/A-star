import pygame
import sys
import A_star
from time import sleep

white = (255, 255, 255)
gold = (255, 204, 0)
green = (0, 255, 0)
dark_green = (0, 153, 0)
black = (0, 0, 0)

size = [800, 600]  # setup game size
box_size = 45  # setup box size
player_size = 20  # setup player size

start_point = (0, 1)  # start y,x
end_point = (9, 15)  # end y,x

maze_x = 17  # max maze x
maze_y = 11  # max maze y

make_maze = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
             [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

class MAZE:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(size)  # display setup
        pygame.display.set_caption('maze')  # caption setup
        pygame.display.set_icon(pygame.image.load('img/maze.png'))  # icon setup
        self.fps = pygame.time.Clock()  # fps setup

        self.player_x = 70  # pixcel x
        self.player_y = 20  # pixecl y

        self.x = start_point[1]  # real x
        self.y = start_point[0]  # real y

        self.font = pygame.font.SysFont("Arial", 40)  # font setup

        self.cnt = 0 # move count check
        self.path=[start_point,] # add move path

        self.maze()

    def maze(self):# draw maze
        mx = 0
        my = 0

        for i in range(0, maze_x * maze_y):
            if make_maze[my][mx] == 3:
                pygame.draw.rect(self.display, gold, (mx * box_size, my * box_size, box_size, box_size))
            if make_maze[my][mx] == 2:
                pygame.draw.rect(self.display, green, (mx * box_size, my * box_size, box_size, box_size))
            if make_maze[my][mx] == 1:
                pygame.draw.rect(self.display, white, (mx * box_size, my * box_size, box_size, box_size), 2)
            mx += 1
            if mx == maze_x:
                mx = 0
                my += 1

    def char(self): # setup character
        self.player = pygame.Rect(self.player_x, self.player_y, player_size, player_size)

    def move(self): # check the key press and move
        key = pygame.key.get_pressed()
        speed = 0.3

        if key[pygame.K_RIGHT]:  # move right
            if make_maze[self.y][self.x + 1] == 1:
                pass
            elif make_maze[self.y][self.x + 1] == 2:
                make_maze[self.y][self.x] = 0
                self.cnt -= 1
                pygame.draw.circle(self.display, green, (self.player_x, self.player_y), player_size)
                self.player_x += box_size
                self.x += 1
                sleep(speed)
            else:
                make_maze[self.y][self.x] = 2
                pygame.draw.circle(self.display, white, (self.player_x, self.player_y), player_size)
                self.player_x += box_size
                self.x += 1
                self.cnt += 1
                self.path.append((self.y,self.x))
                sleep(speed)

        elif key[pygame.K_LEFT]:  # move left
            if make_maze[self.y][self.x - 1] == 1:
                pass
            elif make_maze[self.y][self.x - 1] == 2:
                make_maze[self.y][self.x] = 0
                self.cnt -= 1
                pygame.draw.circle(self.display, green, (self.player_x, self.player_y), player_size)
                self.player_x -= box_size
                self.x -= 1
                sleep(speed)
            else:
                make_maze[self.y][self.x] = 2
                pygame.draw.circle(self.display, white, (self.player_x, self.player_y), player_size)
                self.player_x -= box_size
                self.x -= 1
                self.cnt += 1
                self.path.append((self.y, self.x))
                sleep(speed)

        elif key[pygame.K_UP]:  # move up
            if make_maze[self.y - 1][self.x] == 1:
                pass
            elif make_maze[self.y - 1][self.x] == 2:
                make_maze[self.y][self.x] = 0
                self.cnt -= 1
                pygame.draw.circle(self.display, green, (self.player_x, self.player_y), player_size)
                self.player_y -= box_size
                self.y -= 1
                sleep(speed)
            else:
                make_maze[self.y][self.x] = 2
                pygame.draw.circle(self.display, white, (self.player_x, self.player_y), player_size)
                self.player_y -= box_size
                self.y -= 1
                self.cnt += 1
                self.path.append((self.y, self.x))
                sleep(speed)

        elif key[pygame.K_DOWN]:  # move down
            if make_maze[self.y + 1][self.x] == 1:
                pass
            elif make_maze[self.y + 1][self.x] == 2:
                make_maze[self.y][self.x] = 0
                self.cnt -= 1
                pygame.draw.circle(self.display, green, (self.player_x, self.player_y), player_size)
                self.player_y += box_size
                self.y += 1
                sleep(speed)
            else:
                make_maze[self.y][self.x] = 2
                pygame.draw.circle(self.display, white, (self.player_x, self.player_y), player_size)
                self.player_y += box_size
                self.y += 1
                self.cnt += 1
                self.path.append((self.y, self.x))
                sleep(speed)

    def show(self): # display Move count string
        showcount = self.font.render("Move:" + str(self.cnt), False, gold)
        self.display.blit(showcount, (650, 500))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.fps.tick(30)
            self.display.fill(black)

            self.move()
            self.maze()
            self.char()
            self.show()

            pygame.draw.circle(self.display, green, (self.player.left, self.player.top), player_size)  # draw character
            pygame.draw.circle(self.display, dark_green, (self.player.left - 1, self.player.top - 1),player_size)  # draw gradation

            if self.x == end_point[1] and self.y == end_point[0]:
                print("도착!")
                print("도착지까지의 들은 비용은 : " + str(self.cnt))
                if self.cnt == answer:
                    print("\n최적의 경로 값입니다!")
                    print("A * 알고리즘이 찾은 경로는 : "+str(answer_path))
                    print("플레이어가 찾은 경로는 : "+str(self.path))
                else:
                    print("\n최적의 경로 값은 아닙니다...")
                sys.exit()

            if (self.x == start_point[1] and self.y == start_point[0]) and self.cnt > 0:  # draw last move point
                self.cnt = 0
                mx = 0
                my = 0
                for i in range(0, maze_x * maze_y):
                    if make_maze[my][mx] == 2:
                        make_maze[my][mx] = 0
                        pygame.draw.rect(self.display, white, (mx * box_size, my * box_size, box_size, box_size), 2)
                    mx += 1
                    if mx == maze_x:
                        mx = 0
                        my += 1

            pygame.display.flip()

if __name__ == "__main__":  # start main
    global answer_path , answer

    answer_path = A_star.main(make_maze,start_point,end_point) # a star 알고리즘 경로
    answer = len(A_star.main(make_maze,start_point,end_point)) -1 # a star 알고리즘 경로 길이 값
    MAZE().run()
