import csv
import datetime

from itertools import combinations

colors = []
header = []
with open('../data/colorsTest.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile)
  header = reader.next()
  for row in reader:
    colors.append([int(r) for r in row])

print len(colors), 'colors'

timea = datetime.datetime.now()

pairs = [p1+p2 for p1,p2 in combinations(colors, 2)]

timeb = datetime.datetime.now()

print len(pairs), 'combinations'
print 'Took', (timeb - timea).seconds, ' seconds'
print 'Writing...'

with open('../data/colorsTestPairs.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter=' ')
  #Format: ['L1','a1','b1','L2','a2','b2']
  for p in pairs:
    writer.writerow(p)

print 'Done.'