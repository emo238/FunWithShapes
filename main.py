import tools
import numpy as np

#%% Testing with a simple triangle

#triangle = tools.build_triangle()

#tools.build_triangles_in_triangle(triangle, 30)

#%% Testing shape with a number of points

#shape = tools.build_random_shape(5)

#tools.build_shapes_in_shape(shape, 50, 0.1)

#%% Trying to use the whole frame 

points = tools.generates_random_points(10)

triangles = tools.generates_triangles_from_points(points, True)

shapes = []

for triangle in triangles :
    shapes.append(tools.build_shapes_in_shape(triangle, 30))
    
tools.draw_picture(shapes, True)
    
    