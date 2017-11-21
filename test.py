import turtle
import input_reader


def draw_voronoi(file_address):
    """draw voronoi using bob the turtele"""
    # read input from processed data
    voronoi_list = input_reader.read_input(file_address)
    turtle.getscreen().screensize(20000,20000)
    turtle.speed(10)
    for voronoi in voronoi_list:        
        point_generator = voronoi.get_points()
        point = next(point_generator)
        turtle.setpos(point.x, point.y)
        turtle.pendown()

        for point in voronoi.get_points():
            turtle.setpos(point.x, point.y)
        
        turtle.penup()

    # turtle.setpos(60,30)
    turtle.mainloop()

if __name__ == '__main__':
    for a_file in utils.get_all_files_in('test/'):
        draw_voronoi(a_file)
        break