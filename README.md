#### **RNA-seq Analysis Pipeline (Python, GEO)**



###### **Overview**



This repository contains an end-to-end RNA-seq analysis pipeline implemented in Python, using real public data from the Gene Expression Omnibus (GEO).



###### **Purpose of This Project**



High-throughput RNA sequencing (RNA-seq) is widely used to measure gene expression across different biological conditions. However, meaningful interpretation of RNA-seq data depends on correct sample annotation, normalization, and comparison. 

The biological purpose of this project is to compare gene expression patterns between distinct human immune cell types using publicly available RNA-seq data.



**The project demonstrates:**



* Parsing of raw count matrices
* Programmatic extraction of sample metadata
* Metadata-driven grouping of samples
* Expression filtering
* CPM normalization
* Log₂ transformation
* Log₂ fold-change analysis between biological conditions





###### **Dataset**



Source: GEO ; accession : GSE60424

Organism: Homo sapiens

Experiment type: Bulk RNA-seq

Samples: Purified immune cell populations

Total samples: 134



###### **Files used**



"GSE60424\_counts.txt" :  Gene × sample raw count matrix 

"GSE60424\_series\_matrix.txt" :  GEO metadata used to derive biological groups



**Biological comparison performed**



Control: CD4 T cells

Treatment: CD8 T cells



The Sample groups are derived programmatically from the GEO metadata.





###### **Pipeline Steps**



1. Load the count matrix

&nbsp;  Reads the gene raw counts and converts it into a pandas DataFrame.

&nbsp;  (genes = rows, samples = columns)

&nbsp;

2\. Parse GEO metadata

&nbsp;  Extracts the sample names and cell types from the series matrix file.



3\. Create the sample groups

&nbsp;  Groups samples by their cell type using metadata (CD4, CD8, Whole Blood, Neutrophils, Monocytes, B-cells, NK)



4\. Filter out the low-expression genes

&nbsp;  Keeps genes with ≥10 counts in at least 2 samples 



5\. Normalize expression (CPM)

&nbsp;  Corrects for library size differences across samples



6\. Log₂ transformation

&nbsp;  Stabilizes variance and enables fold-change interpretation



7\. Differential expression summary

&nbsp;  Computes log₂ fold change (CD8 − CD4)



###### **Output**



results/GSE60424\_CD4\_vs\_CD8\_log2FC.csv

Contains:

* &nbsp;Mean log₂ expression in CD4
* &nbsp;Mean log₂ expression in CD8
* &nbsp;Log₂ fold change per gene



**Interpretation**



* Positive log₂FC → higher expression in CD8 T cells
* Negative log₂FC → higher expression in CD4 T cells
* Values near zero → similar expression in both cell types



Author : Aswin Antony

