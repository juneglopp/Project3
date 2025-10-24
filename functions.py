# Topic 1

# Task 1:
import numpy as np


"""
Generate one random (x, y, z) point inside the simulation box.
    The point is drawn from a uniform distribution.
    
    Parameters:
    box_min : array-like 3 values
        Minimum coordinates [x_min, y_min, z_min] (in nm)
    box_max : array-like 3 values
        Maximum coordinates [x_max, y_max, z_max] (in nm)

    Returns:
    numpy.ndarray of shape 3
    -Random point [x, y, z] inside the box
"""

def random_point_in_box(box_min, box_max):
    point = np.random.uniform(box_min, box_max)
    return point

