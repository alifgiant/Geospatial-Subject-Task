'''
MAIN APP FOR MY TA
'''

import turtle
import input_reader
import utils
from model import MBR

def main(file_address):
    """
    Main algorithm functions
    """

    # read input from raw data
    # voronoi_list = input_reader.read_input(file_address)
    
    # store readed voronoi to increase processing speed
    # input_reader.store_processed_input(voronoi_list)

    # read input from processed data
    voronoi_list = input_reader.get_processed_input(file_address)

    # create MBR
    mbr = MBR()
    for voronoi in voronoi_list:
        mbr.add(voronoi)

    # new query point
    # query_point = Point(0.2221, 2.2222)
    # voronoi_position = mbr.find_voronoi_for_point(mbr, query_point)

    print('total voronoi', len(voronoi_list))
    # print('my point location', query_point)

if __name__ == '__main__':
    for a_file in utils.get_all_files_in('test/'):
        draw_voronoi(a_file)
        break