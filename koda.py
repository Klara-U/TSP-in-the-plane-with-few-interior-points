import sys
import math
import random
import matplotlib.pyplot as plt
import random
from shapely.affinity import affine_transform
from shapely.geometry import Point, Polygon
from shapely.ops import triangulate

# vmesna funkcija, ki random razdeli seznam na dva seznama
def random_partition(a):
    b = list()
    c = list()
    for i in range(len(a)):
        if random.randrange(2):
            b.append(a[i])
        else:
            c.append(a[i])
    return b,c

# funkcija, ki nam generira random seznam n stevil in jih uredi
def get_deltas(n):
    # generiramo n stevil
    de = [random.random() for _ in range(n)]
    # jih uredimo
    de.sort()
    #razdelimo brez prvega in zadnjega z random particijo na dva seznama
    dep, dem = random_partition(de[1:-1])
    # drugemu seznamu obrnemo vrstni red
    dem.reverse()
    # seznam = prvi element + prva particija + zadnji + druga particija + prvi
    des = [de[0]] + dep + [de[-1]] + dem + [de[0]]
    # naredimo vektor razdalj med elementi
    deltas = [des[i] - des[i-1] for i in range(1, len(des))]
    # vrnemo vektor razdalj, prvi in zadnji element
    return deltas, (de[0], de[-1])

def get_xyq(n):
    # dobimo razdalje, x, y, ter prve in zadnje koordinate
    x, (a1, a2) = get_deltas(n)
    y, (b1, b2) = get_deltas(n)
    # random zmesamo y
    random.shuffle(y)
    # damo skupaj razdalje, da dobimo usmerjene vektorje v ravnini
    vectors = [(x[i], y[i]) for i in range(n)]
    vectors.sort(key=lambda v: math.atan2(v[1], v[0]))
    points = [(0, 0)]
    for v in vectors:
        points.append((points[-1][0] + v[0], points[-1][1] + v[1]))
    xmin = min([p[0] for p in points])
    ymin = min([p[1] for p in points])
    dx = a1 - xmin
    dy = b1 - ymin
    points = [(p[0]+dx, p[1]+dy) for p in points]
    return points

# funkcija, ki random izbere k tock znotraj poligona
def random_points_in_polygon(polygon, k):
    areas = []
    transforms = []
    for t in triangulate(polygon):
        areas.append(t.area)
        (x0, y0), (x1, y1), (x2, y2),_ = t.exterior.coords
        transforms.append([x1 - x0, x2 - x0, y2 - y0, y1 - y0, x0, y0])
    tocke = []
    for transform in random.choices(transforms, weights=areas, k=k):
        x, y = [random.random() for _ in range(2)]
        if x + y > 1:
            p = Point(1 - x, 1 - y)
        else:
            p = Point(x, y)
        tocke.append(affine_transform(p, transform))
    return tocke



if __name__ == "__main__":
    n = 10

    k = 1
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    points = get_xyq(n)
    polygon = Polygon(points)
    tocke = random_points_in_polygon(polygon,k)
    plt.plot([p[0] for p in points], [p[1] for p in points])
    plt.show()
    print("Zunanje tocke", points)
    print(tocke)