import open3d as o3d
import numpy as np

def analyze_mesh(path):
    mesh = o3d.io.read_triangle_mesh(path)
    obb = mesh.get_oriented_bounding_box()
    dims = obb.extent
    volume = np.prod(dims)

    return mesh, obb, dims, volume
