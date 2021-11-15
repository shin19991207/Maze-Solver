import sys

from typing import List


def BFS(start, maze) -> None:
    step = 0
    goal_reached = False
    q = {0: [start]}
    # Set shortest path length of start to 0
    maze[start[0]][start[1]]['path_length'] = 0
    # Set step size of start to 1
    maze[start[0]][start[1]]['step_size'][0] = 1
    while True:
        while step in q and len(q[step]) != 0:
            cur = q[step].pop(0)
            x = cur[0]
            y = cur[1]
            if maze[x][y]['color'] == 'goal':
                goal_reached = True
                break
            if maze[x][y]['color'] == 'r':
                maze[x][y]['step_size'][step] += 1
            elif maze[x][y]['color'] == 'y':
                maze[x][y]['step_size'][step] -= 1
            if maze[x][y]['step_size'][step] < 1:
                continue
            for direction in maze[x][y]['directions']:
                coor = direction_to_coordinate(direction)
                newx = x + coor[0] * maze[x][y]['step_size'][step]
                newy = y + coor[1] * maze[x][y]['step_size'][step]
                if newx < 0 or newy < 0 \
                        or newx >= len(maze) or newy >= len(maze) \
                        or cur in maze[newx][newy]['parents']['all']:
                    continue
                else:
                    if step + 1 in q:
                        q[step + 1].append((newx, newy))
                    else:
                        q[step + 1] = [(newx, newy)]
                    maze[newx][newy]['parents']['all'].append(cur)
                    maze[newx][newy]['parents'][step + 1] = cur
                    maze[newx][newy]['step_size'][step + 1] = \
                        maze[x][y]['step_size'][step]
                    if maze[newx][newy]['path_length'] > step + 1:
                        maze[newx][newy]['path_length'] = step + 1
        # if reached goal or there is no solution
        if goal_reached or step not in q:
            break
        else:
            step += 1


def direction_to_coordinate(direction: str) -> tuple:
    return {
        'r': (0, 1),
        'l': (0, -1),
        'u': (-1, 0),
        'd': (1, 0),
        'ur': (-1, 1),
        'dr': (1, 1),
        'ul': (-1, -1),
        'dl': (1, -1)
    }[direction]


def get_shortest_path_length(maze, goal) -> int:
    x = goal[0]
    y = goal[1]
    return maze[x][y]['path_length']


def get_shortest_path(maze, goal) -> List:
    path = [goal]
    total_step = maze[goal[0]][goal[1]]['path_length']
    curr = goal
    while total_step > 0:
        curr = maze[curr[0]][curr[1]]['parents'][total_step]
        path.insert(0, curr)
        total_step = total_step - 1
    return path


def get_path_str(path: List) -> str:
    path_str = ""
    for index in range(len(path) - 1):
        path_str += f'{path[index]}'
        path_str += " -> "
    path_str += f'{path[len(path) - 1]}'
    return path_str


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 Alice.py <inputfilename>")
        sys.exit()
    f = open(sys.argv[1])

    grid_size = int(f.readline())

    # start location
    s = f.readline().strip('s=()\n').split(',')
    s = (int(s[0]), int(s[1]))
    # goal location
    g = f.readline().strip('g=()\n').split(',')
    g = (int(g[0]), int(g[1]))
    # create maze matrix and store it to m
    m = []
    for i in range(grid_size):
        lst = f.readline().split()
        r = []
        for item in lst:
            vertex = {}
            cube_lst = item.split(':')
            vertex['color'] = cube_lst[0]
            vertex['path_length'] = sys.maxsize
            vertex['step_size'] = {}
            vertex['parents'] = {'all': []}
            if len(cube_lst) > 1:
                directions = cube_lst[1].strip('()\n').split(',')
                vertex['directions'] = directions
            r.append(vertex)
        m.append(r)

    BFS(s, m)

    shortest_path_length = get_shortest_path_length(m, g)
    if shortest_path_length == sys.maxsize:
        print("The maze has no solution.")
        exit(1)

    shortest_path = get_shortest_path(m, g)
    print(f'The shortest path length was {shortest_path_length} steps.')
    print(f'The path was {get_path_str(shortest_path)}.')
    exit(0)
