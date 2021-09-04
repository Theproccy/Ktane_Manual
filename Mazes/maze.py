import json
import os
import pygame
pygame.init()


def maze_gen():
    """takes in put from the user and returns a map

    Returns:
        dict: the json file containing all the maps 
    """
    res = {}
    for i in range(9):  # for each of the mazes (9)
        print("this is maze ", i+1)

        Green_1 = []
        Green_2 = []
        Green_1.append([int((inp := input(
            "The Position of the first circle given in the format x,y :"))[0]), int(inp[-1])])
        Green_2.append([int((inp := input(
            "The Position of the second circle given in the format x,y :"))[0]), int(inp[-1])])
        horizontal_wall = []
        vertical_wall = []

        for y in range(5):  # for each x (5) because there are only 5 rows of horizontal walls
            horizontal_wall.append([])
            for x in range(6):  # for each y (6)
                # horizontal_wall[y].append(bool(1))
                horizontal_wall[y].append(
                    bool(input(f"is there a horizontal wall under {x +1, y+1}")))

        for y in range(6):  # for each x (6)
            vertical_wall.append([])
            for x in range(5):   # for each x (5) because there are only 5 columns  of vertical walls
                # vertical_wall[y].append(bool(1))
                vertical_wall[y].append(
                    bool(input(f"is there a vertical wall to the right of {x+1 , y+1}")))  # adding 1 to x and y so as the
                # range start with 0 but we use 1

        res[str(i+1)] = {
            "Green_circle_1": Green_1,
            "Green_circle_2": Green_2,
            "horizontal_wall": horizontal_wall,
            "vertical_wall": vertical_wall}
    return res


def save_data(data: dict) -> None:
    """takes a dict objects and saves it as json file in ./data.json

    Args:
        data (dict): the data u want to save in ./data.json file

    Returns:
        None    
    """
    with open(__file__[:-1*len(os.path.basename(__file__))]+"data.json", "w") as f:
        return json.dump(data, f, indent=4)


def load_data() -> dict:
    """loads in ./data.json file

    Returns:
        dict: the data.json in dict type
    """
    with open(__file__[:-1*len(os.path.basename(__file__))]+"data.json",) as f:
        data = json.load(f)
    return data


#res = maze_gen()
#print(res)
#save_data(res)
#print(load_data())


class Maze:
    def __init__(self, data: dict, window):
        """creates a maze using the data given

        Args:
            data (dict): a dict which includes Green circle, horizontal wall,vertical wall
            window (pygame.screen): the screen to display the maze
        """

        self.SQUARE_SIZE = 100
        # list of green Circles with x,y cords
        self.Green_circle = [*data["Green_circle_1"], *data["Green_circle_2"]]
        # list of horizontal walls [[True,False,...],[True,True,...]...]
        self.horizontal_wall = data["horizontal_wall"]
        # list of vertical walls [[True,False,...],[True,True,...]...]
        self.vertical_wall = data["vertical_wall"]
        self.screen = window  # pygame scree to draw and do stuff

        # loop through every side and it there is a wall i draws that
        for y, row in enumerate(self.vertical_wall):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_vertical_wall(x+1, y)
        for y, row in enumerate(self.horizontal_wall):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_horizontal_wall(x, y+1)

        self.draw_circle()

    def draw_vertical_wall(self, x: int, y: int) -> None:
        """draws the vertical walls of maze

        Args:
            x (int): x codtinate of the wall
            y (int): y codtinate of the wall
        """
        pygame.draw.line(self.screen, (0, 0, 0),
                         (x * 100, y * 100), (x * 100, (y + 1) * 100))

    def draw_horizontal_wall(self, x: int, y: int) -> None:
        """draws the horizontal walls of maze

        Args:
            x (int): x codtinate of the wall
            y (int): y codtinate of the wall
        """
        pygame.draw.line(self.screen, (0, 0, 0),
                         (x * 100, y * 100), ((x + 1) * 100, y * 100))

    def draw_circle(self) -> None:
        """draws the 2 green circle of the maze
        """
        pygame.draw.circle(self.screen, (20, 200, 20),
                           (self.Green_circle[0][0]*100-50, self.Green_circle[0][1]*100-50), 25)
        pygame.draw.circle(self.screen, (20, 200, 20),
                           (self.Green_circle[1][0]*100-50, self.Green_circle[1][1]*100-50), 25)


#HEIGHT = 600
#WIDTH = 600
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
#clock = pygame.time.Clock()
#screen.fill((255, 255, 255))
## loads and creates the first make the maze
#maze_1 = Maze(load_data()["1"], screen)
#pygame.display.update()

""" 
basic code to keep the pygame screen running until u stop it
"""
#run = True
#while run:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            run = False
#    clock.tick(5)
