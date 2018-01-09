"""
Main file
"""

import time
import pickle
import os.path
from model import Point, RTree
import input_reader

def build_tree(voronoi_file_source, should_build_new=False):
    """
    build tree either by read new data or read saved data
    """
    saved_tree_path = 'save/pypy_tree.pkl'

    if not should_build_new and os.path.isfile(saved_tree_path):
        print('Loading Tree From File:', saved_tree_path)
        with open(saved_tree_path, 'rb') as file_input:
            tree = pickle.load(file_input)
    else:
        if(not should_build_new):
            print('=======', 'No saved file found', '=======')

        print('Building Tree From', voronoi_file_source)
        voronoi_list = input_reader.read_input(voronoi_file_source)
        tree = RTree(max_content_size = 4)

        start_construct = time.time()
        for voronoi in voronoi_list:
            print('processing:', voronoi.name)
            tree.insert(voronoi)
            
        duration = time.time() - start_construct
        print('Tree Construction Time (ms):', duration)

        with open(saved_tree_path, 'wb') as file_output:
            print('Saving Tree To:', saved_tree_path)
            pickle.dump(tree, file_output, pickle.HIGHEST_PROTOCOL)
        
    return tree

if __name__ == '__main__':
    FILE_INPUT = 'test/region-4/region-4.input'	
    TREE = build_tree(FILE_INPUT, should_build_new = False)

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
