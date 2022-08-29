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


