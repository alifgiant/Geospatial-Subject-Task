"""
Unit Test file for moodel
"""
import unittest
from model import Voronoi, RTree, Point

def do_inspect(tree):
    tree.inspect_tree()

class TestVoronoi(unittest.TestCase):
    """
    Test Case for Voronoi object
    """
    def test_voronoi_creation(self):
        points = [(1, 1), (3, 1), (3, 3), (1, 3)]
        voronoi = Voronoi("poly_a", points)
        self.assertEqual(len(points), len(voronoi.bound.vertices))
        self.assertEqual(Point(2, 2), voronoi.bound.centroid)
        self.assertEqual(4, voronoi.bound.area)

class TestRTree(unittest.TestCase):
    """
    Test Case for RTree object
    """
    def test_update_bound(self):
        """
        Make sure update bound work
        """
        polygon_a = Voronoi("poly_a", [(1, 4), (1, 1), (3, 1), (3, 4)])
        polygon_b = Voronoi("poly_b", [(10, 4), (9, 3), (10, 3)])
        polygon_c = Voronoi("poly_c", [(1, 4), (1, 1), (10, 1), (10, 4)])
        self.assertEqual(polygon_c.bound, RTree.update_bound(polygon_a, polygon_b))
    
    def test_split(self):
        """
        Make sure split into 2 distance nodes, and the splitted refer to correct parent
        """
        polygon_a = Voronoi("poly_0", [(1, 4), (1, 3), (3, 3), (3, 4)])
        polygon_b = Voronoi("poly_1", [(1, 3), (1, 1), (3, 1), (3, 3)])
        polygon_c = Voronoi("poly_2", [(8, 4), (8, 3), (9, 3), (9, 4)])
        polygon_d = Voronoi("poly_3", [(9, 4), (9, 3), (10, 4)])
        polygon_e = Voronoi("poly_4", [(10, 4), (9, 3), (10, 3)])

        root = RTree()
        root.childs = [polygon_a, polygon_b, polygon_c, polygon_d, polygon_e]    
        first, second = root.split()

        self.assertEqual(2, len(first.childs))
        self.assertEqual(3, len(second.childs))

        self.assertEqual(root, first.parent)
        self.assertEqual(root, second.parent)
    
    def test_rebound_border(self):         
        """
        Make rebound border, recreate MBR
        """
        polygon_a = Voronoi("poly_a", [(1, 4), (1, 1), (3, 1), (3, 4)])
        polygon_b = Voronoi("poly_b", [(10, 4), (9, 3), (10, 3)])
        polygon_c = Voronoi("poly_c", [(1, 4), (1, 1), (10, 1), (10, 4)])

        tree = RTree()
        tree.childs = [polygon_a, polygon_b]
        tree.rebound_border()
    
        self.assertEqual(polygon_c.bound, tree.bound)
    
    def test_insert_in_leaf(self):  
        """
        Make sure linear/leaf insert work
        """
        polygon_a = Voronoi("poly_a", [(1, 4), (1, 3), (3, 3), (3, 4)])
        polygon_b = Voronoi("poly_b", [(1, 3), (1, 1), (3, 1), (3, 3)])
        polygon_c = Voronoi("poly_c", [(8, 4), (8, 3), (9, 3), (9, 4)])
        polygon_d = Voronoi("poly_d", [(9, 4), (9, 3), (10, 4)])

        tree = RTree()
        tree.insert(polygon_a)
        self.assertEqual(1, len(tree.childs))
        tree.insert(polygon_b)
        self.assertEqual(2, len(tree.childs))
        tree.insert(polygon_c)
        self.assertEqual(3, len(tree.childs))
        tree.insert(polygon_d)
        self.assertEqual(4, len(tree.childs))
    
    def test_insert_in_2_order(self):
        """
        Make sure insert into 2nd order node correct
        """
        polygon_a = Voronoi("poly_0", [(1, 4), (1, 3), (3, 3), (3, 4)])
        polygon_b = Voronoi("poly_1", [(1, 3), (1, 1), (3, 1), (3, 3)])
        polygon_c = Voronoi("poly_2", [(8, 4), (8, 3), (9, 3), (9, 4)])
        polygon_d = Voronoi("poly_3", [(9, 4), (9, 3), (10, 4)])
        polygon_e = Voronoi("poly_4", [(10, 4), (9, 3), (10, 3)])

        child1 = RTree(content = [polygon_a, polygon_b])
        child2 = RTree(content = [polygon_c, polygon_d])
        
        root = RTree(content = [child1, child2])
        root.is_leaf = False

        root.insert(polygon_e)
        self.assertNotEqual(3, len(child1.childs))
        self.assertEqual(3, len(child2.childs))
    
    def test_find_furthest_2(self):
        """
        Make sure returned 2 furtest region
        """
        polygon_a = Voronoi("poly_0", [(1, 4), (1, 3), (3, 3), (3, 4)])
        polygon_b = Voronoi("poly_1", [(1, 3), (1, 1), (3, 1), (3, 3)])
        polygon_c = Voronoi("poly_2", [(8, 4), (8, 3), (9, 3), (9, 4)])
        polygon_d = Voronoi("poly_3", [(9, 4), (9, 3), (10, 4)])

        root = RTree(content = [polygon_a, polygon_b, polygon_c, polygon_d])

        self.assertEqual(polygon_b.bound, root.find_furthest_2()[0].bound)
        self.assertEqual(polygon_d.bound, root.find_furthest_2()[1].bound)
    
    def test_search(self):
        """
        Momment of true, search query point
        """
        polygon_a = Voronoi("poly_0", [(1, 4), (1, 3), (3, 3), (3, 4)])
        polygon_b = Voronoi("poly_1", [(1, 3), (1, 1), (3, 1), (3, 3)])
        polygon_c = Voronoi("poly_2", [(8, 4), (8, 3), (9, 3), (9, 4)])
        polygon_d = Voronoi("poly_3", [(9, 4), (9, 3), (10, 4)])
        polygon_e = Voronoi("poly_4", [(10, 4), (9, 3), (10, 3)])

        tree_a = RTree(content = [polygon_a, polygon_b])
        tree_b = RTree(content = [polygon_c, polygon_d, polygon_e])

        tree = RTree(content = [tree_a, tree_b])
        res = tree.search(Point(2, 1), include_on_edge = True)
        self.assertEqual(("poly_1", 2), res)

        res = tree.search(Point(4, 2), include_on_edge = True)
        self.assertIsNone(res)

if __name__ == '__main__':
    unittest.main()