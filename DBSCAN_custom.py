# DBSCAN: Density Based Spatial Clustering of Applications with Noise

# The code is on the base of choffstein's dbscan code (authors: Martin Ester, Hans-Peter Kriegel, Jörg Sander, Xiaowei Xu).
# The current python code is for dbscan clustering method with "customized distance measurements,"
# i.e., besides traditional Euclidean distance, this code also allows user to use custom distance matrix as input.
# This dbscan algorithm with custom distance measurements are for those cases when novel distance measurements are used


import math
import pandas as pd
from collections import Counter

class DBSCAN():

    def __init__(self, df, distance_matrix = pd.DataFrame()):
        """
        :param df: A dataframe whose columns are feature vectors
        :param distance_matrix: A custom distance matrix where each cell is the pair distance between two data points.
                                The default value is an empty matrix, which means there is no custom matrix input.
                                Then the distance measurements used will be Euclidean distances.
        """
        self.data = df
        self.distance_matrix = distance_matrix
        if self.distance_matrix.shape[0] == 0:
            self.custom = False
        else:
            self.custom = True


    def _dist(self, p, q):
        if self.custom:
            return self.distance_matrix.iloc[p, q]
        else:
            return math.dist(self.data.iloc[p, :], self.data.iloc[q, :])


    def _eps_neighborhood(self, p, q, eps):
        return self._dist(p, q) < eps


    def _region_query(self, p, eps):
        n_points = self.data.shape[0]
        seeds = []
        for q in range(0, n_points):
            if self._eps_neighborhood(p, q, eps):
                seeds.append(q)
        return seeds


    def _expand_cluster(self, classifications, p, cluster_id, eps, min_points):
        seeds = self._region_query(p, eps)
        if len(seeds) < min_points:
            classifications[p] = -1
            return False
        else:
            classifications[p] = cluster_id
            for seed_id in seeds:
                classifications[seed_id] = cluster_id

            while len(seeds) > 0:
                current_point = seeds[0]
                results = self._region_query(current_point, eps)
                if len(results) >= min_points:
                    for i in range(0, len(results)):
                        result_point = results[i]
                        if classifications[result_point] == 'Unclassified' or classifications[result_point] == -1:
                            if classifications[result_point] == 'Unclassified':
                                seeds.append(result_point)
                            classifications[result_point] = cluster_id
                seeds = seeds[1:]
            return True


    def get_cluster(self, eps, min_points):
        """Implementation of Density Based Spatial Clustering of Applications with Noise
        See https://en.wikipedia.org/wiki/DBSCAN

        Inputs:
        :param eps: Maximum distance two points can be to be regionally related
        :param min_points: The minimum number of points to make a cluster

        Outputs:
        An array with either a cluster id number or Noise (-1) for each row vector (data point) in df.
        """

        cluster_id = 1
        n_points = self.data.shape[0]
        classifications = ['Unclassified'] * n_points
        for p in range(0, n_points):
            if classifications[p] == 'Unclassified':
                if self._expand_cluster(classifications, p, cluster_id, eps, min_points):
                    cluster_id = cluster_id + 1
        self.classifications = classifications
        self.counts = Counter(classifications)
        return classifications


