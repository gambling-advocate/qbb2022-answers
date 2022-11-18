#!/usr/bin/env python

import numpy as np
import numpy.lib.recfunctions as rfn
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram
from matplotlib import pyplot as plt
import seaborn as sns
import statsmodels.formula.api
from scipy import stats
import statsmodels.api as sm

#inputting the data into an array
input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
col_names = list(input_arr.dtype.names)
# print(col_names)

#print(input_arr)
#print(col_names)

#creating a list for transcripts:
transcripts = input_arr["t_name"]
#subsetting input_arr
subset = input_arr[col_names[1:]]
#print(subset)


fpkm_values_2d = rfn.structured_to_unstructured(subset, dtype= float)
# print(fpkm_values_2d)

#finding the median for transcripts
submedian = np.median(fpkm_values_2d, axis =1)
# print(submedian)

#finding the row indices where median > 0
filtermedian = np.where(submedian > 0)[0]
processed_arr = fpkm_values_2d[filtermedian]
pro_trans = transcripts[filtermedian]
# print(processed_arr)
# print(pro_trans)

#log transforming the values of the data
waterlogged = np.log2(processed_arr + 0.1)
# print(waterlogged)
# print(waterlogged.shape)
#print(pro_trans.shape)

#using linkage to cluster data
genes = linkage(waterlogged, 'single')
samples = linkage(waterlogged.T, 'single')
# print(zelda)

link = leaves_list(genes)
zelda = leaves_list(samples)
# print(zelda2)

rearrange = waterlogged[link]
rearrange = waterlogged.T[zelda]
# print(rearrange)

# fig = plt.figure(figsize=(25,10))
# dylan = np.array(col_names[1:])[zelda]
# dendrogram(genes, labels = dylan)
# print(dylan)
# plt.title("Relatedness of Samples")
# plt.tight_layout()
# # plt.show()
# plt.savefig("Samples_dend.png")

# ax = sns.heatmap(rearrange)
# plt.show()
# plt.savefig("clustered_genes_heatmap.png")

p_val = []
betaval = []
sexes = []
stages = []

for s in col_names[1:]:
    sexes.append(s.split('_')[0])
    stages.append(s.split('_')[1])
# print(sexes)
# print(stages)
for i in range(waterlogged.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names[1:])):
        list_of_tuples.append((transcripts[i], waterlogged[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    model = statsmodels.formula.api.ols(formula = 'fpkm ~ 1 + stage' , data = longdf, subset=None, drop_cols=None)
    results = model.fit()
    p_val.append(results.pvalues)
print(results.pvalues)