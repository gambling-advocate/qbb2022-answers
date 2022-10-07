1. Here it is.

2. I used the following plink code 
`plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3 --out PCAfile`
	The figure is uploaded as `step2.png` and the code for it is in `plots.py`

3. The plink code to generate AF was 
` plink --freq --vcf genotypes.vcf --pca 10 --out PCAfile`
	this outputted a frequency file with column names. I used
	`grep -V 'CHR' PCAfile.frq > PCAfileneeded.frq`
	to remove the column names. And then that didn't work so I used
	`grep -v 'CHR' PCAfile.frq > PCAfileneeded.frq`
	The script for the plot is in `plots.py` and the figure is `step3.png`

4. So we found some flags to use on plink and our final command was
`plink --vcf genotypes.vcf --covar PCAfile.eigenvec --pheno CB1908_IC50.txt --allow-no-sex --linear --out PCAfile`

`plink --vcf genotypes.vcf --covar PCAfile.eigenvec --pheno G5451_IC50.txt --allow-no-sex --linear --out Pheno2`

5 and 6. the code is in plots.py. the figures are uploaded as well.

I think I did something wrong in 6 and was not able to find the right values for number 7.