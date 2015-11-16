from PIL import Image
from random import randrange
import KMeansClustering

class Point:
	def __init__(self, R, G, B, x, y):
		self.R = R	
		self.G = G
		self.B = B
		self.x = x
		self.y = y

	def __iter__(self):
		yield self.R
		yield self.G
		yield self.B

	def zero(self):
		self.R = 0
		self.G = 0
		self.B = 0

	def __add__(self, other):
		return Point(self.R + other.R, self.G + other.G, self.B + other.B, self.x, self.y)	

	def __truediv__(self, scalar):
		return Point(self.R / scalar, self.G / scalar, self.B / scalar, self.x, self.y)

	def __str__(self):
		return str(self.R) + " " + str(self.G) + " " + str(self.B)
	

#################################################################################
#################################################################################
#################################################################################

# 128 * 128 pixel image
image = Image.open("bird_small.tiff")
pixels = image.load()
# initialize points in 3D space with coordinates as pixel's RGB values
points = []
for x in range(128):
	for y in range(128):
		R, G, B = pixels[x, y]	
		points.append( Point(R, G, B, x, y) )

centers = []
for i in range(16):
	while True:
		RGB = Point(randrange(0, 256), randrange(0, 256), randrange(0, 256), 0, 0)
		if RGB not in centers:
			centers.append(RGB)
			break	

centers, cluster_index = KMeansClustering.k_means_clustering(points, 16, False, True, centers)

for i in range(len(points)):
	pnt = points[i]
	R = centers[cluster_index[i]].R
	G = centers[cluster_index[i]].G
	B = centers[cluster_index[i]].B
	pixels[pnt.x, pnt.y] = (int(R), int(G), int(B))
image.save("output-bird.tiff")
