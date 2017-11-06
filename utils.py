import os
import input_reader

def turn_input_to_in(address, out_dir = 'out/'):
    file_name = address.split('/')
    name = file_name[-1][:file_name[-1].index('.')]
    # read input from raw data
    voronoi_list = input_reader.read_input(address)

    # store readed voronoi to increase processing speed
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    input_reader.store_processed_input(voronoi_list, out_dir+name+'.in')


def main():
    turn_input_to_in('object/region-5-titik.input')

if __name__ == '__main__':
    main()