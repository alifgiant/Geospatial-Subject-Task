'''
MAIN APP FOR MY TA
'''

import input_reader
import mbr
from model import Point

def main():
    """
    Main algorithm functions
    """

    # read input from raw data
    # voronoi_list = input_reader.read_input()
    
    # store readed voronoi to increase processing speed
    # input_reader.store_processed_input(voronoi_list)

    # read input from processed data
    voronoi_list = input_reader.get_processed_input()

    # create mbr
    mbr_list = mbr.create_mbr(voronoi_list)

    # new query point
    query_point = Point(0.2221, 2.2222)
    # voronoi_position = mbr.find_voronoi_for_point(mbr, query_point)

    print('total voronoi', len(voronoi_list))
    print('my point location', query_point)

if __name__ == '__main__':
    main()
