import os
import numpy as np


def save_point_cloud(path, points, colors):
    """Save a point cloud to a PLY file.

    Args:
        path (str): output file path.
        points (array-like): (N, 3) array of XYZ coordinates.
        colors (array-like): (N, 3) array of RGB values in [0, 1].
    """
    pts = np.asarray(points).reshape(-1, 3)
    cols = np.asarray(colors).reshape(-1, 3)
    cols = np.clip(cols, 0.0, 1.0)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write('ply\n')
        f.write('format ascii 1.0\n')
        f.write(f'element vertex {len(pts)}\n')
        f.write('property float x\n')
        f.write('property float y\n')
        f.write('property float z\n')
        f.write('property float red\n')
        f.write('property float green\n')
        f.write('property float blue\n')
        f.write('end_header\n')
        for p, c in zip(pts, cols):
            f.write(f'{p[0]} {p[1]} {p[2]} {c[0]} {c[1]} {c[2]}\n')

