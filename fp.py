#!/usr/bin/env python3

import sys
from math import hypot
import time

MAX_MINUTES = 3

# make sure we received the right number of arguments
if len(sys.argv) < 2:
    print("error, no file name specified")
    print("correct usage: python3 fp.py [filename.txt]")
    sys.exit()

# this function creates an initial tour using nearest neighbor
def neighbor(c):
    return c

# this function returns the euclidean distance between cities a and b
def distance(a, b):
    return int(round(hypot(a[1]-b[1], a[2]-b[2])))

# this function computes the total length of a given tour
def tourLength(t):
    length = 0
    for n in range(len(t) - 1):
        length += distance(t[n], t[n+1])
    length += distance(t[len(t) - 1], t[0])
    return length

# this function performs a 'swap' between cities a and b in tour t
def swap(t, a, b):
    n = [] # the new tour that will contain the the swapped edges
    # the path from 0 until a - 1 is added to the new tour
    n += t[:a]
    # the path from a to b is added in reverse order
    n += t[b:a-1:-1]
    # the rest of the path after b is added to n
    n += t[b+1:]
    return n;

# this function checks whether two edges are crossing each other before performing a swap
# def crossing(t, i, j):
#     a = t[i] # first point in first edge
#     b = t[i + 1] # second point in first edge
#     c = t[j - 1] # first point in second edge
#     d = t[j] # second point in second edge
#
#     # 1) Find the small rectangle in which a crossig could occur.
#     # 1.a) Find the left side of the rectangle.
#     left = max(min(a[1], b[1]), min(c[1], d[1]))
#     # 1.b-d) Find the other sides.
#     right = min(max(a[1], b[1]), max(c[1], d[1]))
#     top = min(max(a[2], b[2]), min(c[2], d[2]))
#     bottom = max(min(a[2], b[2]), min(c[2], d[2]))
#
#     # 2) Find the intersection of the two lines, if it exists:
#     # 2.a) Find the standard equation of the line passing through the two
#     # points of each edge.
#     # 2.a.i) Find the slope of the first line using m = (y2-y1)/(x2-x1)
#     if a[1]-b[1] == 0:
#         return True
#     m1 = (a[2]-b[2])/(a[1]-b[1])
#     # 2.a.ii) Find the standard equation of the line, ax + by = c and store
#     # the coefficients a, b, c.  This requires some algebra wrangling to
#     # understand where everything comes from.
#     a1, b1, c1 = m1, 1, a[2]-m1*a[1]
#     # 2.a.iii) Do it again for the second line.
#     if c[1]-d[1] == 0:
#         return True
#     m2 = (c[2]-d[2])/(c[1]-d[1])
#     a2, b2, c2 = m2, 1, c[2]-m2*c[1]
#
#     # 3) Solve using numpy.
#     # 3.a) Form the matrices representing the coefficient matrix and
#     # constant vector.
#     A = np.matrix([[a1,b1], [a2,b2]])
#     c = np.matrix([[c1], [c2]])
#     # 3.b) Compute the inverse of A.  If it doesn't exist, the lines are
#     # parallel and don't cross.
#     try:
#         Ai = np.linalg.inv(A)
#         # 3.c) Compute the intersection of the lines.
#         sol = Ai.dot(c)
#
#         # 4) Check that the solution lies inside of the rectangle from part 1.
#         if (left <= sol[0] <= right) and (bottom <= sol[0] <= top):
#             return True
#         return False
#     except:
#         # Numpy's inverse function raises an exception if the inverse doesn't
#         # exist, in which case the lines are parallel and don't cross.
#         return False

# this function contains the 2-opt algorithm that optimizes our tour
def twoOpt(t):
    n = [] # a new temp tour
    bestLength = tourLength(t) # get tour length of initial tour
    startTime = time.clock() # start function timer
    found = True # bool to test whether a better tour was found
    while found and time.clock() - startTime < 60 * MAX_MINUTES:
        found = False
        for i in range(1, len(t) -1):
            for j in range(i+1, len(t)):
                n = swap(t, i, j)
                l = tourLength(n)
                if l < bestLength:
                    bestLength = l;
                    t = n
                    found = True
                    break
            if found:
                break
    return t

# read input file into an array
startTime = time.clock() # start function timer
inputfile = open(str(sys.argv[1]))
lines = inputfile.readlines()
inputfile.close()

# read all cities and store them in an array
cities = []
for line in lines:
    city = [int(n) for n in line.split()] # 0 is the city identifier, 1 is x, 2 is y
    cities.append(city)

# construct the initial tour
cities = neighbor(cities)

# optimize it with twoOpt
cities = twoOpt(cities)

# output results
print(str(tourLength(cities)) + ' | ' + str(time.clock() - startTime) + '\n')
outputfile = open(sys.argv[1] + ".tour", 'w')
outputfile.write(str(tourLength(cities)) + '\n')
for city in cities:
    outputfile.write(str(city[0]) + "\n")
outputfile.close()
