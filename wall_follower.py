from pyamaze import maze, agent, COLOR

DIRECTIONS = ['N', 'E', 'S', 'W']

def rotate_clockwise(direction):
    return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]

def rotate_counter_clockwise(direction):
    return DIRECTIONS[(DIRECTIONS.index(direction) - 1) % 4]


def move_forward(cell, direction):
    if direction == 'E':
        return (cell[0], cell[1] + 1), 'E'
    if direction == 'W':
        return (cell[0], cell[1] - 1), 'W'
    if direction == 'N':
        return (cell[0] - 1, cell[1]), 'N'
    if direction == 'S':
        return (cell[0] + 1, cell[1]), 'S'


def wall_follower(m):
    direction = 'N'
    curr_cell = (m.rows, m.cols)
    path = ''
    while curr_cell != (1, 1):
        if m.maze_map[curr_cell][rotate_counter_clockwise(direction)] == 0:
            if m.maze_map[curr_cell][direction] == 0:
                direction = rotate_clockwise(direction)
            else:
                curr_cell, d = move_forward(curr_cell, direction)
                path += d
        else:
            direction = rotate_counter_clockwise(direction)
            curr_cell, d = move_forward(curr_cell, direction)
            path += d
    return path.replace('EW', '').replace('WE', '').replace('NS', '').replace('SN', '')


if __name__ == '__main__':
    my_maze = maze(20, 30)
    my_maze.CreateMaze()
    b = agent(my_maze, shape='arrow', color=COLOR.cyan)
    path = wall_follower(my_maze)
    my_maze.tracePath({b: path})
    print(path)
    my_maze.run()
