#Part 0: base locations
chr11   1900000 2800000
chr14   100700000    100990000
chr15   23600000        25900000
chr20   58800000        58912000

#Part 1: Call and phase variant
```
medaka_variant -i methylation.bam -f hg38.fa -r chr11:1900000-2800000 -p -o "chr11medaka"

medaka_variant -i methylation.bam -f hg38.fa -r chr14:100700000-100990000 -p -o "chr14medaka"

medaka_variant -i methylation.bam -f hg38.fa -r chr15:23600000-25900000 -p -o "chr15medaka"

medaka_variant -i methylation.bam -f hg38.fa -r chr20:58800000-58912000 -p -o "chr20medaka"
```

#Part 2: Mark reads with haplotype tag

```
whatshap haplotag -o coolChr11 -r hg38.fa --regions chr11:1900000:2800000 --output-haplotag-list chr11haplotags chr11medaka/round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o coolChr14 -r hg38.fa --regions chr14:100700000:100990000 --output-haplotag-list chr14haplotags chr14medaka/round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o coolChr15 -r hg38.fa --regions chr15:23600000:25900000 --output-haplotag-list chr15haplotags chr15medaka/round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o coolChr20 -r hg38.fa --regions chr20:58800000:58912000 --output-haplotag-list chr20haplotags chr20medaka/round_0_hap_mixed_phased.vcf.gz methylation.bam
```
#Part 3: Split reads into two files based on their haplotype

```
whatshap split --output-h1 chr11final1 --output-h2 chr11final2 coolChr11 chr11haplotags

whatshap split --output-h1 chr14final1 --output-h2 chr14final2 coolChr14 chr14haplotags

whatshap split --output-h1 chr15final1 --output-h2 chr15final2 coolChr15 chr15haplotags

whatshap split --output-h1 chr20final1 --output-h2 chr20final2 coolChr20 chr20haplotags

samtools cat -o AllH1s.bam chr11final1 chr14final1 chr15final1 chr20final1
 
samtools cat -o AllH2s.bam chr11final2 chr14final2 chr15final2 chr20final2

samtools index AllH1s.bam

samtools index AllH2s.bam
```

#Part 6: Find and plot methylated regions
all images are uploaded under their chromosome names. Except for some reason, even though my file length is about 