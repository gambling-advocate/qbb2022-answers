#! usr/bin/env python

import scanpy as sc
import pandas
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

#making unfiltered PCA plot
# sc.tl.pca(adata, n_comps=None, zero_center=True, svd_solver='arpack', random_state=0, return_info=False, use_highly_variable=None, dtype='float32', copy=False, chunked=False, chunk_size=None)
#
# sc.pl.pca(adata, save = "BFPCA.png")


#making filtered PCA plot using Zheng method
sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True)

sc.tl.pca(adata, n_comps=None, zero_center=True, svd_solver='arpack', random_state=0, return_info=False, use_highly_variable=None, dtype='float32', copy=False, chunked=False, chunk_size=None)

# sc.pl.pca(adata, save = "FiltPCA.png")

#using leiden to cluster 
sc.pp.neighbors(adata)
sc.tl.leiden(adata)

#making a tsne
# sc.tl.tsne(adata)
# sc.pl.tsne(adata, save = "LeidentSNE.png", color = "leiden")

#Making a umap
# sc.tl.umap(adata, maxiter = 1000)
# sc.pl.umap(adata, save = "LeidenUMAP.png", color = 'leiden')


#running a t test
# sc.tl.rank_genes_groups(adata, "leiden")
# sc.pl.rank_genes_groups(adata, save = "t-test.png")

#running logistic regression
sc.tl.rank_genes_groups(adata, "leiden", method = 'logreg')
# sc.pl.rank_genes_groups(adata, save = "log_regression.png")

#making a dotplot to mark the marker genes
sc.pl.rank_genes_groups_dotplot(adata, n_genes = 4, save = "dotplots.png")

#creating a dictionary for the labels.

annotation = {
    '21': 'OL',
    '25': 'PC',
    '26': 'MG',
    '16': 'EC',
    '4': 'FB2',
    '13': 'AC',
}

adata.obs['cell type'] = adata.obs['clusters'].map(annotation).astype('category')
sc.pl.umap(adata, color='cell type', legend_loc='on data',
           frameon=False, legend_fontsize=10, legend_fontoutline=2)



#Data from database:
#Olig1 and Olig2 are mostly enriched in oligodendrocytes (shocker). I think cluster 21 is Oligodendrocytes.
#Abcc9 and Higd1b are mostly enriched in pericytes. I think cluster 25 is pericytes.
#Fcgr3 and C1qb is mostly enriched in Microglia. I think cluster 26 is microglia
#The Hbb and Hba genes are mostly enriched in EC cells. I think that's what cluster 16 is.
#I think cluster 4 is fibroblast like type 2 cells because of the enrichment of crym and nrp2 cells.
#Nefm and Nefl are mostly enriched in astrocytes, which is what I think cluster 13 is.