RNA sequence Analysis Pipeline using Python

This repository contains an end-to-end RNA-seq analysis pipeline implemented in Python.
The pipeline implements bioinformatics concepts by using real public data from NCBI GEO.

The purpose of this project is to perform;
1- RNA-seq count data structure
2- Gene filtering
3- Library-size normalization (CPM)
4- Log2 transformation
5- Metadata-driven sample grouping
6- Log2 fold-change calculation

Dataset used is obtained from NCBI Gene Expression Omnibus (GEO) having the accession number GSE60424.

The dataset contains bulk RNA-seq gene count data from purified human immune cell types, including:
- Whole Blood
- Neutrophils
- Monocytes
- B cells
- CD4 T cells
- CD8 T cells
- NK cells

Two files are used:
- "GSE60424_counts.txt" – gene × sample raw count matrix
- "GSE60424_series_matrix.txt" – sample metadata (cell type annotations)

Analysis

For demonstration, differential expression is approximated by comparing:

 Control: CD4 T cells  
 Treatment: CD8 T cells  

Pipeline Overview

1. Load gene-level count matrix  
2. Parse GEO series matrix to extract cell-type metadata  
3. Group samples by cell type  
4. Filter low-expression genes  
   - Keep genes with ≥10 counts in at least 2 samples  
5. Normalize counts using CPM (Counts Per Million)  
6. Log2-transform normalized values  
7. Compute group-wise mean expression  
8. Calculate log2 fold change (CD8 − CD4)  
9. Save results to CSV  



