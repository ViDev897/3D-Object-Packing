import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from src.mesh_analysis import analyze_mesh
from src.obb_visualization import draw_obb
from src.bin_packing import pack_items
from src.visualize_packing import draw_box

# ---------- Mesh Analysis ----------
mesh_files = ["data/CUBE.obj", "data/CYLINDER.obj", "data/TEAPOT.obj"]

for path in mesh_files:
    mesh, obb, dims, volume = analyze_mesh(path)

    print(f"\nFile: {path}")
    print(f"Dimensions: {dims}")
    print(f"Volume: {volume:.2f}")

    vertices = np.asarray(mesh.vertices)

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], s=1, alpha=0.5)
    draw_obb(ax, obb)
    plt.show()

# ---------- Bin Packing ----------
with open("data/items.json") as f:
    items = json.load(f)

items = sorted(items, key=lambda x: np.prod(x["dims"]), reverse=True)
placed_items = pack_items(items)

# ---------- Visualization ----------
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection="3d")

ax.set_xlim(0,100)
ax.set_ylim(0,100)
ax.set_zlim(0,100)

for item in placed_items:
    draw_box(ax, item["pos"], item["dims"])

plt.show()
