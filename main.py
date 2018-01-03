import input_reader
import utils
import time
from model import Point, RTree
# import pickle
import random

def build_tree(file_dir):    
     voronoi_list = input_reader.read_input(file_dir)
     tree = RTree(max_content_size = 4)

     startConstruct = int(round(time.time()*1000))
     for voronoi in voronoi_list:
        #  print("insert region:", voronoi.name)
         tree.insert(voronoi)
        #  tree.reset()
        #  tree.inspectTree()
        #  print(tree.choose_leaf())
     endConstruct = int(round(time.time()*1000))
     longConstruct = endConstruct-startConstruct
    #  print (longConstruct,'Time Construct (ms)')

    #  with open('save/pypy_tree.pkl', 'wb') as file_output:
    #      pickle.dump(tree, file_output, pickle.HIGHEST_PROTOCOL)

    #  with open('save/pypy_tree.pkl', 'rb') as file_input:
    #    tree = pickle.load(file_input)
     return tree


if __name__ == '__main__':
    #file_input = raw_input('Input File (file.input): ')
    # file_input = 'test/test-irfan.input'
    file_input = 'object/region-10-titik.input'
        
    tree= build_tree(file_input)
    tree.inspectTree()


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

    query_point =Point(465,484)

    """
    R-Tree Search
    
    """
    # startRtree = int(round(time.time() * 1000))
    # region = tree.search(query_point, include_on_edge=True)
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

    """
    Sequential Search
    
    """
    voronoi_list = input_reader.read_input(file_input) 
    startSeq = int(round(time.time()*1000))
    
    response = tree.seq_search(query_point,True, voronoi_list)
    print(response)
    p = tree.search(query_point,True)
    # print(p)
    
    endSeq=int(round(time.time()*1000))
    longSeq = endSeq - startSeq
    
    print ('Waktu Pencarian Linear = ', longSeq, 'ms')
