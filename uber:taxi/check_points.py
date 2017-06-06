def point_inside_polygon(x, y, poly):
    """
    A function determines if a given pair of (lon, lat) is inside a
    given polygon or not

    Parameter: x, longitude
               y, latitude
               polygon, a list of (x, y) pairs.

    Return: a boolean, whether a (x, y) inside the poly or not.
    """
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside