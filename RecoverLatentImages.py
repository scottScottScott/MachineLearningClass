import numpy as np
from PIL import Image

def blowUp(picture_array, name, factor):
	selected_array = np.copy(picture_array)
	im = Image.new("L", (factor * 28, factor * 28))
	pixels = im.load()

	for y in range(28):
		for x in range(28):

			for i in range(factor):
				for j in range(factor):
					pixels[x * factor + i, y * factor + j] = int(selected_array[y * 28 + x])

	im.save(name + "X" + str(factor) + ".jpg")

def save_image(picture_array, name):
	selected_array = np.copy(picture_array)

	im = Image.new("L", (28, 28))
	pixels = im.load()

	min_val = np.amin(selected_array)
	max_val = np.amax(selected_array)
	max_val = max_val - min_val

	selected_array -= min_val
	selected_array /= max_val
	selected_array *= 255
	selected_array = selected_array.astype(int)

	for y in range(28):
		for x in range(28):
			pixels[x, y] = int(selected_array[y * 28 + x])

	#im.save(name + ".jpg")
	blowUp(selected_array, name, 4)	
	#blowUp(selected_array, name, 100)	

################################################################
################################################################

f = open("lfa.txt", "r")

data_list = []
for line in f:
	a = line.split()	
	a = list(map(float, a))
	data_list.append(a)	

data_array = np.array(data_list)
# print(data_array.dtype)
# print(data_array.shape)

save_image(data_array[6], "Image7")

meanData_array = np.average(data_array, axis = 0)
save_image(meanData_array, "ImageMean")

N_values = [50, 100, 1000, 5000]
for N in N_values:
	temp_array = np.copy(data_array[0:N])

	meanData_array = np.average(temp_array, axis = 0)
	normalized_data_array = temp_array - meanData_array
	covariance_array = np.empty([784, 784], dtype=float)

	for i in range(len(normalized_data_array)):
		covariance_array += np.outer(normalized_data_array[i], normalized_data_array[i])
	covariance_array /= len(normalized_data_array)

	w, v = np.linalg.eig(covariance_array)
	# print(w, v)

	eigenvectors = np.empty([784, ])
	for i in range(10):
		eigenvector = v[:, i]	
		save_image(eigenvector, str(N) + "EigenVector" + str(i))
