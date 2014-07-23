#!/usr/bin/python

import sys
sys.path.append('/home/connor/r/binLab/ciede2000')
import ciede2000 as dist

argv = sys.argv

def distance(L1,a1,b1,L2,a2,b2):
  Lab1 = [float(L1), float(a1), float(b1)]
  Lab2 = [float(L2), float(a2), float(b2)]

  deltaE = dist.ciede2000(Lab1, Lab2)
  outstr = str(L1) + ' ' + str(a1) + ' ' + str(b1) + ' ' + str(L2) + ' ' + str(a2) + ' ' + str(b2) + ' ' + str(deltaE)
  return outstr

fname = '/home/connor/r/binLab/data/colorsPairs'+argv[1]+'.csv'
with open(fname) as csvfile:
  reader = csv.reader(csvfile, delimeter=' ')
  output = [distance(r[0],r[1],r[2],r[3],r[4],r[5]) for r in reader]
  for o in output:
    print o
