"""
Project for Module 3. Algorithmic Thinking course, Coursera
04/10/2014
Esther Alvarez Feijoo
"""

import math
from alg_cluster import Cluster


def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters in cluster_list with indices idx1 and idx2

    :param cluster_list: list of Cluster elements
    :param idx1: index of a cluster in cluster_list
    :param idx2: index of other cluster in cluster_list
    :return: tuple (dist, idx1, idx2) with idx1 < idx2. dist is distance between idx1 and idx2 elements in cluster_list
    """
    return cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2)


def slow_closest_pairs(cluster_list):
    """
    Compute the set of closest pairs of cluster in list of clusters
    using O(n^2) all pairs algorithm

    :param cluster_list: list of Cluster elements
    :return: set of all tuples (dist, idx1, idx2) where the cluster_list[idx1] and cluster_list[idx2]
        have minimum distance dist.
    """
    result_set = set()
    min_distance = float("inf")

    for idx1 in range(len(cluster_list)):
        for idx2 in range(idx1 + 1, len(cluster_list)):  # start in the next position to avoid repeated points
            actual_distance = pair_distance(cluster_list, idx1, idx2)  # calculate distance
            if actual_distance[0] < min_distance:
                min_distance = actual_distance[0]
                result_set = set([actual_distance])
            elif actual_distance[0] == min_distance:
                result_set.add(actual_distance)
    return result_set


def fast_closest_pair(cluster_list):
    """
    Compute a closest pair of clusters in cluster_list using O(n log(n)) divide and conquer algorithm

    :param cluster_list: list of Cluster elements
    :return: a tuple (distance, idx1, idx2) with idx1 < idx 2 where cluster_list[idx1] and cluster_list[idx2]
            have the smallest distance dist of any pair of clusters
    """

    def fast_helper(cluster_list, horiz_order, vert_order):
        """
        Divide and conquer method for computing distance between closest pair of points
        Running time is O(n * log(n))

        :param cluster_list:
        :param horiz_order: lists of indices for clusters ordered horizontally
        :param vert_order: lists of indices for clusters ordered vertically

        :return: a tuple (distance, idx1, idx2) with idx1 < idx 2 where cluster_list[idx1] and cluster_list[idx2]
                have the smallest distance dist of any pair of clusters
        """

        if len(horiz_order) <= 3:
            # base case
            (distance, hor_idx1, hor_idx2) = slow_closest_pairs([cluster_list[indx] for indx in horiz_order]).pop()
            return round(distance, 10), horiz_order[hor_idx1], horiz_order[hor_idx2]

        else:
            # preparing divide
            half_point = len(horiz_order) / 2

            # mid_x_value
            mid_x_value = (cluster_list[horiz_order[half_point - 1]].horiz_center() +
                          cluster_list[horiz_order[half_point]].horiz_center()) / 2

            hor_left = horiz_order[:half_point]
            hor_right = horiz_order[half_point:]
            vert_left = [idx for idx in vert_order if idx in hor_left]
            vert_right = [idx for idx in vert_order if idx in hor_right]

            # divide: recursion
            left_result = fast_helper(cluster_list, hor_left, vert_left)
            right_result = fast_helper(cluster_list, hor_right, vert_right)

            # conquer
            min_result = min(left_result, right_result)

            s_list = [idx for idx in vert_order
                      if abs(cluster_list[idx].horiz_center() - mid_x_value) < min_result[0]]

            for idx1 in range(len(s_list) - 1):
                for idx2 in range(idx1 + 1, min(idx1 + 3, len(s_list))):
                    min_result = min(min_result, pair_distance(cluster_list, s_list[idx1], s_list[idx2]))

            return min_result[0], min(min_result[1:]), max(min_result[1:])  # ordered coords

    # compute list of indices for the clusters ordered in the horizontal direction
    hcoord_and_index = [(cluster_list[idx].horiz_center(), idx)
                        for idx in range(len(cluster_list))]
    hcoord_and_index.sort()
    horiz_order = [hcoord_and_index[idx][1] for idx in range(len(hcoord_and_index))]

    # compute list of indices for the clusters ordered in vertical direction
    vcoord_and_index = [(cluster_list[idx].vert_center(), idx)
                        for idx in range(len(cluster_list))]
    vcoord_and_index.sort()
    vert_order = [vcoord_and_index[idx][1] for idx in range(len(vcoord_and_index))]
    # print horiz_order
    # compute answer recursively
    answer = fast_helper(cluster_list, horiz_order, vert_order)
    return answer


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function mutates cluster_list

    :param cluster_list: List of clusters
    :param num_clusters: number of resultant clusters
    :return: List of clusters whose length is num_clusters
    """
    while len(cluster_list) > num_clusters:
        # search the two closest clusters
        min_distance = slow_closest_pairs(cluster_list).pop()
        cluster1 = cluster_list[min_distance[1]]
        cluster2 = cluster_list[min_distance[2]]

        # reuse cluster1's position, as the new merged cluster

        new_cluster = cluster1.merge_clusters(cluster2)

        # remove the second (old) merged cluster from cluster_list
        cluster_list.remove(cluster1)
        cluster_list.remove(cluster2)

        cluster_list.append(new_cluster)
    return cluster_list


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters

    :param cluster_list: List of clusters
    :param num_clusters: number of clusters
    :param num_iterations: number of iterations
    :return: List of clusters whose length is num_clusters
    """

    # initialize k-means clusters to be initial clusters with largest populations
    centers = sorted(cluster_list, key=lambda x: x.total_population(), reverse=True)[:num_clusters]

    # main loop
    while num_iterations > 0:
        num_iterations -= 1     # update countdown of iterations

        empty_sets = [Cluster(set([]),  idx.horiz_center(), idx.vert_center(), 0, 0.0) for idx in centers]

        #organize free clusters into k sets
        for cluster in cluster_list:
            # calculate the distances between cluster and every cluster in empty_set
            distances = [empty_sets[idx].distance(cluster) for idx in range(len(empty_sets))]
            # take the empty_set's cluster that is the closest to the current cluster
            closest = empty_sets[distances.index(min(distances))]
            #merge current cluster to the closest one
            closest.merge_clusters(cluster)     # update closest, so it's updated in empties

        for idx in range(num_clusters):
            #update the center of every cluster, taking it from the empties list
            centers[idx] = Cluster(set([]), empty_sets[idx].horiz_center(), empty_sets[idx].vert_center(), 0, 0.0)

    return empty_sets