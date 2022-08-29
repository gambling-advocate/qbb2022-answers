genefile2=/Users/cmdb/data/vcf_files/random_snippet.vcf
echo $genefile2

bedfile2=/Users/cmdb/qbb2022-answers/day1-homework/allthe1s.bed
echo $bedfile2

bedtools intersect -a $genefile2 -b $bedfile2 > intersecthw3.out
