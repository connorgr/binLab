import csv
from subprocess import call

with open('../data/colorsTestPairs.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile)
  pairs = []
  for r in reader:
    pairs.append(r[0])
    call('./clusterComputeDistance.py '+ r[0], shell=True)
