#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    
    fuel, position = 0, 0
    negatives_fuel = 0
    for i in range(0, len(petrolpumps)):
        fuel = fuel + petrolpumps[i][0] - petrolpumps[i][1]
        if fuel < 0:
            negatives_fuel -= fuel
            fuel = 0
            position = i + 1
    
    if position >= len(petrolpumps):
        return -1
    
    if fuel + negatives_fuel >= 0:
        return position
    return -1
    
    

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
