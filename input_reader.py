'''
This file define how my TA gain it's input
'''

import pickle
from model import Point, Voronoi


def clean_input(address='voronoi.input'):
    """
    clean input file from empty lines
    """
    file_input = open(address, 'r')
    file_output = open(address+".out", 'w')

    for line in file_input:
        if line not in ('', ' ', '\n'):
            file_output.write(line)


def read_input(address='voronoi.input'):
    """
    read input file in address location and return array points
    param:
    - address

    retun:
    - voronoi list
    """
    file_input = open(address, 'r')
    voronoi_list = []
    for line in file_input:
        data = line.split(',')
        # print(data, data[0])

        current_voronoi = get_voronoi(voronoi_list, data[0])
        point = Point(data[1], data[2])

        current_voronoi.add_point(point)

    return voronoi_list


def get_voronoi(voronoi_list, voronoi_name):
    """
    get the last voronoi to insert poin, cause input file is not sorted
    """
    for voronoi in voronoi_list:
        if voronoi.name == voronoi_name:
            return voronoi
    
    new_voronoi = Voronoi(voronoi_name)
    voronoi_list.append(new_voronoi)

    return new_voronoi


def store_processed_input(voronoi_list, file_address='processed.in'):
    """
    store processing input into json
    """
    with open(file_address, 'wb') as output:
        pickle.dump(voronoi_list, output, pickle.HIGHEST_PROTOCOL)


def get_processed_input(address='processed.in'):
    """
    read input from processed file
    """
    with open(address, 'rb') as input_file:
        return pickle.load(input_file)
