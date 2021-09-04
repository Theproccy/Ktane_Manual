import maze
import pygame

which_maze = str(input("which maze wouuld you like to see"))

HEIGHT = 600
WIDTH = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
# loads and creates the first make the maze
maze_1 = maze.Maze(maze.load_data()[which_maze], screen)
pygame.display.update()

""" 
basic code to keep the pygame screen running until u stop it
"""
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(5)
