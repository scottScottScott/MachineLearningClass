from random import randrange
from math import sqrt
from copy import deepcopy


def squared_dist(pnt_a, pnt_b):
	total = 0
	for a_val, b_val in zip(pnt_a, pnt_b):
		total += pow(a_val - b_val, 2)
	return total



def dist(pnt_a, pnt_b):
	return sqrt(squared_dist(pnt_a, pnt_b))



# randomly pick k points to be the initial centers
def random_centers(points, k):
	centers = []
	for i in range(k):
		while True :
			random_int = randrange(0, len(points))
			if points[random_int] not in centers :	
				centers.append(points[random_int])
				break
	return centers



def cluster_assign(centers, points, cluster_index):
	for i in range(len(points)): # iterate through points
		min_index = 0	
		for j in range(1, len(centers)): # iterate through centers
			if(dist(points[i], centers[j]) < dist(points[i], centers[min_index])):
				min_index = j 
		# assign point i to the cluster with center that's min distance away point i
		cluster_index[i] = min_index



def update_centroid(centers, points, cluster_index):
	k = len(centers)
	for i in range(k):
		centers[i].zero()

	# sum over all points that belong to the same cluster
	for i in range(len(points)): # iterate over points
		centers[cluster_index[i]] += points[i]

	for i in range(k): # iterate over clusters
		# divide cluster sum by number of elements in cluster
		if(cluster_index.count(i)):
			centers[i] = centers[i] / cluster_index.count(i)



# calculate the Within-Cluster Sum of Squares, a.k.a Average Square Distance
def WCSS(centers, points, cluster_index):
	total = 0
	for i in range(len(points)):
		total += squared_dist(points[i], centers[cluster_index[i]])
	return total



# if track set to True then will also return list of each iteration's WCSS
def k_means_clustering(points, k, track = False, randomized = False, centers = []):
	num_points = len(points)
	if not randomized:
		centers = random_centers(points, k)
	cluster_index = [0] * num_points
	prev_cluster_index = [-1] * num_points

	if track:
		WCSS_list = []
	
	# repeat until convergence
	while cluster_index != prev_cluster_index:
		prev_cluster_index = deepcopy(cluster_index)
		cluster_assign(centers, points, cluster_index)
		if track:
			WCSS_list.append(WCSS(centers, points, cluster_index))
		update_centroid(centers, points, cluster_index)

	if track:
		return centers, cluster_index, WCSS_list
	else:
		return centers, cluster_index
