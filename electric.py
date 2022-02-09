"""Simple python to automate the boring stuff

This script calculates the electric potential at a point r away
from away from a charge point Q.

"""
import math
import argparse

parser = argparse.ArgumentParser(
 'This script calculates the electric potential at a point r awayfrom away from a charge point Q.')

#parser.add_argument("charge", type=float)
parser.add_argument('dist', help="distance from charge point in meters",type=float)
#parser.add_argument("simulated", type=float)
#parser.add_argument("calculated", type=float)
args = parser.parse_args()

#cols = args.charge
metres = args.dist
#simulated = args.simulated
#calculated = args.calculated

def calculatePotential(r,Q=1):
      
    constant = 9 * (math.pow(10,9))
    charge = Q * (math.pow(10,-9))
    dist = r

    voltage = (constant * charge)/dist

    return round(voltage,3)

def calculateField(r,Q=1):
    constant = 8.99 * (math.pow(10,9))
    charge = Q * (math.pow(10,-9))
    dist = r

    field = (constant * charge)/math.pow(dist,2)

    return round(field,2)
    

def calculateError(sim,cal):
    error = ((cal-sim)/cal) * 100
    return abs(round(error, 2))




#print("voltage = ", calculatePotential(metres))
print("field: ", calculateField(metres))
#print("error: ", calculateError(simulated, calculated))
