This is definitely a great start. There are a couple of weird things going on, so let me see if I can point you in the right direction!

1. For the PCA plot, I don't actually see your plot, but I ran your code and it works, so no worries there. The plink command you have in your README is super weird though, because you're using a different vcf file than the one we gave you, so I'm wondering if  you copied this bit from `day3-homework`. Your second plink command actually makes the PCA correctly though.
2. For the AF plot, I again don't see your plot, but your code is a little funky here. I think because you're not skipping the header line when you read in the `.frq` file, the dataype of the MAF is set to string. And then when you plot it, you're actually plotting the distribution of the different *strings* in that column, rather than the actual numerical values. That's why your x-axis labels are just a black line. (-0.5 point)
3. For the manhattan plots, your GS451 plot looks good, but the CB1908 plot doesn't. I think you've got an error in this for loop:
```
for p, thing in enumerate(pval_1):
    if thing > 5:
        sigpval_1.append(item)
        sigpos_1.append(pos_1[p])
```
I think you want to do `sigpval_1.append(thing)`, otherwise it will keep setting it as whatever the last value of `item` was from the previous for loop. (-0.5 point)
4. For the boxplot, there's actually two different things going on here. First, you're mixing the pvals from GS451 with the phenotypes for CB1908. But! There's another issue as well. You're finding the most significant pval by doing `min_val = min(pval_2)`, but `pval_2` is your logged pvals, so you're actually finding the *least* significant pval and plotting that. That's why your boxplot makes it look like there's not a strong association (-0.5 point).
5. We still need your answer for question 7, but hopefuly what I've given you here helps! (-1 point)

Really good start, you're almost there.

(7.5/10)
