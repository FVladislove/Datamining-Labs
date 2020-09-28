from typing import List
import math


class Dot:
    def __init__(self, *params):
        self.dimensions: list = list(params)

    def calculate_distance(self, another_dot):
        if (diff := len(another_dot.dimensions) - len(self.dimensions)) > 0:
            self.add_dimensions(diff)
        elif diff < 0:
            another_dot.add_dimensions(math.fabs(diff))

        return math.sqrt(sum(map(lambda x, y: (x - y) ** 2, self.dimensions, another_dot.dimensions)))

    def add_dimensions(self, num_of_dimensions):
        while num_of_dimensions != 0:
            self.dimensions.append(0.0)
            num_of_dimensions -= 1

    def __str__(self):
        return str(self.dimensions)


def calculate_middle_dot(dots: List[Dot]):
    coords = [0.0] * len(dots[0].dimensions)
    for dot in dots:
        if (diff := len(dot.dimensions) - len(coords)) > 0:
            while diff != 0:
                coords.append(0)
                diff -= 1
        for dimension in range(len(dot.dimensions)):
            coords[dimension] += dot.dimensions[dimension]
    count_of_dots = len(dots)
    for dimension in range(len(coords)):
        coords[dimension] = coords[dimension] / count_of_dots
    return Dot(*coords)


def calculate_cluster_radius(middle_dot: Dot, cluster_dots: List[Dot]):
    radius = 0
    for dot in cluster_dots:
        if (new_radius := middle_dot.calculate_distance(dot)) > radius:
            radius = new_radius
    return radius


def main():
    cluster1 = [
        Dot(2, 2),
        Dot(2, 3),
        Dot(3, 2),
        Dot(3, 3),
        Dot(4, 4),
    ]
    cluster2 = [
        Dot(7, 9),
        Dot(8, 7),
        Dot(8, 8),
        Dot(9, 9),
        Dot(10, 10),
    ]
    first_cluster_middle_dot = calculate_middle_dot(cluster1)
    second_cluster_middle_dot = calculate_middle_dot(cluster2)

    first_cluster_radius = calculate_cluster_radius(first_cluster_middle_dot, cluster1)
    second_cluster_radius = calculate_cluster_radius(second_cluster_middle_dot, cluster2)

    print(f"First cluster middle dot  : {first_cluster_middle_dot}\n"
          f"First cluster radius      : {first_cluster_radius}\n"
          f"Second cluster middle dot : {second_cluster_middle_dot}\n"
          f"Second cluster radius     : {second_cluster_radius}\n")


if __name__ == '__main__':
    main()
