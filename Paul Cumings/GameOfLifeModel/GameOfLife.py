"""
Drawing representation of Conway's Game of Life in NodeBox.
  http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

 

"""

##
class World(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.cells = []
        
        # Change these to increase/decrease the number of cells in the animation
        self.rows = 25
        self.cols = 25

        self.grid_width = self.width / self.cols
        self.grid_height = self.height / self.rows
        
        self.cell_width = self.grid_width - 1
        self.cell_height = self.grid_height - 1

        # Init cells with 0's or 1's to seed the world
        for i in range(0, self.rows):
            self.cells.append([])
            for x in range(0, self.cols):
                # Here's the magic ratio of 0 vs 1 cell defaults
                if random(10) > 8:
                    val = 1
                else:
                    val = 0
                
                self.cells[i].append(val)


    def is_lit(self, x, y):
        return self.cells[x][y]
    
    def update(self):
        # Iterate over the 2D cells data structure and apply the Conway's Game of Life rules to each cell
        for x in range(0, len(self.cells)):
            for y in range(0, len(self.cells[x])):
                # ...count the number of neighbor cells that are active...
                nsum = 0
                
                try:
                    nsum += self.cells[x-1][y-1]
                except IndexError:
                    pass
                
                try:
                    nsum += self.cells[x-1][y]
                except IndexError:
                    pass
                
                try:
                    nsum += self.cells[x-1][y+1]
                except IndexError:
                    pass

                try:
                    nsum += self.cells[x][y-1]
                except IndexError:
                    pass
                
                try:
                    nsum += self.cells[x][y+1]
                except IndexError:
                    pass
                
                try:
                    nsum += self.cells[x+1][y-1]
                except IndexError:
                    pass
                
                try:
                    nsum += self.cells[x+1][y]
                except IndexError:
                    pass
                
                try:
                    nsum += self.cells[x+1][y+1]
                except IndexError:
                    pass
                
                # Cells with less then two neighbors die
                if nsum < 2:
                    self.cells[x][y] = 0
                    continue
                
                # Cells with exactly two neighbors continue unchanged
                if nsum == 2:
                    continue
                
                # Empty cells with three neighbords come to life
                if nsum == 3:
                    self.cells[x][y] = 1
                    continue
                
                # Cells with more then three neighbors die
                if nsum > 3:
                    self.cells[x][y] = 0
                    continue


# --
def draw():
    global w

    # Iterate over the drawing grid to fill in appropriate cells...
    for x, y in grid(w.rows, w.cols, w.grid_width, w.grid_height):
        # x and y are drawing coordiates. We can compute the grid
        # indexes by dividing them by the grid width and height 
        col = x / w.grid_width
        row = y / w.grid_height
        
        # Ask the world if this cell should be lit up...
        if w.is_lit(col, row):
            # Fill with a random, redish color
            fill(color(random(0.0, 1.0), 0.2, 0.2))
            rect(x, y, w. cell_width, w. cell_height, roundness=0.8)
    
    # Update the world (ie., apply rules for cell life)
    w.update()

# ------
# MAIN
# ------
width = 600
height = 600

size(width, height)
speed(50)

w = World(width, height)
