"""
This File Define My Wy to Model The Data
"""


class Point(object):
    """
    Class For Point holding their coordinates
    """

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "position {} {}".format(self.x, self.y)


class Edge(object):
    """
    Class for outer Points
    """

    def __init__(self):
        self.top = 0
        self.bottom = 0
        self.left = 0
        self.right = 0

    @staticmethod
    def combine_edge(*edges):
        """
        Combine edges end find outer edge
        """
        new_edge = Edge()
        for edge in edges:
            if new_edge.top < edge.y:
                new_edge.top = edge.y
            if new_edge.bottom > edge.y:
                new_edge.bottom = edge.y
            if new_edge.left > edge.x:
                new_edge.left = edge.x
            if new_edge.right > edge.x:
                new_edge.right = edge.x
        
        return new_edge


class Box(object):
    """
    Implementation Of A Box Region
    """
    def __init__(self):
        self.edge = Edge()

    def __update_edge(self, new_edge):
        self.edge = Edge.combine_edge(self.edge, new_edge)
    
    def calculate_area(self):
        """
        Calculate Area Size
        """
        return abs(self.edge.right - self.edge.left) * abs(self.edge.top - self.edge.bottom)


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

        new_edge = Edge()
        new_edge.top = point.y
        new_edge.bottom = point.y
        new_edge.left = point.x
        new_edge.right = point.x
        
        Box.__update_edge(self.edge, new_edge)


class MBR(object):
    """
    Class for MBR to store voronoi, Maximum content is N
    """
    MAXIMUM_CONTENT = 4

    def __init__(self):
        self.content = []
        self.edge = Edge()

    def content_size(self):
        """
        return content size
        """
        return len(self.content)

    def split_mbr(self, first, second):
        pass

    def add(self, voronoi):
        """
        adding process to MBR
        """
        if (self.content_size + 1 < MBR.MAXIMUM_CONTENT):
            self.content.append(voronoi)
            voronoi_edges = voronoi.get_edge()
            self.__update_edge(voronoi_edges)
            return self  # returning current MBR
        else:  # splitting mbr into 2
            first = MBR()
            second = MBR()
            return self.split_mbr(first, second)
