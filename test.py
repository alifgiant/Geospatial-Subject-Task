import turtle
# import input_reader


# def draw_voronoi(file_address):
#     """draw voronoi using bob the turtele"""
#     # read input from processed data
#     voronoi_list = input_reader.read_input(file_address)
#     turtle.getscreen().screensize(20000,20000)
#     turtle.speed(10)
#     for voronoi in voronoi_list:        
#         point_generator = voronoi.get_points()
#         point = next(point_generator)
#         turtle.setpos(point.x, point.y)
#         turtle.pendown()

#         for point in voronoi.get_points():
#             turtle.setpos(point.x, point.y)
        
#         turtle.penup()

#     # turtle.setpos(60,30)
#     turtle.mainloop()

def comb_and_comp(lst, n):
    """
    get combination and its complementer
    function from https://stackoverflow.com/questions/28992042/algorithm-to-return-all-combinations-of-k-out-of-n-as-well-as-corresponding-comp
    """
    # no combinations
    if len(lst) < n:
        return
    # trivial 'empty' combination
    if n == 0 or lst == []:
        yield [], lst
    else:
        first, rest = lst[0], lst[1:]
        # combinations that contain the first element
        for in_, out in comb_and_comp(rest, n - 1):
            yield [first] + in_, out
        # print('move next generator')
        # combinations that do not contain the first element
        for in_, out in comb_and_comp(rest, n):
            yield in_, [first] + out

if __name__ == '__main__':
    # for a_file in utils.get_all_files_in('test/'):
    #     draw_voronoi(a_file)
    #     break
    for max_member_count in range(4):
        for case in comb_and_comp([0,1,2,3,4], max_member_count+1):
            print('case', case)