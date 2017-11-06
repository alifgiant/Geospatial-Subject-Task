"""
this file describe MBR processing
"""

def create_mbr(voronoi_list):
    """
    create mbr list for voronoi,
    RULE: an MBR mostly consist of 4 voronoi
    """
    mbr = []
    for voronoi in voronoi_list:
        edges = voronoi.get_outer_point()
        # if 
        pass
    return 0


def find_voronoi_for_point(mbr, point):
    """
    Query Point in MBR to find voronoi
    """
    # return voronoi name
    return 'R0'


