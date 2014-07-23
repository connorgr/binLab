import csv
import datetime

from itertools import combinations
from itertools import islice

def split_every(n, iterable):
    i = iter(iterable)
    piece = list(islice(i, n))
    while piece:
        yield piece
        piece = list(islice(i, n))

colors = []
header = []
with open('../data/colors.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile)
  header = reader.next()
  for row in reader:
    colors.append([int(r) for r in row])

print len(colors), 'colors'

timea = datetime.datetime.now()

pairs = [p1+p2 for p1,p2 in combinations(colors, 2)]

pairBins = list(split_every(1000000, pairs))

timeb = datetime.datetime.now()

print len(pairs), 'combinations'
print 'Took', (timeb - timea).seconds, ' seconds'
print 'Writing...'

for bin in pairBins:
  index = str(pairBins.index(bin))
  with open('../data/colorsPairs-'+index+'.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    #Format: ['L1','a1','b1','L2','a2','b2']
    for p in bin:
      writer.writerow(p)

print 'Done.'