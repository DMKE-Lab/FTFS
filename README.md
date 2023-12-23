# FTFS

This is a Python implementation of 

> Unsupervised Fuzzy Temporal Knowledge Graph Entity Alignment via Joint Fuzzy Semantics Learning and Global Structure Learning 

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

Entity Alignment on F_DICEWS dataset
--------------------------------
```
python run_FTFS.py --ds 0 
```

Alignment on F_YAGO-WIKI50K dataset
--------------------------------
```
python run_FTFS.py ---ds 1
```
