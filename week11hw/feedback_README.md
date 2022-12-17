This all looks really good, Kaven. I think the only issue with "renaming" your clusters is in the column name for your clusters. When you do leiden clusters, it creates a column called `leiden` unless you specifically tell it to name the column something else. The line you have right now : `adata.obs['cell type'] = adata.obs['clusters'].map(annotation).astype('category')` is trying to use a column called `clusters`, which as far as I know, doesn't exist in the data frame. If you replace that with `leiden` (or rename the column to `clusters`) it should work just fine. (-0.5 point)

(9.5/10)
