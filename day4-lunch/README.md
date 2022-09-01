1. In the portion of the output where each file is subset, the following is displayed.
Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
1. Using the `cmp` tool in bash allows me to check that there is a difference between the files I produced and the corresponding ones in the cache directory. This was believed to be because of a difference in versions of matplotlib (3.5.3 vs 3.5.1).
1. There are also protein_coding, lncRNA, and miRNA. I think these are interesting as they are able to show us how long proteins genes are, but also where they are located in relation to some of the different RNAs that regualte their expression.
2. We improved the plots by changing the script in plot_vcf_ac.py to:
```
fig, ax = plt.subplots()
ax.hist(ac, density=True )
plt.yscale('log')
ax.set_ylabel("number of occurences")
ax.set_xlabel("allele count")
ax.title.set_text("Log Scale Frequency of Allele Count")
fig.savefig( vcf + ".png" )

fs.close()
```

3. SYNOPSIS
    
	 bxlab/cmdb-plot-vcfs -- plots LogScaled histogram of allele count from variant file. Uses GTF file to select the gene type.

DEPENDENCIES
	
	bedtools(2.30.0), matplotlib(3.5.1 or 3.5.3 work), python3(3.10.4), bash, sys, awk
	
 USAGE
     bash do_all.sh <variant file> <GTF file> ...

 DESCRIPTION
     1. Create .bed files for features of interest
         - Run subset_regions.sh Bash script
         - Use grep to extract only the chromosome number from the uploaded GTF file
		 	- creates a new GTF file from that.
		 	- Use grep to search the new GTF file for the specific gene types listed, prints Allele Count from those rows into and postions into a new bed file.
		 	- Use grep to search for the GTF file for Allele Count in all the rows with Exons.
		 - Use bedtools sort, merge, and intersect all of the bed files created based on gene type and creates a new vcf file from those.
		 - Run plot_vcf_ac.py
		 	- Split all of the lines and removes "AC=" and adds the Allele count value to a a list.
			- Then uses new list as the data for a logscaled histogram.
		- Saves the figure as PNG file.
		
OUTPUT

	EX: 
	```
	*** Creating .bed files for features of interest
	--- Creating exons.chr21.bed
	*** Subsetting .vcf for each feature
	--- Subsetting exons.chr21.bed.vcf
	    + Covering 1107407 bp
	*** Plotting AC for each .vcf
	--- Plotting AC for exons.chr21.bed.vcf
	```