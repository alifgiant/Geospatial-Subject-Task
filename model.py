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
    def __init__(self, max_content_size = 4, content = None, is_leaf = True):
        self.max_content_size = max_content_size        
        self.childs = list()

        self.parent = None
        self.bound = None
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

    # def seq_search(self, query_point, include_on_edge, voronoi_list):
    #     for voronoi in voronoi_list:
    #         # print(voronoi.name)
    #         if voronoi.bound.encloses_point(query_point) or (include_on_edge and voronoi.bound.intersection(query_point)):
    #             return "Region Found :"+voronoi.name
    #     return 'Region Not Found'
    
    def search(self, query_point, include_on_edge = False):
        stack = []
        for n in self.childs:
            print(n)
            stack.append((n, 0))
        possible = []
        while len(stack) != 0:
            checked, depth = stack.pop(0)
            if(checked.bound.encloses_point(query_point) or (include_on_edge and checked.bound.intersection(query_point))):
                if isinstance(checked, RTree) :
                  for n in checked.childs:
                      # if isinstance(n,Voronoi):
                      # print(n.name)
                      stack.insert(0, (n, depth + 1))
                else:
                    # print(checked)
                    possible.append((checked.name, depth))
        #     for s in stack:
        #         print(s)
        #     print("###########")
        # for v in possible:
        #     print(v)
        return possible

    def insert(self, new_inserted):
        """
        Main Process of RTree, node insertion
        """
        if self.is_leaf and len(self.childs) + 1 < self.max_content_size:
            self.childs.append(new_inserted)
        if not self.is_leaf:
            # look for suitable node
            for child in self.childs:
                if child.bound.encloses_point(new_inserted) or child.bound.intersection(new_inserted):
                    child.insert(new_inserted)
                    break
        else:  # self in not leaf and adding child will make overflow
            # try split
            pass
    
    def _find_furthest_2(self):
        pass

    def rebound_upward(self):
        if self.parent is not None:
            # print 'rebound_upward', self.parent, self.parent.childs
            self.parent.childs.remove(self)
            for child in self.childs:
                self.parent.childs.append(child)            
            if len(self.parent.childs) > self.parent.max_content_size:
                self.parent.childs = list(self.parent.split())
                self.parent.rebound_upward()

    def reset(self):
        currentLevel = []
        nextLevel = []
        #print(len(self.childs))
        for n in self.childs:
            #print(n)
            currentLevel.append(n)
        while len(currentLevel) != 0:
            x = currentLevel.pop(0)
            if isinstance(x, RTree):
                x.isReinsert = False
                for n in x.childs:
                    nextLevel.append(n)
            if (len(currentLevel) == 0):
                #print("Next Level/Depth")
                currentLevel = nextLevel
                nextLevel = []

    def split(self,new_inserted):
        # ready the new container
        first_node = None
        second_node = None
        objects = [new_inserted] + self.childs
        bestpairs = (None, None)
        bestArea = 0
        for i in range(len(objects)):
            for j in range(i + 1, len(objects)):
                polygon = RTree.update_bound(objects[i], objects[j])
                area = polygon.area
                if (bestArea == 0 or bestArea < area):
                    bestpairs = (objects[i], objects[j])
                    bestArea = area
        # entry picking
        ###################
        # removing non seed entries
        firstGroup = [bestpairs[0]]
        secondGroup = [bestpairs[1]]
        objects.remove(bestpairs[0])
        objects.remove(bestpairs[1])
        for entry in objects:
            d1 = RTree.update_bound(entry, bestpairs[0]).area
            d2 = RTree.update_bound(entry, bestpairs[1]).area
            if (d1 <= d2):
                firstGroup.append(entry)
            else:
                secondGroup.append(entry)
        first_node = RTree(max_content_size=4, content=firstGroup, is_leaf=self.is_leaf)
        second_node = RTree(max_content_size=4, content=secondGroup, is_leaf=self.is_leaf)
        #
        # # put indexes in new list
        # content_indexes = list(range(len(self.childs)))
        # for max_member_count in range(self.max_content_size):
        #     for first_indexes, second_indexes in comb_and_comp(content_indexes, max_member_count + 1):
        #         new_first = RTree(max_content_size=self.max_content_size,
        #                                content=[self.childs[i] for i in first_indexes])
        #         new_second = RTree(max_content_size=self.max_content_size,
        #                                 content=[self.childs[i] for i in second_indexes])
        #         new_first.rebound_border()
        #         new_second.rebound_border()
        #         if (first_node is None and second_node is None):
        #             first_node = new_first
        #             second_node = new_second
        #
        #
        #     else:
        #             current_best = first_node.bound.area + second_node.bound.area
        #             new_best = new_first.bound.area + new_second.bound.area
        #             if new_best <= current_best:  # ' <= ' take last configuration, cause it divide the node with more member
        #                 first_node = new_first
        #                 second_node = new_second
        #
        # first_node.parent = self
        # second_node.parent = self
        #
        # self.is_leaf = False
        return first_node, second_node

    def rebound_border(self):
        self.bound = None
        for content in self.childs:
            self.bound = RTree.update_bound(self, content)

    @staticmethod
    def count_overlap_area(first, second):
        first_xmin, first_ymin, first_xmax, first_ymax = first.bound.bounds
        second_xmin, second_ymin, second_xmax, second_ymax = second.bound.bounds
        return (max(0, min(first_xmax, second_xmax)) - max(first_xmin, second_xmin)) * \
                (max(0, min(first_ymax, second_ymax)) - max(first_ymin, second_ymin))

    @staticmethod
    def choose_leaf(node, new_inserted):
        if node.is_leaf:
            return node
        else:
            choosed = None
            choosed_expanded_size = 0
            choosed_total_overlap = 0
            for i, child in enumerate(node.childs):
                expanded_size = RTree.update_bound(child, new_inserted).area
                total_overlap = 0
                for j, other_child in enumerate(node.childs[:i] + node.childs[i+1:]):
                    overlap = RTree.count_overlap_area(child, other_child)                    
                    total_overlap += overlap
                if choosed is None or \
                    choosed_total_overlap > total_overlap or \
                    (choosed_total_overlap == total_overlap and choosed_expanded_size > expanded_size):
                    choosed = child
                    choosed_expanded_size = expanded_size
                    choosed_total_overlap = total_overlap
            return RTree.choose_leaf(choosed, new_inserted)
    
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
