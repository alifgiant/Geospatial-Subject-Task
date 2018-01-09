"""
Main file
"""

import time
import pickle
import os.path
from model import Point, RTree
import input_reader
import utils

def build_tree(voronoi_file_source, should_build_new = False):
    """
    build tree either by read new data or read saved data
    """
    saved_tree_path = 'save/pypy_tree.pkl'

    if not should_build_new and os.path.isfile(saved_tree_path):
        with open(saved_tree_path, 'rb') as file_input:
            tree = pickle.load(file_input)
    else:        
        voronoi_list = input_reader.read_input(voronoi_file_source)
        tree = RTree(max_content_size = 4)

        start_construct = time.time()
        for voronoi in voronoi_list:
            print('processing:', voronoi.name)
            # tree.insert(voronoi)
            #  tree.reset()
            #  tree.inspectTree()
            #  print(tree.choose_leaf())    
        duration = time.time() - start_construct
        print('Tree Construction Time (ms):', duration)

        with open(saved_tree_path, 'wb') as file_output:
            pickle.dump(tree, file_output, pickle.HIGHEST_PROTOCOL)
        
    return tree


if __name__ == '__main__':

    FILE_INPUT = 'test/test-region-4.input'	
    TREE, ALL_VORONOI = build_tree(FILE_INPUT, should_build_new = True)

    # with open('save/pypy_seq-05-titik.pkl', 'wb') as file_output:
    #     pickle.dump(tree, file_output, pickle.HIGHEST_PROTOCOL)

    # for v in voronoi_list:
    #     print(v.name)
    # points = [  Point(), #R0
    #             Point(1.000, 198),#R14
    #             Point(662.1,551.96)]#R8
    # for p in points:

    # for v in voronoi_list;

    # random.uniform(1.0,)

    """
    Input query point
    """

    QUERY_POINT = Point(465,484)

    # """
    # R-Tree Search

    # """
    # startRtree = int(round(time.time() * 1000))
    # region = tree.search(QUERY_POINT, include_on_edge=True)
    # if region:
    #     print ('Region Found:', region)
    # else:
    #     print ('Region Not Found')

    # endRtree = int(round(time.time() * 1000))
    # longRtree = endRtree - startRtree
    # print ('Waktu Pencarian R-Tree = ', longRtree, 'ms')
    
    # #
    # #      # query_point = Point([float(data) for data in raw_input('Query Point (x,y): ').split(',')])
    # #
    # #
    
    # """
    # Sequential Search
    
    # """
    # startSeq = int(round(time.time()*1000))
    
    # response = tree.seq_search(query_point,True, voronoi_list)
    # print(response)    
    # endSeq=int(round(time.time()*1000))
    # longSeq = endSeq - startSeq
    
    # print ('Waktu Pencarian Linear = ', longSeq, 'ms')
