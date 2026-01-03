#IMPORTS

import pandas as pd
import numpy as np
from collections import defaultdict


# 1. Loading the Count Matrix

counts_file= "GSE60424_counts.txt"
df= pd.read_csv(
    counts_file,
    sep=r"\s+",
    index_col=0
)

#print(df)
print("Count matrix shape:", df.shape)


# 2. Parse GEO metadata

series_file = "GSE60424_series_matrix.txt"
sample_names=[]
cell_types=[]

with open(series_file) as f:
    for line in f:
        
        if line.startswith("!Sample_title"):
            sample_names=[x.strip('"')
            for x in line.strip().split("\t")[1:]] 

        if line.startswith("!Sample_characteristics_ch1") and ("celltype:") in line.lower():
            cell_types=[x.split("celltype:")[-1].strip().strip('"')
            for x in line.strip().split("\t")[1:]]
#print(sample_names)
#print(cell_types)

# -> Sanity Check
assert len(sample_names) == len(cell_types)
assert len(sample_names) == df.shape[-1]


# 3. Grouping cell types

groups = defaultdict(list)

for sample,cell in zip(sample_names,cell_types):
    groups[cell].append(sample)
print("Sample count per cell type")
for cell, libs in groups.items():
    print(cell,"->",len(libs))
    

# 4. Control and Treatment

control=groups["CD4"]
treatment=groups["CD8"]

# -> Sanity Check
assert set(control).issubset(df.columns)
assert set(treatment).issubset(df.columns)
assert len(control) == len(treatment)

print("Control: ",len(control))
print("Treatment:",len(treatment))


# 5. Filter out Low Expression Genes

mask = (df>=10).sum(axis=1) >= 2
df_filtered= df[mask]

print(df_filtered.shape)


# 6. Cpm Normalisation

library_sizes = df_filtered.sum(axis=0)
df_cpm= df_filtered.div(library_sizes,axis=1)* 1_000_000
#print(df_cpm)
#print(library_sizes)


# 7. log 2 Transformation

df_log2 = np.log2(df_cpm+1)


# 8. Differential Expression

control_mean= df_log2[control].mean(axis=1)
treatment_mean = df_log2[treatment].mean(axis=1)

df_de = pd.DataFrame({
    "Control Mean": control_mean,
    "Treatment Mean": treatment_mean,
    "Log2FC": treatment_mean - control_mean 
})
df_de

# 9. Result

df_de.to_csv("GSE60424_CD4_vs_CD8_log2FC.csv")
#print(df_de.head())