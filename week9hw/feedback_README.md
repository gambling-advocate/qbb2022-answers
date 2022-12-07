Great start! A few things before this is complete:
1. When you're clustering the fpkm array by transcript and sample, the way you have it right now is that you're clustering by gene, and then *overwriting* that by clustering by sample. You should use the "clustered by transcript" array as input when you cluster by sample. (no points deducted)
2. Your labels for the dendrogram and heatmap are a bit funky. I think when you use the `labels` argument in the dendrogram function, it automatically rearranges the labels, so you don't actually have to do that on your end (no points deducted)
3. You've got a good start on the regression. You'll want to subset the `results.pvalues` to just the p-values associated with stage, by doing `results.pvalues['stage']`. Don't forget to get the betas for the regression as well. Plot the pvalues distribution on a QQ plot (-1 point)
4. After running the regression on stage, run a second model regression fpkm onto both stage and sex. Do FDR correction on both this model and the "stage-only" model, and then compare the significant genes between the two models (-2 points)
5. Finally, make a volcano plot of the results from the "stage+sex" model (-1 point)

Good work, so far!
(6/10)
