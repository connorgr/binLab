#!/bin/bash

colorsFile="../data/colorsTestPairs.csv"
outFile="../data/distanceTest.csv"

touch $outFile
> $outFile

cat $colorsFile | while read line
do
  dist=$(python clusterComputeDistance.py $line)
  echo $dist >> $outFile
done