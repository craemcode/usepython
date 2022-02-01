"""This program produces the Mandelbort fractal"""
import math
import argparse


"""
using a recursive function is not safe because we can reach recursive limit.
the better solution is a generator because of 1,2,3.



#calculating z using recursion
def calculateZ(n,c):
#n is the number of iterations. c is the next step in recursion
    if n==0:
        return 0
    else: return math.pow(calculateZ(n-1,c), 2) + c
    #for every number c, give recursive values of z. add c to the square of z for the next.


"""
parser = argparse.ArgumentParser("Find out if the number c produces numbers in the mandlebort set!")
parser.add_argument('c', help="number c(seed)", type=float)

args = parser.parse_args()

#calculating z using an generator
def iterateZ(c):
    z = 0
    while True:
        yield z
        z = z**2 + c

for n,z in enumerate(iterateZ(args.c)):
    print(f"z({n}) = {z}")
    if n>= 9:
        break




