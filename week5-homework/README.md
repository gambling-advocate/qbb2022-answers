# Part 1: ChIP-seq analysis

1. I used the following 4 commands.
```
samtools view -o "D2_Sox_R1_first.bam" -q 10 -b D2_Sox2_R1.bam
samtools view -o "D2_Sox_R2_first.bam" -q 10 -b D2_Sox2_R2.bam
samtools view -o "D2_Sox_R1_inputsam.bam" -q 10 -b D2_Sox2_R1_input.bam
samtools view -o "D2_Sox_R2_inputsam.bam" -q 10 -b D2_Sox2_R2_input.bam
```

2. To call the peaks I used:
```
macs2 callpeak -t D2_Sox_R1_first.bam -c D2_Sox_R1_inputsam.bam -g 94987271 -B -n "R1files"
macs2 callpeak -t D2_Sox_R2_first.bam -c D2_Sox_R2_inputsam.bam -g 94987271 -B -n "R2files"
```

3. I used this command!
```
bedtools intersect -a R1files_peaks.narrowPeak -b R2files_peaks.narrowPeak > intersectr1r2.bed
```
4. I used word count on the Sox2 intersect file and intersected that file with my Klf4 peaks file.

```
wc -l intersectr1r2.bed
wc -l D2_Klf4_peaks.bed 
bedtools intersect -a intersectr1r2.bed -b D2_Klf4_peaks.bed > total_intersect.bed
wc -l total_intersect.bed
```
I got 593 Sox2 peaks, 60 Klf4 peaks, and 40 overlaps between the two of them.

5. I cropped and scaled the 4 files with the following commands:
```
python scale_bdg.py D0_H3K27ac_treat.bdg D0_H3K27ac_scaled.bdg 
python scale_bdg.py D2_H3K27ac_treat.bdg D2_H3K27ac_scaled.bdg 
python scale_bdg.py D2_Klf4_treat.bdg D2_Klf4_scaled.bdg 
python scale_bdg.py R1files_treat_pileup.bdg R1files_treat_scaled.bdg

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' R1files_treat_scaled.bdg > R1files_treat_scaled_and_cropped.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D0_H3K27ac_scaled.bdg > D0_H3K27ac_scaled_and_cropped.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_Klf4_scaled.bdg > D2_Klf4_scaled_and_cropped.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_H3K27ac_scaled.bdg > D2_H3K27ac_scaled_and_cropped.bdg
```

#Part 2: motif finding

1. hear are my commands needed for these steps.
```
sort -k 5 R2files_peaks.narrowPeak | head -300 > R2files_peaks_sorted.narrowPeak
awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' R2files_peaks_sorted.narrowPeak > R2files_peaks_awked.narrowPeak
samtools faidx -r R2files_peaks_awked.narrowPeak mm10.fa > R2files_samtools.narrowPeaks
meme-chip R2files_samtools.narrowPeaks > R2files_motifs.narrowFiles
```

#Part 3: Motif Identification

I used the following commands:
```
mv ~/Downloads/motif_databases
tomtom memechip_out/combined.meme motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme
open tomtom.html
less tomtom.tsv 
grep "SOX2\|KLF4" tomtom.tsv 
```
I got the following results:
`1	KLF4_MOUSE.H11MO.0.A	2	6.4185e-05	0.0340822	0.0059992	CCCACCCA	GCCACACCCACTCCA	-`


