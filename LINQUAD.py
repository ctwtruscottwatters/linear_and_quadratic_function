# -*- coding: utf-8 -*-
"""
Linear and Quadratic Function Example

@author: Charles_Truscott
Written while sitting 6.0001 from MIT OCW, edX.org

"""
def solve_quadratic_function(a, b, c, point=0):
    for x in range(-10, 11, 1):
        print("x: {}\t\ty: {}".format(x, a * x ** 2 + b * x + c))
        print("{} * {} ^ 2 + {} * {} + {} = {}".format(a, x, b, x, c, a * x ** 2 + b * x + c))
    point = 2055
    print("The value at the point {} of {} * {} ^ 2 + {} * {} + {} is:\t{}".format(point, a, point, b, point, c, a * point ** 2 + b * point + c))
def solve_linear_function(m, b, point=0):
    for x in range(-10, 11, 1):
        print("x: {}\t\ty: {}".format(x, m * x + b))
        print("y = {} * {} + {} = {}\n".format(m, x, b, m * x + b))
    point = 2093
    print("The value at the point {} of {} * {} + {} is:\t{}".format(point, m, point, b, m * point + b))
    
def main():
    solve_linear_function(2481, 1955, 0)
    solve_quadratic_function(1955, 1993, 0)
if __name__ == "__main__": main()