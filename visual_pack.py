def draw_box(ax, pos, dims):
    x,y,z = pos
    dx,dy,dz = dims

    xx = [x, x+dx, x+dx, x, x]
    yy = [y, y, y+dy, y+dy, y]

    ax.plot(xx, yy, [z]*5)
    ax.plot(xx, yy, [z+dz]*5)

    for i in range(4):
        ax.plot([xx[i],xx[i]], [yy[i],yy[i]], [z,z+dz])
