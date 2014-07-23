import csv
import math

import datetime
import ciede2000 as dist

colors = []
header = []
with open('../data/colors.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile)
  header = reader.next()
  for row in reader:
    colors.append([int(r) for r in row])

de2000s = []

timea = datetime.datetime.now()
timeb = datetime.datetime.now()

# need to distribute this on the cluster
for c1 in colors:
  for c2 in colors:
    de2000s.append(c1+c2+[dist.ciede2000(c1,c2)])
  index = colors.index(c1)
  if index % 100 == 0:
    timeb = datetime.datetime.now()
    timediff = timeb - timea
    print index, timediff.seconds
    timea = timeb

with open('distances.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    for de in de2000s:
      writer.writerow(de)

diff = ciede2000([50,2.6772,-79.7751], [50,0,-82.7485])
print 'CIEDE2000 TEST: should result in [50,2.6772,-79.7751], [50,0,-82.7485], 2.0425'
print [50,2.6772,-79.7751], [50,0,-82.7485], diff

print len(de2000s)