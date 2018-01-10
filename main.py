"""
Main file
"""

import time
import pickle
import os.path
from model import Point, RTree, seq_search
import input_reader

def build_seq_voronoi(voronoi_file_source, should_build_new=False):
    """
    build a linear list of voronoi 
    """
    saved_voronoi_path = 'save/pypy_seq.pkl'

    if not should_build_new and os.path.isfile(saved_voronoi_path):
        print('Loading Voronoi List From File:', saved_voronoi_path)
        with open(saved_voronoi_path, 'rb') as file_input:
            all_list = pickle.load(file_input)
    else:
        if(not should_build_new):
            print('=======', 'No saved file found', '=======')

        print('Building Voronoi List From', voronoi_file_source)
        voronoi_list = input_reader.read_input(voronoi_file_source)

        start_construct = time.time()
        all_list = list(voronoi_list)            
        duration = time.time() - start_construct
        print('List Construction Time (ms):', duration * 1000)

        with open(saved_voronoi_path, 'wb') as file_output:
            print('Saving List To:', saved_voronoi_path)
            pickle.dump(all_list, file_output, pickle.HIGHEST_PROTOCOL)
        
    return all_list

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
            tree.inspectTree()
            
        duration = time.time() - start_construct
        print('Tree Construction Time (ms):', duration * 1000)

        with open(saved_tree_path, 'wb') as file_output:
            print('Saving Tree To:', saved_tree_path)
            pickle.dump(tree, file_output, pickle.HIGHEST_PROTOCOL)
        
    return tree

if __name__ == '__main__':
    FILE_INPUT = 'test/region-15/region-15.input'	
    # FILE_INPUT = 'object/region-08-titik.input'	
    TREE = build_tree(FILE_INPUT, should_build_new = True)

    """
    Input query point
    """
    QUERY_POINT = Point(508, 686)

    print (TREE.find_reg("R254"))
    """
    R-Tree Search
    """
    START_TREE_SEARCH = time.time()
    RESULT = TREE.search(QUERY_POINT, include_on_edge=True)
    if RESULT:
        print ('---Region Found:', RESULT[0])
        print ('---Depth Found:', RESULT[1])
    else:
        print ('Region Not Found')
    
    # DURATION_TREE_SEARCH = time.time() - START_TREE_SEARCH    
    # print ('Waktu Pencarian R-Tree = ', DURATION_TREE_SEARCH * 1000, 'ms')
        
    # """
    # Sequential Search    
    # """
    # START_SEQ_SEARCH = time.time()    
    # VORONOI_LIST = build_seq_voronoi(FILE_INPUT, should_build_new = False)
    # RESULT_SEQ = seq_search(QUERY_POINT, VORONOI_LIST, include_on_edge=True)
    # if RESULT_SEQ:
    #     print ('---Region Found:', RESULT_SEQ)
    # else:
    #     print ('Region Not Found')
    
    # DURATION_SEQ_SEARCH = time.time() - START_SEQ_SEARCH        
    # print ('Waktu Pencarian Linear = ', DURATION_SEQ_SEARCH * 1000, 'ms')
