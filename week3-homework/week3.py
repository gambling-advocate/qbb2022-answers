#!/bin/bash 

#steps 1-3
for value in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do
    bwa mem -t 4 -R "@RG\tID:${value}\tSM:${value}" sacCer3.fa ${value}.fastq > ${value}.sam
    samtools sort -@ 4 -o ${value}.bam ${value}.sam
	samtools index -b ${value}.bam
done

#step 4
$freebayes -f sacCer3.fa --genotype-qualities *.bam > dylans_darling.vcf 

#step 5
$vcffilter -f "QUAL > 20" dylans_darling.vcf > dylans_darling2.vcf

#step 6
$vcfallelicprimitives -k -g dylans_darling2.vcf > dylans_darling3.vcf

#step 7
snpeff ann dylans_darling3.vcf > dylans_darling4.vcf

#step 8
code uploaded as `week3python.py`
