#!/usr/bin/env python3

import matplotlib.pyplot as plt
from vcfParser import parse_vcf

most = parse_vcf("dylans_darling4.vcf")[1:]

qual = [i[5] for i in most]
dp = [j[7]["DP"] for j in most]
af = [k[7]["AF"] for k in most]
ann = [z[7]["ANN"].split("|")[2] for z in most]
anns = list(set(ann))
annsa = [ann.count(v) for v in anns]
print(annsa)

fig, ax = plt.subplots(nrows=4)
ax[0].hist(qual)
ax[0].set_title("Qual Values")

ax[1].hist(dp)
ax[1].set_title("Read Depth")

ax[2].hist(af)
ax[2].set_title("Allele Frequency")

ax[3].bar(anns, annsa)
ax[3].set_title("Predicted effects")
plt.tight_layout()
plt.savefig("Week3graphs.png")


# most = parse_vcf("dylans_darling4.vcf")[1]
# print(most[7]["ANN"].split("|")[9])