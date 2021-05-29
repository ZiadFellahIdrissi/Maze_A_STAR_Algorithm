from game2dboard import Board

import numpy as np  

maze =  np.random.randint(2, size=(2, 3))
print(maze)
b = Board(2,3)
b[0][0] = "start"
b[0][0] = "ziad"

b.title = "Maze"
b.margin = 1
b.cell_size = 50
b.cell_color = "bisque"
b.create_output(background_color="wheat4", color="white")
b.print("cliquer sur 'S' pour savoir le chemin")
b.show()