import numpy as np

def draw_obb(ax, obb, color="red"):
    corners = np.asarray(obb.get_box_points())

    edges = [
        (0,1),(1,3),(3,2),(2,0),
        (4,5),(5,7),(7,6),(6,4),
        (0,4),(1,5),(2,6),(3,7)
    ]

    for e in edges:
        p1, p2 = corners[e[0]], corners[e[1]]
        ax.plot(
            [p1[0], p2[0]],
            [p1[1], p2[1]],
            [p1[2], p2[2]],
            color=color
        )
