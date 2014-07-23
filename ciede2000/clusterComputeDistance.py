#!/usr/bin/python

import sys
import ciede2000 as dist

argv = sys.argv

if len(argv) != 7:
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
outstr = L1 + ' ' + a1 + ' ' + b1 + ' ' + L2 + ' ' + a2 + ' ' + b2 + ' ' + deltaE
print outstr
