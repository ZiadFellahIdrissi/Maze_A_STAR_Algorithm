from game2dboard import Board
import math as ma
from tqdm import tqdm
# from node import Node


class Node():
    """Une classe de noeuds"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):

    # Création d'un nœud de début et de fin
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # nitialiser les deux listes
    open_list = []
    closed_list = []  # liste des noeuds qui sont déjà traité

    # Ajouter le nœud de départ
    open_list.append(start_node)
    outer_iteration = 0
    max_iteration = (len(maze) // 2) ** 10

    # Loop until you find the end
    # pbar = tqdm(total=len(open_list))
    while len(open_list) > 0:
        # pbar.update(1)

        # Get the current node
        current_node = open_list[0]
        outer_iteration += 1
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        if outer_iteration > max_iteration:
            print(outer_iteration)
            return [(0, 0)]

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        movement = [
            [-1, 0],  # up
            [0, -1],  # left
            [1, 0],   # down
            [0, 1]    # right
        ]
        # Generate children
        children = []
        # Adjacent squares
        for new_position in movement:

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if len([vis for vis in closed_list if vis == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = abs(child.position[0] - end_node.position[0]) + \
                abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h

            # Child is already in the open list
            if len([i for i in open_list if i == child and child.g > i.g]) > 0:
                continue

            # Add the child to the open list
            open_list.append(child)

    # pbar.close()


def fnkbd(key):
    if key == "s":
        draw_path()
    if key == "a":
        setup()


def mouse_fn(btn, row, col):
    if b[row][col] != "start" and b[row][col] != "end":
        if b[row][col] == 'obstacle':
            b[row][col] = 'normal'
            maze[row][col] = 0
        else:
            b[row][col] = 'obstacle'
            maze[row][col] = 1


def setup():
    width = len(maze)
    height = len(maze[0])
    b = Board(width, height)
    b[start[0]][start[1]] = 'start'
    b[end[0]][end[1]] = 'end'
    for i in range(width):
        for j in range(height):
            if maze[i][j]:
                b[i][j] = 'obstacle'
    return b


def draw_path():
    path = astar(maze, start, end)
    if path == None:
        b.print("N'a pas de chemin")
        return
    for i in path[1:-1]:
        b[i[0]][i[1]] = "body"


if __name__ == "__main__":

    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
            [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
    start = (0, 0)
    end = (4,0)

    b = setup()
    b.title = "Maze"
    b.margin = 1
    b.cell_size = 50
    b.cell_color = "bisque"
    b.on_key_press = fnkbd
    b.on_mouse_click = mouse_fn
    b.create_output(background_color="wheat4", color="white")
    b.print("cliquer sur 'S' pour savoir le chemin")
    b.show()
