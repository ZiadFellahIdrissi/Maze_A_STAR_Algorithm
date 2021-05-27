from game2dboard import Board

maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0]]

b = Board(5,5)
b[0][0] = "start"
b[0][0] = "ziad"

b.title = "Maze"
b.margin = 1
b.cell_size = 50
b.cell_color = "bisque"
b.create_output(background_color="wheat4", color="white")
b.print("cliquer sur 'S' pour savoir le chemin")
b.show()