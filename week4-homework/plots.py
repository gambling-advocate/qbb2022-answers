#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

# plinkpca = np.genfromtxt("PCAfile.eigenvec", dtype = None, encoding = None, names = ["col1", "col2", "col3", "col4", 'col5', 'col6', 'col7', ' col8', 'col9', 'col10', 'col11', 'col12'])
#
# # print(plinkpca)
#
# id1 = plinkpca["col3"]
# id2 = plinkpca["col4"]
#
# fig, ax = plt.subplots()
# ax.scatter(id1,id2)
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# ax.set_title('PCA1 vs PCA2')
# ax.legend()
# plt.show()
# plt.savefig("step2.png")


# allelefreq = np.genfromtxt("PCAfileneeded.frq", dtype = None, encoding = None, names = ["col1", "col2", "col3", "col4", 'col5', 'col6'])
#
# id3 = allelefreq['col5']
# # print(id3)
#
# fig, ax = plt.subplots()
# ax.hist(id3)
# ax.set_title('Frequency of Allele Frequency')
# plt.savefig('step3.png')
#plt.show()

#CB1908
# pheno1 = open("PCAfile.assoc.linear")
# bp_1 = []
# pval_1 = []
# chrom_1 = []
# pvalRaw_1 = []
# pos_1 = []
# for line in pheno1:
#     new = line.rstrip("\n").split()
#     if new[4] == "ADD":
#         bp_1.append(int(new[2]))
#         pval_1.append(-1 * np.log10(float(new[8])))
#         pvalRaw_1.append(float(new[8]))
#         chrom_1.append(int(new[0]))
# for i, item in enumerate(bp_1):
#     pos_1.append(i)
# sigpval_1 = []
# sigpos_1 = []
# for p, thing in enumerate(pval_1):
#     if thing > 5:
#         sigpval_1.append(item)
#         sigpos_1.append(pos_1[p])
# xtick_1 = []
# for i in range(1, 23):
#     first_pos = None
#     last_pos = None
#     for c, item in enumerate(chrom_1):
#         if item == i:
#             if first_pos == None:
#                 first_pos = c
#             if last_pos == None or c > last_pos:
#                 last_pos = c
#     middle = (last_pos + first_pos)/2
#     xtick_1.append(middle)
#
# fig, ax = plt.subplots(figsize = (10, 6))
# ax.scatter(pos_1, pval_1)
# ax.scatter(sigpos_1, sigpval_1, color = "red")
# ax.set_xticks(xtick_1)
# ax.set_xticklabels(range(1, 23))
# ax.set_xlabel("Chrom Position")
# ax.set_ylabel("-log10(pval)")
# ax.set_title("Manhattan CB1908")
# fig.savefig("CB1908_Manhat.png")
# plt.show()

# G5451
pheno2 = open("Pheno2.assoc.linear")
bp_2 =[]
pval_2 = []
chrom_2 = []
snp_2 = []
pvalRaw_2 = []
for line in pheno2:
    new = line.rstrip("\n").split()
    if new[4] == "ADD":
        bp_2.append(int(new[2]))
        pval_2.append(-1 * np.log10(float(new[8])))
        pvalRaw_2.append(float(new[8]))
        chrom_2.append(int(new[0]))
        snp_2.append(new[1])

pos_2 = []
for i, item in enumerate(bp_2):
    pos_2.append(i)

sigpval_2 = []
sigpos_2 = []
for p, item in enumerate(pval_2):
    if item > 5:
        sigpval_2.append(item)
        sigpos_2.append(pos_2[p])
xtick_2 = []
for i in range(1, 23):
    first_pos = None
    last_pos = None
    for c, item in enumerate(chrom_2):
        if item == i:
            if first_pos == None:
                first_pos = c
            if last_pos == None or c > last_pos:
                last_pos = c
    middle = (last_pos + first_pos)/2
    xtick_2.append(middle)

fig, ax = plt.subplots(figsize = (10, 6))
ax.scatter(pos_2, pval_2)
ax.scatter(sigpos_2, sigpval_2, color = "red")
ax.set_xticks(xtick_2)
ax.set_xticklabels(range(1, 23))
ax.set_xlabel("Chrom Position")
ax.set_ylabel("-log10(pval)")
ax.set_title("Manhattan G5451")
# fig.savefig("G5451_Manhat.png")
# plt.show()



# Step 6 for CB1908
ref = []
het = []
alt = []
min_val = min(pval_2)
position = pval_2.index(min_val)
significant = snp_2[position]
sigbp = bp_2[position]
sigchrom = chrom_2[position]
genotypes = []
sampleid = []

gene_file = open("genotypes.vcf")
pheno_file = open("CB1908_IC50.txt")
for i in gene_file:
    if i.startswith("##"):
        continue
    gene_list = i.rstrip("\n").split("\t")
    if gene_list[2] == significant:
        genotypes = gene_list[9:]
    if i.startswith("#"):
        sampleid = gene_list[9:]
new_dict = dict(zip(sampleid, genotypes))
for i in pheno_file:
    if i.startswith("F"):
        continue
    pheno_list = i.rstrip("\n").split("\t")
    id_A = pheno_list[0]
    id_B = pheno_list[1]
    combined =id_A + "_" + id_B
    if pheno_list[2] == "NA":
        continue
    sample_val =float(pheno_list[2])
    gt = new_dict[combined]
    if gt == "0/0":
        ref.append(sample_val)
    if gt == "0/1":
        het.append(sample_val)
    if gt == "1/1":
        alt.append(sample_val)
fig, ax = plt.subplots()
ax.boxplot([ref, het, alt])
ax.set_xlabel("Genotype")
ax.set_ylabel("Phenotype")
plt.xticks([1, 2, 3], ["Hom_Ref", "Het", "Hom_Alt"])
fig.savefig("CB1908_box.png")
plt.show()

