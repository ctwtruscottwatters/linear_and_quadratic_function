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
    return a * point ** 2 + b * point + c
def solve_linear_function(m, b, point=0):
    for x in range(-10, 11, 1):
        print("x: {}\t\ty: {}".format(x, m * x + b))
        print("y = {} * {} + {} = {}\n".format(m, x, b, m * x + b))
    point = 2093
    print("The value at the point {} of {} * {} + {} is:\t{}".format(point, m, point, b, m * point + b))
    return m * point + b
def main():
    x = solve_linear_function(2481, 1955, 1993)
    y = solve_quadratic_function(1955, 1993, 2481)
    z = ((x & y) ^ (x | y)) 
    z <<= 2
    print("z: = {}".format(int(z)))
    z = str(z)
    pqrs = ""
    for c in z:
        if c == "1":
            print("ABC", end='')
            pqrs += c
        if c == "2":
            print("DEF", end='')
            pqrs += c
        if c == "3":
            print("GHI", end='')
            pqrs += c
        if c == "4":
            print("JKL", end='')
            pqrs += c
        if c == "5":
            print("MNO", end='')
            pqrs += c
        if c == "6":
            print("PQR", end='')
            pqrs += c
        if c == "7":
            print("STU", end='')
            pqrs += c
        if c == "8":
            print("VWX", end='')
            pqrs += c
        if c == "9":
            print("YZA", end='')
            pqrs += c
        if c == "10":
            print("BCD", end='')
            pqrs += c
    print("\n")
    abcd = ((5194688 & 8260111971) ^ (5194688 | 8260111971))
    abcd <<= 2
    print("{}".format(str("011001111000000110000011000")))
    print("Encrypted text (basic cryptosystem):")
    print("{}".format(abcd))
 
if __name__ == "__main__": main()