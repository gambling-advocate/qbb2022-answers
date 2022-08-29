#!/bin/bash

#USAGE: bash exercise1.sh input_VCF

for nuc in A C G T
do
  echo "Considering " $nuc
  awk -v ver=$nuc '/^#/{next} {if ($4 ==ver) {print $5}}' $1 | sort | uniq -c
done
