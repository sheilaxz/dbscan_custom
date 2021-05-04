## DBSCAN: Density Based Spatial Clustering of Applications with Noise

Given a set of points in some space, DBSCAN algorithm groups together points that are closely packed together (points with many nearby neighbors), marking as outliers points that lie alone in low-density regions (whose nearest neighbors are too far away) [1](https://en.wikipedia.org/wiki/DBSCAN). The "nearby neighbors" are filtered according to the distance between two data points.  
The DBSCAN algorithm in existing packages such as sklearn allows users to select a certain distance measurement method, e.g., the Euclidean distance. Yet, in cases when customized distance measurements are used, these packages are not applicable.   
The current python script is a DBSCAN clustering algorithm with "customized distance measurements." In other words, besides traditional Euclidean distance, this code also allows user to use custom distance matrix as input. See [Instruction](#instruction) for details and instructions of this script. This dbscan algorithm with custom distance measurements are for those cases when novel distance measurements are used in calculation.


### Table of Contents

1. [Installation](#installation)
2. [File Description](#files)
3. [Instruction](#instruction)
4. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The libraries used in this analysis process include: pandas, math, and collections.
The code should run with no issues using Python versions 3.*.


## File Descriptions <a name="files"></a>

DBSCAN_custom.py includes a class function for this algorithm. 

## Instruction<a name="instruction"></a>

TO BE UPDATED.

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credits to Martin Ester, Hans-Peter Kriegel, Jörg Sander, Xiaowei Xu, who proposed DBSCAN in 1996. 
Also give credits to [Choffstein](https://github.com/choffstein/dbscan/blob/master/dbscan/dbscan.py), as the current version of the algorithm was coded on the base of his work.

