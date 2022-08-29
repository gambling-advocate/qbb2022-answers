# QBB2022 - Day 1 - Lunch Exercises Submission
1. I'm excited to learn python and bash.

2. a) To copy the files, I first used `cd` and `cp`:

```
cd ~/data/bed_files
cp genes.chr21.bed ~/qbb2022-answers/day1-lunch/
cp exons.chr21.bed ~/qbb2022-answers/day1-lunch/
cd ../../qbb2022-answers/day1-lunch/
```

2. b) I then used wc -l to find the number of exons and genes and divded the two to get 62.3:

```
wc -l exons.chr21.bed
wc -l genes.chr21.bed
```
2. c) to find the median I would first check the positions of each exon and ensure that it's start and end corresponds to being located within the start and end of a gene. Creating a new list with that count that includes all genes and exons in between them, I would use a command to find the middle point of that list.

3. a) to copy the files:

```
cd ~/data/bed_files
cp chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed ~/qbb2022-answers/day1-lunch/
cd ../../qbb2022-answers/day1-lunch/
```
3. b) to count i used the below command, total counts were 1:305; 2:678; 3:79; 4:377; 5:808; 6:146; 7:1050; 8:156; 9:654; 10:17; 11:17; 12:30; 13:62; 14:228; 15:992.
```
cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort -g | uniq -c
```

3. c) First I would take the difference between the 3rd and 2nd column for all the lines in all the different states. Then i would add those differences together and see which state had the largest sum.