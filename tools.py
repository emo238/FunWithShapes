from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np
import itertools
import imageio
import shutil
import random
import math
import os

def draw_shape(shape):
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))

    ax.plot(shape[[-1,0],0], shape[[-1,0],1], 'b-')
    ax.plot(shape[:,0], shape[:, 1], 'b-')

    ax.set_ylim(bottom=0, top=1)
    ax.set_xlim(left=0, right=1)
    ax.set_title("This is a shape")
    plt.show()
    return 0

def draw_shapes(shapes):
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))

    for shape in shapes:
        ax.plot(shape[[-1,0],0], shape[[-1,0],1], 'b-')
        ax.plot(shape[:,0], shape[:, 1], 'b-')

    ax.set_ylim(bottom=0, top=1)
    ax.set_xlim(left=0, right=1)
    ax.set_title("This is a shape")
    plt.show()
    return 0

def clear_directory(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Remove each file
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Remove each directory
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def create_gif(image_folder, gif_name, duration=0.5):
    images = []
    # Get the list of image files
    file_names = sorted(os.listdir(image_folder), key=lambda x: int(x.split('_')[-1].split('.')[0]))

    # Load the images in forward order
    for filename in file_names:
        images.append(imageio.imread(os.path.join(image_folder, filename)))

    # Append the images in reverse order (except the first and the last)
    images.extend(reversed(images[1:-1]))

    # Save the gif
    imageio.mimsave(gif_name, images, duration=duration)

def draw_picture(list_shapes, gif = False):
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))
    n = len(list_shapes[0])
    for i in range(n):
        for shapes in list_shapes:
                ax.plot(shapes[i][[-1,0],0], shapes[i][[-1,0],1], 'b-')
                ax.plot(shapes[i][:,0], shapes[i][:, 1], 'b-')
        if gif:
            ax.set_ylim(bottom=0, top=1)
            ax.set_xlim(left=0, right=1)
            ax.set_title("This is a shape")
            plt.savefig(f'img/shape_snapshot_{i}.png')
    if gif: 
        create_gif("img", "gifs/warzazat.gif", 0.1)
        clear_directory("img")
    
    ax.set_ylim(bottom=0, top=1)
    ax.set_xlim(left=0, right=1)
    ax.set_title("This is a shape")
    plt.show()
    return 0

def polygon_area(points):
    # Ensure the points form a closed polygon by appending the first point at the end
    closed_points = np.vstack([points, points[0]])
    x = closed_points[:, 0]
    y = closed_points[:, 1]
    
    # Compute the area using the shoelace formula
    area = 0.5 * np.abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))
    return area

def build_triangle(show=False):
    A = np.array([random.random(), random.random()])
    B = np.array([random.random(), random.random()])
    C = np.array([random.random(), random.random()])
    triangle = np.array([A,B,C])
    area = polygon_area(triangle)
    if area < 0.3:
        triangle = build_triangle(False)
        area = polygon_area(triangle)
    
    if show:
        draw_shape(triangle)
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
    draw_shapes(triangles)

def build_random_shape(n_points, show=False):
    shape = np.array([np.array([random.random(), random.random()]) for _ in range(n_points)])

    hull = ConvexHull(shape)
    hull_points = shape[hull.vertices]

    area = polygon_area(hull_points)

    if area < 0.3 or len(hull_points) < n_points:
        return build_random_shape(n_points, show)
    
    if show:
        draw_shape(hull_points)

    return hull_points

def build_shapes_in_shape(shape, n, percentage = -0.1, show = False):
    if percentage > 0: 
        percentage = percentage * (-1)
    shapes = [shape]
    number_of_points = len(shape)

    for i in range(n):
        new_shape = []
        for j in range(number_of_points):
            if j==number_of_points-1:
                vector = shapes[i][j]-shapes[i][0]
            else:
                vector = shapes[i][j]-shapes[i][j+1]
            
            translation_vector = vector*percentage
            new_point = shapes[i][j] + translation_vector
            new_shape.append(new_point)

        new_shape = np.array(new_shape)
        shapes.append(new_shape)
    if show:
        draw_shapes(shapes)
    return shapes
    
def plot_points(points):
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))

    ax.plot(points[[-1,0],0], points[[-1,0],1], 'b-')
    ax.plot(points[:,0], points[:, 1], 'b-')

    ax.set_ylim(bottom=0, top=1)
    ax.set_xlim(left=0, right=1)
    ax.set_title("This is a shape")
    plt.show()
    return 0

def generates_random_points(n, show = False):
    points = [np.array([random.random(), random.random()]) for _ in range(n)]
    
    points.append(np.array([0,0]))
    points.append(np.array([0,1]))
    points.append(np.array([1,0]))
    points.append(np.array([1,1]))
    
    additional_side_points = math.floor(np.sqrt(n))-1
    step = 1/(additional_side_points+1)
    
    for i in range(additional_side_points):
        points.append(np.array([0,(i+1)*step]))
        points.append(np.array([1,(i+1)*step]))
        points.append(np.array([(i+1)*step,0]))
        points.append(np.array([(i+1)*step,1]))
    
    
    points = np.array(points)
    if show:
        plot_points(points)
    return points

def generates_triangles_from_points(points, show = False):
    triangulation = Delaunay(points)

    triangles = points[triangulation.simplices]
    
    if show:
        draw_shapes(triangles)
        
    return triangles


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    