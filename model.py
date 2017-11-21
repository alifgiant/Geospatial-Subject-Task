"""
This File Define My Wy to Model The Data
"""
import unittest

def comb_and_comp(lst, size):
    """
    get combination and its complementer
    function from https://stackoverflow.com/questions/28992042/algorithm-to-return-all-combinations-of-k-out-of-n-as-well-as-corresponding-comp
    """
    # no combinations
    if len(lst) < size:
        return
    # trivial 'empty' combination
    if size == 0 or lst == []:
        yield [], lst
    else:
        first, rest = lst[0], lst[1:]
        # combinations that contain the first element
        for in_, out in comb_and_comp(rest, size - 1):
            yield [first] + in_, out
        # print('move next generator')
        # combinations that do not contain the first element
        for in_, out in comb_and_comp(rest, size):
            yield in_, [first] + out

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
        if (len(edges) > 1):
            for edge in edges[1]:           
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
        return self.top == other.top \
                    and self.bottom == other.bottom  \
                    and self.right == other.right \
                    and self.left == other.left


class Box(object):
    """
    Implementation Of A Box Region
    """
    def __init__(self, top=None, bottom=None, right=None, left=None):
        self.edge = None
        if top is not None and bottom is not None and right is not None and left is not None:
            self.edge = Edge(top, bottom, right, left)

    def _update_edge(self, *new_edge):
        if self.edge is None:
            self.edge = new_edge[0]
        self.edge = Edge.combine_edge(self.edge, new_edge)

    def is_inside_box(self, other_box):
        """find out wether other box is inside"""
        return self.edge.top > other_box.edge.top and self.edge.bottom < other_box.edge.bottom \
                and self.edge.left < other_box.edge.left and self.edge.right > other_box.edge.right

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
        Box.__init__(self)
        self.x = float(x)
        self.y = float(y)
        self._update_edge(Edge(self.y, self.y, self.x, self.x))

    def __str__(self):
        return "position {} {}".format(self.x, self.y)


class Voronoi(Box):
    """
    Class For Region (Voronoi) holding an array for points
    Assume as a box area, to target MBR
    """

    def __init__(self, name=""):
        Box.__init__(self)
        self.name = name
        self.__points = []

    def __str__(self):
        return "voronoi {} has {} points size {}".format(self.name, len(self.__points), self.calculate_area())

    def get_points(self):
        """get poitns generator"""
        for point in self.__points:
            yield point

    def add_point(self, point):
        """Insert a point edge into voronoi"""
        self.__points.append(point)
        self._update_edge(point.edge)

    def add_points(self, *points):
        """Insert a points edge into voronoi"""
        self.__points.extend(points)
        for point in points:
            self._update_edge(point.edge)

class MBR(Box):
    """
    Class for MBR to store voronoi, Maximum content is N
    """
    MAXIMUM_CONTENT = 4

    def __init__(self, is_leaf=True):
        Box.__init__(self)
        self.content = list()
        self.is_leaf = is_leaf

    def content_size(self):
        """
        return content size
        """
        return len(self.content)

    def split_mbr(self):
        """split current mbr into 2"""
        # ready the new container
        first_mbr = MBR()
        second_mbr = MBR()
        
        content_indexes = list(range(len(self.content)))
        for max_member_count in range(MBR.MAXIMUM_CONTENT):
            for first_indexes, second_indexes in comb_and_comp(content_indexes, max_member_count + 1):
                print('indexes', first_indexes, second_indexes)
                new_first = MBR()
                new_second = MBR()
                new_first.add_list_points_test([self.content[i] for i in first_indexes])
                new_second.add_list_points_test([self.content[i] for i in second_indexes])

                print('new_first', new_first)

                if (first_mbr.content_size() == 0 and second_mbr.content_size() == 0):
                    first_mbr = new_first
                    second_mbr = new_second
                else:
                    current_best = first_mbr.calculate_area() + second_mbr.calculate_area()
                    new_best = new_first.calculate_area() + new_second.calculate_area()
                    if new_best < current_best:
                        first_mbr = new_first
                        second_mbr = new_second

                print('current', first_mbr.calculate_area(), second_mbr.calculate_area())
                print('new', new_first.calculate_area(), new_second.calculate_area())

        return first_mbr, second_mbr

    def add(self, voronoi):
        """
        adding process to MBR
        """
        if (self.is_leaf):
            self.content.append(voronoi)

            if (self.content_size < MBR.MAXIMUM_CONTENT):
                self._update_edge(voronoi.get_edge())
                return self  # returning current MBR
        
            else:  # splitting mbr into 2
                return self.split_mbr()
        else:
            pass
    
    def add_list_points_test(self, points):
        for point in points:
            self.content.append(point)
            self._update_edge(point.edge)

    def __str__(self):
        print()
        if self.content_size() > 0:
            for content in self.content:
                print('content', content)
            return ''
        else:
            return 'empty content'
        

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

    def test_split(self):
        """Test case for box model"""
        mbr = MBR()
        vorono1 = Voronoi('vorono1')
        vorono2 = Voronoi('vorono2')
        vorono3 = Voronoi('vorono3')
        vorono4 = Voronoi('vorono4')
        vorono5 = Voronoi('vorono5')

        vorono1.add_points(Point(1,1), Point(3,1), Point(3,2), Point(1,2))
        vorono2.add_points(Point(1,1), Point(3,1), Point(3,2), Point(1,2))
        vorono3.add_points(Point(1,1), Point(3,1), Point(3,2), Point(1,2))
        # vorono2.add_points(Point(2,3), Point(3,3), Point(3,4), Point(2,4))
        # vorono3.add_points(Point(4,6), Point(7,6), Point(7,9), Point(4,9))
        vorono4.add_points(Point(7,7), Point(9,7), Point(9,10), Point(7,10))
        vorono5.add_points(Point(7,7), Point(9,7), Point(9,10), Point(7,10))
        # vorono5.add_points(Point(6,1), Point(8,1), Point(8,3), Point(6,3))

        mbr.content.append(vorono1)
        mbr.content.append(vorono2)
        mbr.content.append(vorono3)
        mbr.content.append(vorono4)
        mbr.content.append(vorono5)

        print('=======')
        print('vorono1', vorono1.calculate_area())
        print('vorono2', vorono2.calculate_area())
        print('vorono3', vorono3.calculate_area())
        print('vorono4', vorono4.calculate_area())
        print('vorono5', vorono5.calculate_area())
        print('=======')

        first, second = mbr.split_mbr()

        print('first', first)
        print('second', second)

        self.assertEqual(3, 3)

if __name__ == '__main__':
    unittest.main()
    # TestModel().test_split()
