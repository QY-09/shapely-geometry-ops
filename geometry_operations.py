"""
2D polygon boolean operation implement
created by: QY
"""
from shapely.geometry import Polygon
from shapely.ops import unary_union
import matplotlib.pyplot as plt

# Define two polygons
def create_polygon(coords,color):
    poly= Polygon(coords)
    x, y= poly.exterior.xy
    plt.fill(x,y,alpha=0.5, color=color)
    return poly

def main():
    coords_a = [(0, 0), (2, 0), (2, 2), (0, 2)]  # 正方形
    coords_b = [(1, 1), (3, 1), (3, 3), (1, 3), (0,2)]
    #coords_a=[(0,0),(3,1),(2,2),(0,1)]
    #coords_b=[(1,1),(3,1),(3,3),(2,3)]

    poly1=create_polygon(coords_a,'blue')
    poly2=create_polygon(coords_b,'red')
    plt.title('Original Polygons')
    plt.show()

    union=poly1.union(poly2)
    x,y=union.exterior.xy
    plt.fill(x,y, alpha=0.5, color='purple')
    plt.title('Union')
    plt.show()

    intersec= poly1.intersection(poly2)
    if not intersec.is_empty:
        x, y= intersec.exterior.xy
        plt.fill(x,y,alpha=0.5, color='yellow')
        plt.title('Intersection Area')
        plt.show()
    else:
        print('No intersection!')

if __name__ == "__main__":
    main()


