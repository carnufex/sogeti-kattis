import math

## Required to plot ###
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

class Vector:
    def __init__(self, point, vector):
        t = 0
        while True:
            t += 1
            x1 = t * vector[0]
            y1 = t * vector[1]
            z1 = t * vector[2]
            
            if x1 > 10 or x1 < -10 or y1 > 10 or y1 < -10 or z1 < 0 or z1 > 10:
                self.vector = (x1, y1, z1)
                break

        self.point = point
    
    def find_terminal_point(self):
        # vector = terminal - initial, terminal = vecto + initial
        return tuple(map(sum, zip(self.vector, self.point)))
    
    def start_point(self):
        return self.point


class Baloon:
    def __init__(self, r, x, y, z):
        self.r = r
        self.x = x
        self.y = y
        self.z = z
        self.popped = False


    def calculate_intersection(self, x, y, z, vx, vy, vz):
        a = vx**2 + vy**2 + vz**2
        b = 2 * (vx*(x-self.x)+ vy*(y-self.y)+vz*(z-self.z))
        c = (x-self.x)**2 + (y-self.y)**2 + (z-self.z)**2 - self.r**2
        d = b**2 - 4*a*c

        if d > 0:
            solution1 = ((-1)*b-math.sqrt(d))/(2*a)
            solution2 = ((-1)*b+math.sqrt(d))/(2*a)
            # negative solution is behind the gun
            if solution1 >= 0 or solution2 >= 0:
                return True
        return False

        if d < 0:
            # no real solutions
            return False
        return True


def list_as_new_line_stings(input: list):
    return "\n".join([str(i) for i in input])


def read_input():
    """
    Reads all input to list
    """
    data = []
    while True:
        try:
            val = input()
            data.append(val)
            if val == '0':
                break
        except EOFError:
            break

    return data

def toggle(inp: str):
    return 'b' if inp == 's' else 's'

def parse_input():
    """
    Parsing the input without a scanner.
    """
    baloon_or_shot = 's'

    inp = read_input()
    output = []
    baloons = []
    shots = []
    for item in inp: # offset ending 0
        item = item.split()
        if len(item) == 1:
            if item[0] == '0':
                output.append((baloons, shots))
                break
            if baloon_or_shot == 's':
                output.append((baloons, shots))
                baloons = []
                shots = []

            baloon_or_shot = toggle(baloon_or_shot)  
            continue
        if baloon_or_shot == 'b':
            # r, l, x, y
            baloons.append(Baloon(float(item[0]), float(item[2]), float(item[3]), float(item[0]) + float(item[1])))

        if baloon_or_shot == 's':
            # px, py, pz, vx, vy, vz
            shots.append(Vector((float(item[0]), float(item[1]), float(item[2])), (float(item[3]), float(item[4]), float(item[5]))))

    return output[1:] # offset the first empty iteration

def plot(baloons, shots):
    """
    Plots baloon and shots
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(0, 10)
    
    for baloon in baloons:
        # draw sphere
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = baloon.r*np.outer(np.cos(u), np.sin(v))
        y = baloon.r*np.outer(np.sin(u), np.sin(v))
        z = baloon.r*np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x+baloon.x, y+baloon.y, z+baloon.z, color=np.random.choice(['g','b']), alpha=0.5*np.random.random()+0.5)

    for shot in shots:
        ax.quiver(shot.point[0], shot.point[1], shot.point[2], shot.vector[0], shot.vector[1], shot.vector[2])
        
    plt.show() 


def problem_e():
    intersections = []
    baloon_shot_tuples = parse_input()
    for tup in baloon_shot_tuples:
        baloons = tup[0]
        shots = tup[1]

        # check if each shot penetrates any baloons
        for shot in shots:
            end_point = shot.find_terminal_point()
            x1 = end_point[0]
            y1 = end_point[1]
            z1 = end_point[2]

            start_point = shot.start_point()
            x0 = start_point[0]
            y0 = start_point[1]
            z0 = start_point[2]

            intersection_count = 0

            for baloon in baloons:
                intersects = baloon.calculate_intersection(x0, y0, z0, shot.vector[0], shot.vector[1], shot.vector[2])
                if intersects and not baloon.popped:
                    intersection_count += 1
                    baloon.popped = True

            intersections.append(intersection_count)
        break
    plot(baloons, shots)

    return intersections

        
if __name__ == "__main__":
    print(list_as_new_line_stings(problem_e()))

