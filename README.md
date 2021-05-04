## DBSCAN: Density Based Spatial Clustering of Applications with Noise

Given a set of points in some space, DBSCAN algorithm groups together points that are closely packed together (points with many nearby neighbors), marking as outliers points that lie alone in low-density regions (whose nearest neighbors are too far away) [[1](https://en.wikipedia.org/wiki/DBSCAN)]. The "nearby neighbors" are filtered according to the distance between two data points.  

The current python script is a DBSCAN clustering algorithm with "customized distance measurements." In other words, besides traditional Euclidean distance, this code also allows user to use custom distance matrix as input. This dbscan algorithm with custom distance measurements are for those cases when novel distance measurements are used in calculation. Notice that _sklearn.cluster.DBSCAN_ can also do this if set _metric="precomputed"_.

See [Instruction](#instruction) for details and instructions of this script.

### Table of Contents

1. [Installation](#installation)
2. [File Description](#files)
3. [Instruction](#instruction)
4. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The libraries used in this analysis process include: pandas, math, and collections.
The code should run with no issues using Python versions 3.


## File Descriptions <a name="files"></a>

DBSCAN_custom.py includes a class function for this algorithm. 

## Instruction<a name="instruction"></a>

Class DBSCAN(df, distance_matrix = pd.DataFrame()):
	"""
	Parameters :

	df : A dataframe whose columns are feature vectors

	distance_matrix : A custom distance matrix (must be square) where each cell is the pair distance between two data points.  
                      The default value is an empty matrix, which means there is no custom matrix input. Then the distance measurements used will be Euclidean distances.  
	
	Attributes :

	distance_matrix : Returns the distance matrix input  

	custom : True if a custom distance matrix is given. 
			 Otherwise False, which means the measurement is Euclidean distance.
	"""


	def dbscan(self, eps, min_points)
	"""
	Parameters :

    	eps : Maximum distance two points can be to be regionally related

        min_points: The minimum number of points to make a cluster

    Return :
        An array with either a cluster id number or Noise (-1) for each row vector (data point) in df.

    Attributes :

    	classifications: An array with either a cluster id number or Noise (-1) for each row vector (data point) in df.

    	counts : collections.Counter on the classification array, showing the distinct classes and number of items in each class.
    """

	
	Example :

	----------

	# Use Euclidean distance
	>>> df = pd.DataFrame({'x': [1, 1, 2, 7, 8, 8, 17], 'y': [2, 1, 2, 8, 7, 9, 25]})
	>>> clustering=DBSCAN(df)
	>>> clustering.distance_matrix
	Empty DataFrame
	Columns: []
	Index: []
	>>> clustering.custom
	False
	>>> clustering.dbscan(2, 2)
	[1, 1, 1, 2, 2, 2, -1]
	>>> clustering.classifications
	[1, 1, 1, 2, 2, 2, -1]
	>>> clustering.counts
	Counter({1: 3, 2: 3, -1: 1})

	# Use custom distance matrix
	>>> dis_mat = pd.DataFrame(0, index = range(7), columns = range(7))
	>>> for i in range(7):
    		for j in range(7):
        		dis_mat.iloc[i, j] = math.dist(df.iloc[i, :], df.iloc[j, :])
    >>> clustering = DBSCAN(df, dis_mat)
    >>> clustering.distance_matrix
           0          1          2          3          4          5          6
	0   0.000000   1.000000   1.000000   8.485281   8.602325   9.899495  28.017851
	1   1.000000   0.000000   1.414214   9.219544   9.219544  10.630146  28.844410
	2   1.000000   1.414214   0.000000   7.810250   7.810250   9.219544  27.459060
	3   8.485281   9.219544   7.810250   0.000000   1.414214   1.414214  19.723083
	4   8.602325   9.219544   7.810250   1.414214   0.000000   2.000000  20.124612
	5   9.899495  10.630146   9.219544   1.414214   2.000000   0.000000  18.357560
	6  28.017851  28.844410  27.459060  19.723083  20.124612  18.357560   0.000000
	>>> clustering.custom
	True
	>>> clustering.dbscan(3, 2)
	[1, 1, 1, 2, 2, 2, -1] 
	>>> clustering.counts
	Counter({1: 3, 2: 3, -1: 1})

	----------


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credits to Martin Ester, Hans-Peter Kriegel, Jörg Sander, Xiaowei Xu, who proposed DBSCAN in 1996.  

Also give credits to [Choffstein](https://github.com/choffstein/dbscan/blob/master/dbscan/dbscan.py), as the current version of the algorithm was coded on the base of his work.

