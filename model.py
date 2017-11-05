"""
This File Define My Wy to Model The Data
"""
import unittest
class Edge(object):
    """
    Class for outer Points
    """

    def __init__(self, top=0, bottom=0, right=0, left=0):
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left

    @staticmethod
    def combine_edge(*edges):
        """
        Combine edges end find outer edge
        """
        new_edge = edges[0]  # get first edge
        for edge in edges:
            max_top = max([new_edge.top, edge.top])
            new_edge.top = max_top
            min_bottom = min([new_edge.bottom, edge.bottom])
            new_edge.bottom = min_bottom
            max_right = max([new_edge.right, edge.right])
            new_edge.right = max_right
            min_left = min([new_edge.left, edge.left])
            new_edge.left = min_left

        return new_edge

    def __str__(self):
        return "edge {} {} {} {}".format(self.top, self.bottom, self.right, self.left)

    def __eq__(self, other):
        return self.top == other.top and self.bottom == other.bottom and self.right == other.right and self.left == other.left


class Box(object):
    """
    Implementation Of A Box Region
    """

    def __init__(self):
        self.edge = Edge()

    def __update_edge(self, *new_edge):
        self.edge = Edge.combine_edge(self.edge, new_edge)

    def calculate_area(self):
        """
        Calculate Area Size
        """
        return abs(self.edge.right - self.edge.left) * abs(self.edge.top - self.edge.bottom)


class Point(Box):
    """
    Class For Point holding their coordinates
    """
    def __init__(self, x, y):
        Box.__init__()
        self.x = float(x)
        self.y = float(y)
        Box.__update_edge(self.edge, Edge(self.y, self.y, self.x, self.x))

    def __str__(self):
        return "position {} {}".format(self.x, self.y)


class Voronoi(Box):
    """
    Class For Region (Voronoi) holding an array for points
    Assume as a box area, to target MBR
    """

    def __init__(self, name=""):
        Box.__init__()
        self.name = name
        self.__points = []

    def __str__(self):
        return "voronoi {} has {} points".format(self.name, len(self.__points))

    def add_point(self, point):
        """Insert a point edge into voronoi"""
        self.__points.append(point)
        Box.__update_edge(self.edge, point.edge)

    def add_points(self, points):
        """Insert a points edge into voronoi"""
        self.__points.extend(points)
        Box.__update_edge(self.edge, [point.edge for point in points])  

class MBR(Box):
    """
    Class for MBR to store voronoi, Maximum content is N
    """
    MAXIMUM_CONTENT = 4

    def __init__(self):
        Box.__init__()
        self.content = list

    def content_size(self):
        """
        return content size
        """
        return len(self.content)

    def split_mbr(self, first, second):
        """asdasd"""
        pass

    def add(self, voronoi):
        """
        adding process to MBR
        """
        if (self.content_size + 1 < MBR.MAXIMUM_CONTENT):
            self.content.append(voronoi)
            voronoi_edges = voronoi.get_edge()
            Box.__update_edge(self.edge, voronoi_edges)
            return self  # returning current MBR
        
        else:  # splitting mbr into 2
            first = MBR()
            second = MBR()
            return self.split_mbr(first, second)

class TestModel(unittest.TestCase):
    """
    Unit testing for model.py
    """
    def test_edge(self):
        """Test case for edge model"""
        edge1 = Edge()
        edge2 = Edge(0, 0, 0, 0)
        self.assertEqual(edge1, edge2)
        edge3 = Edge(1, 2, 3, 4)
        edge4 = Edge.combine_edge(edge3)
        self.assertEqual(edge3, edge4)

    def test_box(self):
        """Test case for box model"""
        pass

if __name__ == '__main__':
    unittest.main()