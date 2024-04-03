import matplotlib.pyplot as plt
import numpy as np
import random

def draw_triangle(triangle):
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))

    ax.plot(triangle[[-1,0],0], triangle[[-1,0],1], 'b-o')
    ax.plot(triangle[:,0], triangle[:, 1], 'b-o')

    ax.set_ylim(bottom=0, top=1)
    ax.set_xlim(left=0, right=1)
    ax.set_title("This is a triangle")
    plt.show()
    return 0

def draw_triangles(triangles):
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))

    for triangle in triangles:
        ax.plot(triangle[[-1,0],0], triangle[[-1,0],1], 'b-')
        ax.plot(triangle[:,0], triangle[:, 1], 'b-o')

    ax.set_ylim(bottom=0, top=1)
    ax.set_xlim(left=0, right=1)
    ax.set_title("This is a triangle")
    plt.show()
    return 0

def triangle_area(triangle):
    sides_length = []
    for i in range(3):
        if i==2:
            side_vector = triangle[i] -triangle[0]
        else:
            side_vector = triangle[i] - triangle[i+1]
        sides_length.append(np.linalg.norm(side_vector))
    s = sum(sides_length)
    area = np.sqrt(s*(s-sides_length[0])*(s-sides_length[1])*(s-sides_length[2]))
    return area

def build_triangle(show=False):
    A = np.array([random.random(), random.random()])
    B = np.array([random.random(), random.random()])
    C = np.array([random.random(), random.random()])
    triangle = np.array([A,B,C])
    area = triangle_area(triangle)
    while area < 3:
        triangle = build_triangle(show)
        area = triangle_area(triangle)
    if show:
        draw_triangle(triangle)
    return triangle

def build_triangles_in_triangle(triangle, n):
    percentage=-0.1
    triangles = [triangle]
    number_of_points = len(triangle)

    for i in range(n):
        new_triangle = []
        for j in range(number_of_points):
            if j==number_of_points-1:
                vector = triangles[i][j]-triangles[i][0]
            else:
                vector = triangles[i][j]-triangles[i][j+1]
            
            translation_vector = vector*percentage
            new_point = triangles[i][j] + translation_vector
            new_triangle.append(new_point)

        new_triangle = np.array(new_triangle)
        triangles.append(new_triangle)
    draw_triangles(triangles)
    