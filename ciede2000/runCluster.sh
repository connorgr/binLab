#!/bin/bash

colorsFile="/home/connor/r/binLab/data/colorsPairs.csv"
outFile="/home/connor/r/binLab/data/distanceTest.csv"

touch $outFile
> $outFile

cat $colorsFile | while read line
do
  dist=$(python /home/connor/r/binLab/ciede2000/clusterComputeDistance.py $line)
  echo $dist >> $outFile
done
