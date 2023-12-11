# FTFS

This is a Python implementation of 

> Unsupervised Fuzzy Temporal Knowledge Graph Entity Alignment via Joint Fuzzy Semantics Learning and global Structure Learning


Dependencies
--------------------------------
- python 3.9
- cuda 11.3
- pytorch 1.11
- dgl 0.8
- pyg 2.0.4
- scikit-learn 1.0.2
- networkx 2.8.4
- argparse 1.4.0


Alignment on the ICEWS05-15 dataset and YAGO-WIKI50K dataset for knowledge graph entity alignment
--------------------------------------------------------------------
The dataset and LaBSE embedding files can be downloaded from [Google Drive](https://drive.google.com/file/d/1cP6CxVWsqa9ngOM4St1PzFv5NBF_jxBG/view?usp=sharing)
```
python run_FTFS.py
```