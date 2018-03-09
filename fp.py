#!/usr/bin/env python3

import sys
from math import sqrt, pow

# make sure we received the right number of arguments
if len(sys.argv) < 2:
    print("error, no file name specified")
    print("correct usage: python3 fp.py [filename.txt]")
    sys.exit()

# this function creates an initial tour using nearest neighbor
def neighbor(c):


# this function returns the euclidean distance between cities a and b
def distance(a, b):
    return int(round(sqrt(pow(a[1]-b[1],2) + pow(a[2]-b[2],2))))

# this function computes the total length of a given tour
def tourLength(t):
    length = 0
    for n in range(len(t) - 1):
        length += distance(t[n], t[n+1])
    length += distance(t[len(t) - 1], t[0])
    return length

# this function performs a 'swap' between cities a and b in tour t
def swap(t, a, b):


# this function contains the 2-opt algorithm that optimizes our tour
def twoOpt(t):
    

# read input file into an array
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
outputfile = open(sys.argv[1] + ".tour", 'w')
outputfile.write(str(tourLength(cities)) + '\n')
for city in cities:
    outputfile.write(str(city[0]) + "\n")
outputfile.close()
