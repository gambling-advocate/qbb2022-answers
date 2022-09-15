1.1 1,000,000bp * 5x coverage = 5Mbp
	5Mbp / 100bp/read = 50,000 reads 
	150,000 reads for 15x coverage

1.2 did it, code uploaded in question1.py

1.3 7018 is the toatl number, I used np.count_nonzero to total up the amount zero values in my array, here is that code:
```
x = np.array(genome)
zero = x == 0
meh = np.count_nonzero(zero)
```
1.4 did it, code uploaded in question1_4.py and histograms. I got about 8 bp not covered

2.1 4 contigs were produced 

2.2 So for the total length of the contigs, I used the following command instead of samtools.
`grep -v '>' contigs.fasta | wc` and then got  238,377 nucelotides, however this included the 3,190 new lines. So the total is 234,467 nucleotides.

2.3 The largest contig size was 105,830 nucleotides. `grep '>' contigs.fasta`

2.4 So the total size of the genome is 238,377. 50% of that is 124,188. This falls into contig 2, with a size of 47860.

3.1 The percent identity as determined using `dnadiff` was 99.98%

3.2 Nucmer produced a file that gave us the coordinates where the reference file and query file matched up. This told us where the query file had an insertion, as the alignment of the coordinates would be off at that location. The longest alingment was 206,999 nucleotides

3.3 Dnadiff reported one insertion in the query.

4.1 The insertion starts at 26,788. 

4.2 The length of the insertion is 710 nucleotides long.

4.3 The DNA sequence is:

ATACAATGCGTATTGTAGTATGGCCTTACGGGAGGGCAGACGGCAAAGAGTGATCACGTT
CTATCGGATGCAAGGCACCGCTTTATCCATTAGCCTCTTATTGGAGGAGGGCATGGCATT
CATACCCAATGGCTCAATTCTTTTACTACAACATTGATAACTTATCCAAGTACTCTACGA
CCAACCTGCAGAACGGCCCACCGGCCTAACGGCATACCTCACAACTACCCTGCTAAGGCG
AGCACTCCAGCCAAGCAAGACCACATCCACCCAAGCCCACCTCATCGCCTCAGCCAATAG
CGCTCAGACAAAAGGAACTTATTATTAACTGAAACGCTGTACTGCGGTAAGTCCTCAACG
CCGACCAAACGAAACCAGCAGCGTAGTCCTATCGGACTCGCTTGCACACATAACACATGC
TTGTAGTCTTGCACGACCCCAGGCGGACATGAGTTTCTGCTGGGCGGCGAGGAGTCGAAG
CTGCGGGCATTCCTTTCCGAAAACATGAATTACTGCGGGTATGTCCGACCTCAAACATTC
GTACCTGAGCATATTGCTCAAGTGAGCCAGTCGGCAATTCATATCCGAAAACATGACTGT
CTTGCATAAGGCCTCTCTTACGAGCTGAGTGCACGAACCACGGAACAGCTTAGTCACTTA
GAAGAGTACTCTATTCGGGACTTGAAGTACGCGTGCAATCGGGAACTAGTG

4.4 The decoded message was achieved with this command:
`python dna-decode.py -d --input contigfinal.txt`

 Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens..