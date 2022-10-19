# Week 1 Genome Assembly -- Feedback

1 + 1 + 1 + 1 + 0.5 + 1 + 1 + 0.9075 + 1 + 1 = 9.41 points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * good --> +1

2. Question 1.2, 1.4 simulation script(s)

  * very good --> +1

3. Question 1.2, 1.4 plotting script(s)

  * personally, rather than passing the `poisson.pmf` function `x`, I would have just passed it an array of x-tick-values like [0, 1, 2, 3, 4, ...] so something like `range(0, max(x)+1)`
  * consider having one script for the simulation and plotting where you change the number of reads that are simulated, etc. using `sys.argv`
  * very good --> +1

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * Consider adding plot titles in order to distinguish the 5x from the 15x coverage
  * good plots overall --> +1

5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * poisson expectation and how that compares to your observations? --> +0.5

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.5
  * total length of contigs --> +0.5

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.5
  * contig n50 size --> +0.5, great explanation

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> number of deletions? 0.2475 (+ 0.33/4 for half answer + 0.33/2 for explanation/code)

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> +0.5
  * length of novel insertion --> +0.5

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +1
  * secret message --> +1
