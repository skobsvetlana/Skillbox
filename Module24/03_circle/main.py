from circle_class import Circle

circle1 = Circle()
circle2 = Circle(7, 6, 4)

circle1.print_info()
circle1.increase_circle(5)
circle1.print_info()
circle2.print_info()
circle1.is_intersect(circle2)
circle1.is_intersect('fgh')
