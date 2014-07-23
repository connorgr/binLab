import csv
from subprocess import call

for i in range(34):
  gridOutDir = '/home/connor/r/binLab/data/grid'
  qsub = 'qsub -cwd -N "colorDistance" -V -e '+gridOutDir+' -o '+gridOutDir+' -l inf '
  app = '/home/connor/r/binLab/ciede2000/runBrownDistance.py '+ str(i)
  call(qsub+app, shell=True)

# with open('../data/colorsTestPairs.csv', 'rb') as csvfile:
#   reader = csv.reader(csvfile)
#   pairs = []
#   for r in reader:
#     pairs.append(r[0])
#     gridOutDir = '/home/connor/r/binLab/data/grid'
#     qsub = 'qsub -cwd -N "colorDistance" -V -e '+gridOutDir+' -o '+gridOutDir+' -l inf '
#     app = '/home/connor/r/binLab/ciede2000/runBrownDistance.py '+ r[0]
#     call(qsub+app, shell=True)
    #call('./clusterComputeDistance.py '+ r[0], shell=True)
