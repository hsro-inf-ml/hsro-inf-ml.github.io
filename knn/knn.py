#!/usr/bin/python

from math import sqrt

# list of our data points to read
xs = []

# read in featues
with open('admission.asc') as f:
	for line in f:
		x = line.split()
		xs.append((float(x[0]), float(x[1]), int(x[2])))
		# print x

# a (randomly chosen) test point
t = (6, 6)


# compute the 2d euclidean distance between two points
def dist(a, b):
	return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


# compute all distances between test point and training data,
# and store them as tuples (x, dist)
distances = []
for x in xs:
	distances.append((x, dist(t, x)))

# sort the dists ascending
distances = sorted(distances, key=lambda l: l[1])

# print out the n points closest to t
print t
n = 30
for a in distances[:n]:
	print a

# for those points, count the class occurrences
counts = {}
# unwrap the tuples, ignore x/y coords
for ((_, _, c), d) in distances[:n]:
	if c in counts:
		counts[c] += 1
	else:
		counts[c] = 1

print(counts)
print(sorted(counts.iteritems(), key=lambda l: l[1], reverse=True)[0][0])
