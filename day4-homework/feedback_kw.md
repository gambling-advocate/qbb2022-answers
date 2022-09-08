# day 4 homework feedback

Please submit your code

Nice plots overall. It'd be nice if the colorbars were the same (e.g., both had a minimum of 0). I'm guessing that means within the code, you may not have set `vmin` within the `sns.heatmap()` function.

Regarding comments in your README:

* Fantastic job deconstructing that numpy array. Your observations are spot on
* Grayscale is a nice colorblind-friendly palette!
* "For the non corrected p-values there was clear loss of power as sample sizes and probabilities increased." -- I think there was an increase in power actually?
* "For corrected p-values, power remained very strong as probablities became less fair, so long as sample size was very low" -- as long as sample size was very high?
* Yes it essentially was easier to distinguish coins that were more unfair/biased (had a large effect size when compared to a fair coin).
* "we  see stronger power values on the heatmap when we correct p-values." -- we see lower power values?

Power ranges from 0 to 1. A power of 0 is a weak power and says that you never correctly reject the null hypothesis. A power of 1 is strong and says that you correctly reject the null hypothesis every time. a power in between says you correctly reject the null hypothesis that proportion of iterations/tests. (we're correctly rejecting the null hypothesis because the coin is biased (the proportion of heads is not 0.5) and the null hypothesis is that it is not biased (the proportion of heads is 0.5))
