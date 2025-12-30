import numpy as np

MASTER_BOX = np.array([100, 100, 100])

def pack_items(items):
    placed_items = []

    def is_overlap(pos, dims):
        x,y,z = pos
        dx,dy,dz = dims

        for item in placed_items:
            ix,iy,iz = item["pos"]
            idx,idy,idz = item["dims"]

            if not (x+dx <= ix or ix+idx <= x or
                    y+dy <= iy or iy+idy <= y or
                    z+dz <= iz or iz+idz <= z):
                return True
        return False

    def is_supported(pos, dims):
        if pos[2] == 0:
            return True

        for item in placed_items:
            ix,iy,iz = item["pos"]
            idx,idy,idz = item["dims"]

            if (pos[2] == iz + item["pos"][2] and
                pos[0] < ix + idx and pos[0] + dims[0] > ix and
                pos[1] < iy + idy and pos[1] + dims[1] > iy):
                return True
        return False

    for item in items:
        dx,dy,dz = item["dims"]
        placed = False

        for z in range(0, 100):
            for y in range(0, 100):
                for x in range(0, 100):
                    if x+dx > 100 or y+dy > 100 or z+dz > 100:
                        continue

                    pos = (x,y,z)
                    if not is_overlap(pos, item["dims"]) and is_supported(pos, item["dims"]):
                        placed_items.append({
                            "id": item["id"],
                            "dims": item["dims"],
                            "pos": pos
                        })
                        placed = True
                        break
                if placed: break
            if placed: break

    return placed_items
