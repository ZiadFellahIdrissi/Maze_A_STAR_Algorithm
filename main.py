from game2dboard import Board
import numpy as np
from node import Node

start_node = None
end_node = None
maze = []
open_list = []
closed_list = []
movement = [
    [-1, 0],  # up
    [0, -1],  # left
    [1, 0],   # down
    [0, 1]    # right
]
start = (0, 0)
end = (2, 12)


def astar():

    # while len(open_list) > 0:
    if len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        current = current_node
        path = []
        while current is not None:
            path.append(current.position)
            current = current.parent
        path = path[::-1]
  

        if current_node == end_node:
            b.stop_timer()
            b.print("done")  # Return reversed path

        # Generate children
        children = []
        for new_position in movement:

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0 and maze[node_position[0]][node_position[1]] != 1:
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

        for i in open_list:
            b[i.position[0]][i.position[1]] = "open"

        for i in closed_list:
            b[i.position[0]][i.position[1]] = "close"
        
        for i in path:
            b[i[0]][i[1]] = "body"

    else:
        b.stop_timer()
        b.print("sorry noo way")


def fnkbd(key):
    if key == "s":
        b.start_timer(80)


def mouse_fn(btn, row, col):
    if b[row][col] != "start" and b[row][col] != "end":
        if b[row][col] == 'obstacle':
            b[row][col] = 'normal'
            maze[row][col] = 0
        else:
            b[row][col] = 'obstacle'
            maze[row][col] = 1


def setup(w, h):
    global start_node, end_node, open_list, maze

    # Création d'un nœud de Maze
    maze = np.random.randint(3, size=(w, h))
    maze[start[0]][start[1]] = 0
    maze[end[0]][end[1]] = 0

    b = Board(w, h)
    b[start[0]][start[1]] = 'start'
    b[end[0]][end[1]] = 'end'
    for i in range(w):
        for j in range(h):
            if maze[i][j] !=0 and maze[i][j] !=1:
                b[i][j] = 'obstacle'

    # Création d'un nœud de début et de fin
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list.append(start_node)
    return b


if __name__ == "__main__":

    b = setup(15, 30)
    b.title = "Maze"
    b.margin = 1
    b.cell_size = 30
    b.cell_color = "bisque"
    b.on_key_press = fnkbd
    b.on_mouse_click = mouse_fn
    b.on_timer = astar
    b.create_output(background_color="wheat4", color="white")
    b.print("cliquer sur 'S' pour savoir le chemin")
    b.show()