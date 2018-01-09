'''
This file define how my TA gain it's input
'''

import pickle
from model import Voronoi

def clean_input(address='voronoi.input'):
    """
    clean input file from empty lines, remove "enter"
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

    current_region = ''
    points = list()

    for line in file_input:
        data = line.split(',')

        if current_region != data[0]:
            if points:
                yield Voronoi(current_region, points)
            
            points = list()

        current_region = data[0]
        points.append((float(data[1]), float(data[2])))
    
    if points:
        yield Voronoi(current_region, points)

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
