#!/usr/bin/python

import sys
sys.path.append('/home/connor/r/binLab/ciede2000')
import ciede2000 as dist

argv = sys.argv

if len(argv) != 7:
  print argv
  raise Exception("clusterComputeDistance.py requires two sets of L*a*b* values.")

L1 = float(argv[1])
a1 = float(argv[2])
b1 = float(argv[3])

L2 = float(argv[4])
a2 = float(argv[5])
b2 = float(argv[6])

Lab1 = [L1, a1, b1]
Lab2 = [L2, a2, b2]

deltaE = dist.ciede2000(Lab1, Lab2)
outstr = str(L1) + ' ' + str(a1) + ' ' + str(b1) + ' ' + str(L2) + ' ' + str(a2) + ' ' + str(b2) + ' ' + str(deltaE)
print outstr
