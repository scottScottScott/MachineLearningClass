import matplotlib.pyplot as plt
import KMeansClustering

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y	

	def zero(self):
		self.x = 0
		self.y = 0

	def __iter__(self):
		yield self.x	
		yield self.y
	
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __truediv__(self, scalar):
		return Point(self.x / scalar, self.y / scalar)

	def __str__(self):
		return "Point: " + str(self.x) + " " + str(self.y)

##################################################################
##################################################################
##################################################################

#parse the input into a list of Point objects
points = []
data = open("toy_data.txt", 'r')
for line in data:
	curr_args = list(map(lambda x : float(x), line.split()))
	curr_point = Point(*curr_args)
	points.append(curr_point)

runs_info = []
best_WCSS = -1
for run in range(20):
	centers, cluster_index, WCSS_list = KMeansClustering.k_means_clustering(points, 4, True)
	runs_info.append(WCSS_list)
	curr_WCSS = WCSS_list[-1]
	if best_WCSS == -1 or curr_WCSS < best_WCSS:
		best_cluster_index = cluster_index
		best_WCSS = curr_WCSS

# make first graph - points in clusters graph
x_clusters = [ [] for i in range(4) ] 
y_clusters = [ [] for i in range(4) ] 
for i in range(len(best_cluster_index)):
	x_clusters[best_cluster_index[i]].append(points[i].x)
	y_clusters[best_cluster_index[i]].append(points[i].y)

colors = ["bo", "go", "ro", "yo"]
for i in range(4):
	plt.plot(x_clusters[i], y_clusters[i], colors[i])
plt.show()

# make second graph - distortion function over iterations of 20 runs
max_iterations = 0
for i in range(20):
	plt.plot(runs_info[i])
	if(max_iterations < len(runs_info[i])):
		max_iterations = len(runs_info[i])

plt.ylabel("WCSS")	
plt.xlabel("Number of Iterations")	
plt.xlim((0, max_iterations))
plt.xticks(list(range(max_iterations)))
plt.show()
