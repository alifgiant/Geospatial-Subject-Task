"""
Model definition files,
hold voronoi and RTree
"""

from sympy import Point, Polygon
import math

class Voronoi(object):
    """
    Region definition, called voronoi
    """
    def __init__(self, name, points):        
        self.name = name
        self.bound = Polygon(*points)
    
    def __str__(self):
        return str(self.bound)
    
class RTree(object):
    """
    RTree definition, indexing using RTree
    """
    def __init__(self, max_content_size = 4, content = None, is_leaf = True, parent = None):
        self.max_content_size = max_content_size        
        self.bound = None

        self.childs = list()
        self.parent = parent
        self.is_leaf = is_leaf

        if not content:
            content = list()
        for voronoi in content:
            if isinstance(voronoi, RTree) and not self.is_leaf:
                self.is_leaf = False
            self.insert(voronoi)

    # def inspectTree(self):
    #     currentLevel = []
    #     nextLevel =[]
    #     print(len(self.childs))
    #     for n in self.childs:
    #         #  print(n)
    #         currentLevel.append(n)
    #     while len(currentLevel) != 0:
    #         x = currentLevel.pop(0)
    #         if isinstance(x,RTree):
    #             #  print("Subtree")
    #             #  print(x)
    #             mixed = False
    #             type = isinstance(x.childs[0],RTree)
    #             #  print(type)
    #             for n in x.childs:
    #                 if(isinstance(n,RTree) != type and mixed == False):
    #                     mixed = True
    #                 nextLevel.append(n)
    #             #  print("Mixed: " + str(mixed))
    #         #  else:
    #             #  print("Region")
    #             #  print(x.name)
    #         if(len(currentLevel) == 0):
    #             #  print("Next Level/Depth")
    #             currentLevel = nextLevel
    #             nextLevel = []
       
    def search(self, query_point, include_on_edge = False, current_depth = 0):
        """
        Search Tree Using DFS
        """
        for child in self.childs:
            if(child.bound.encloses_point(query_point) or (include_on_edge and child.bound.intersection(query_point))):
                if isinstance(child, Voronoi):
                    return child.name, current_depth + 1 # pylint: disable=E1101
                else:
                    result = child.search(query_point, include_on_edge, current_depth + 1)
                    if result:  # if result none, continue check next child, else it has been CATCH
                        return result
        
        return None

    def insert(self, new_inserted):
        """
        Main Process of RTree, node insertion
        """
        if self.is_leaf and len(self.childs) + 1 <= self.max_content_size:
            self.childs.append(new_inserted)
            self.bound = self.update_bound(self, new_inserted)

        elif not self.is_leaf:
            # look for suitable node
            selected_child = self.childs[0]  # default select first child
            selected_bound_area = RTree.update_bound(selected_child, new_inserted).area
            
            for child in self.childs[1:]:
                bound_area = RTree.update_bound(child, new_inserted).area

                # if area smaller than selected pick it or if area is equals, pick one with lesser child
                if bound_area < selected_bound_area or \
                    (bound_area == selected_bound_area and len(child.childs) < len(selected_child.childs)):
                    selected_child = child
                    selected_bound_area = bound_area
            
            selected_child.insert(new_inserted)

        else:  # self in not leaf and adding child will make overflow
            # add it first
            self.childs.append(new_inserted)

            # then try split
            first, second = self.split()
            self.is_leaf = False
            self.childs = [first, second] # make current trees child to refer new splitted region
            
            # then rebound upward
            self.rebound_upward()           
    
    def split(self):
        """
        Do Split based on furthest 2, map the rest into new tree
        """
        first, second = self.find_furthest_2()
        new_tree_first = RTree(parent = self)
        new_tree_first.insert(first)

        new_tree_second = RTree(parent = self)
        new_tree_second.insert(second)

        for child in self.childs:
            if child not in [first, second]:
                if child.bound.centroid.distance(first.bound.centroid) < child.bound.centroid.distance(second.bound.centroid):
                    new_tree_first.insert(child)
                else:
                    new_tree_second.insert(child)
        return new_tree_first, new_tree_second

    def find_furthest_2(self):
        """
        Pick furtest 2 MBR currently holded by tree
        """
        selected_first = None
        selected_second = None
        selected_distance = None

        for index_first, voronoi_first in enumerate(self.childs[:-1]):
            for voronoi_second in self.childs[index_first:]:
                # euclid distance
                current_distance = voronoi_first.bound.centroid.distance(voronoi_second.bound.centroid)

                if not selected_distance or current_distance > selected_distance:
                    selected_distance = current_distance
                    # if selected distance still none, so does selected first and second
                    selected_first = voronoi_first
                    selected_second = voronoi_second
        # return finding
        return selected_first, selected_second
                
    def rebound_upward(self):
        """
        keep the tree level the same
        """
        if self.parent is not None:
            self.parent.childs.remove(self)

            for child in self.childs:
                # add self child to parent
                self.parent.childs.append(child)

            if len(self.parent.childs) > self.parent.max_content_size:
                self.parent.childs = list(self.parent.split())
                self.parent.rebound_upward()

            if self.parent:  # make sure parent is not deleted yet
                self.parent.rebound_border()  # make sure border size is correct            

    def rebound_border(self):
        """
        Reset border / MBR of a Tree, in case there is a child removed
        """
        self.bound = None
        for content in self.childs:
            self.bound = RTree.update_bound(self, content)
    
    @staticmethod
    def update_bound(current, other):
        if current.bound is None:
            return other.bound
        else:
            current_xmin, current_ymin, current_xmax, current_ymax = current.bound.bounds
            other_xmin, other_ymin, other_xmax, other_ymax = other.bound.bounds
            current_xmin = other_xmin if other_xmin < current_xmin else current_xmin
            current_ymin = other_ymin if other_ymin < current_ymin else current_ymin
            current_xmax = other_xmax if other_xmax > current_xmax else current_xmax
            current_ymax = other_ymax if other_ymax > current_ymax else current_ymax
            return Polygon((current_xmin, current_ymin), (current_xmax, current_ymin), (current_xmax, current_ymax), (current_xmin, current_ymax))


def seq_search(query_point, voronoi_list, include_on_edge=False):
    """
    Do Seq Search To List
    """
    for voronoi in voronoi_list:
        if voronoi.bound.encloses_point(query_point) or (include_on_edge and voronoi.bound.intersection(query_point)):
            return voronoi.name
    return None