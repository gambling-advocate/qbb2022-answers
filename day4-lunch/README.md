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