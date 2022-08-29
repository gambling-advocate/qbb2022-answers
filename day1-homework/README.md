# QBB2022 - Day 1 - Homework Exercises Submission

1. for nuc in A C G T
do
```
  echo "Considering " $nuc
  awk -v ver=$nuc '/^#/{next} {if ($4 ==ver) {print $5}}' $1 | sort | uniq -c
```
done

1. The error was with the if statment including a bash variable, which needed to be converted to an awk variable. The results make sense.

2. First, I decided that promoters are not very clearly defined. Then I used the following code to separate out the Stage 1 genes from the chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed file:

```
awk '{if ($4 == 1){print}}' chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > allthe1s.bed
```
2. Then i used bed tools intersect between random snippet vcf and my new bed file.
```
genefile2=/Users/cmdb/data/vcf_files/random_snippet.vcf
echo $genefile2

bedfile2=/Users/cmdb/qbb2022-answers/day1-homework/allthe1s.bed
echo $bedfile2

bedtools intersect -a $genefile2 -b $bedfile2 > intersecthw3.out
```
2. Finally, I used this awk statement to count and find the most common reference allele for C's in the genome.
```
awk '{if ($4 == "C") {print $5}}' intersecthw3.out | sort | uniq -
```

3. The first portion of the awk statement skips the header, then printing columns 1 and 2  then the file variants.bed is created. genes.bed is then sorted and the bedtools closest tool is used to find matches.
the code did not tab delimit and it did not properly sort variants.bed.

```
#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

awk '/^#/{next} {print $1 "\t" $2-1 "\t" $2}' $1 | sort -k1,1 -k2,2n > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed
```

3. 10,293 variants and 4 genes.