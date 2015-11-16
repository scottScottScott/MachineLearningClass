N_Values = [50, 100, 1000, 5000]

for N in N_Values:
	print("\\newpage")
	print("{ \\Large N = " + str(N) + "} \\\\")
	for i in range(10):
		print("\includegraphics{" + str(N) + "EigenVector" + str(i) + "X4}    ", end="")
		print("Eigenvector \#" + str(i + 1) + " for N = " + str(N) + "\\\\")
	print("\\\\ \\\\")
