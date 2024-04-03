import matplotlib.pyplot as plt
import numpy as np
import random

def drawTriangle(triangle):
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))

    ax.plot(triangle[[-1,0],0], triangle[[-1,0],1], 'b-o')
    ax.plot(triangle[:,0], triangle[:, 1], 'b-o')

    ax.set_ylim(bottom=0, top=1)
    ax.set_xlim(left=0, right=1)
    ax.set_title("This is a triangle")
    plt.show()
    return 0


def build_triangle(show=False):
    A = np.array([random.random(), random.random()])
    B = np.array([random.random(), random.random()])
    C = np.array([random.random(), random.random()])
    triangle = np.array([A,B,C])
    if show:
        drawTriangle(triangle)
    return triangle