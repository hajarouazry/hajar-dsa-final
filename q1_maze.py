import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random 

maze_image = plt.imread("maze.png")

print("Shape:", maze_image.shape)
print("Dtype:", maze_image.dtype)
print("Min:", maze_image.min())
print("Max:", maze_image.max())

grid = maze_image[5::10, 5::10, 0]
print("Grid shape:", grid.shape)

maze = (grid > 0.5).astype(int)
print(maze)

start = (0, 9)
exit_pos = (20, 11)

print("Start:", start, "Exit:", exit_pos)

choice = ""
while choice != "B" and choice != "L":
    choice = input('Which approach do you want? Type B for Backtracking or L for Las Vegas:').upper()

directions = [(1, 0), (0, 1), (0, -1), (-1,0)]
print("Directions:", directions)

def get_neighbours(position):
    row, col = position
    neighbours = []
    for dr, dc in directions: 
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 21 and 0 <= new_col < 21 and maze[new_row, new_col] == 1:
            neighbours.append((new_row, new_col))
    return neighbours 
print("Neighbours of start:", get_neighbours(start))

def backtracking():
    stack = [start]
    visited = {start}
    while len(stack) > 0 and stack[-1] != exit_pos:
        current = stack[-1]
        options = []
        for n in get_neighbours(current):
            if n not in visited:
                options.append(n)
        if len(options) > 0:
            next_square = options[0]
            stack.append(next_square)
            visited.add(next_square)
        else:
            stack.pop()
    success = len(stack) > 0 and stack[-1] == exit_pos
    return success, visited, stack 

def show_result(visited, path, title):
    picture = maze.copy()
    for r, c in visited:
        picture[r, c] = 2
    for r, c in path:
        picture[r, c] = 3
    picture[start] = 4 
    picture[exit_pos] = 4
    colours = ListedColormap(["black", "white", "lightblue", "red", "green"])
    plt.imshow(picture, cmap=colours, vmin=0, vmax=4)
    plt.title(title)
    plt.show()
    
def las_vegas():
    current = start
    visited = [start]
    steps = 0
    while steps < 200 and current != exit_pos:
        options = get_neighbours(current)
        if len(options) > 1 and previous in options:
            options.remove(previous)
        previous = current
        current = random.choice(options)
        visited.append(current)
        steps = steps + 1
    success = current == exit_pos
    return success, visited, steps 
   
if choice == "B":
    bt_success, bt_visited, bt_path = backtracking()
    print("Backtracking success:", bt_success, "Path length:", len(bt_path))
    show_result(bt_visited, bt_path, "Backtracking")
elif choice == "L":
    lv_success, lv_visited, lv_steps = las_vegas()
    print("Las Vegas success:", lv_success, "Steps:", lv_steps)
    show_result(lv_visited, lv_visited, "Las Vegas")
    
runs = 10000

bt_wins = 0
for i in range(runs):
    s, v, p = backtracking()
    if s:
        bt_wins = bt_wins + 1
        
lv_wins = 0
for i in range(runs):
    s, v, st = las_vegas()
    if s:
        lv_wins = lv_wins + 1

print("Backtracking success rate:", bt_wins / runs * 100, "%")
print("Las Vegas success rate:", lv_wins / runs * 100, "%")

    

            



    


        
        
    


    
