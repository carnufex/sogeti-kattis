from queue import PriorityQueue

def wanna_be_dijkstra(matrix, r, c):
    """ 
    Finds the path with least mud depth
    """
    queue = PriorityQueue()
    inf = 1000001

    # spawn cost matrix populated by max values
    costs = [[inf for x in range(c+2)] for y in range(r)] 
    
    # loop to check all directions
    dx = [1, -1, 0, 0] #right, left, up, down
    dy = [0, 0, 1, -1]

    # start
    queue.put((0,0,0))
    costs[0][0] = 0

    while not queue.empty():
        tup = queue.get() 
        cost = tup[0]
        x = tup[1]
        y = tup[2]
        
        # loops all directions from dx, dy
        for diff_x, diff_y in zip(dx, dy):
            next_x = x + diff_x
            next_y = y + diff_y

            if (next_x >= 0 and next_y >= 0 and next_x < r and next_y < c + 2):
                next_cost = max(costs[x][y], matrix[next_x][next_y])
                if (next_cost < costs[next_x][next_y]):
                    costs[next_x][next_y] = next_cost
                    queue.put((next_cost, next_x, next_y))

    return costs[0][c+1]


def list_as_new_line_stings(input: list):
    return "\n".join([str(i) for i in input])

def read_input():
    """
    Reads all input to list
    """
    text = input()
    yx = text.split()
    y = int(yx[0])
    data = []
    while y > 0:
        try:
            val = input()
            data.append(val)
        except EOFError:
            break
        y -= 1

    return data, yx

def parse_input():
    """
    Parsing the input without a scanner.
    """
    inp, yx = read_input()
    output = []

    for line in inp:
        line = line.split()
        col = [-1]
        for item in line:
            col.append(int(item))
        col.append(-1)
        output.append(col)
    
    return output, yx


def problem_f():
    matrix, yx_tup = parse_input()
    return wanna_be_dijkstra(matrix, int(yx_tup[0]), int(yx_tup[1]))

        
if __name__ == "__main__":
    print(problem_f())

