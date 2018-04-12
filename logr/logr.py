#!/usr/bin/python

import numpy as np
import random

xs = []
ys = []

with open('admission.asc') as f:
	for line in f:
		x = line.split()
		xs.append(np.matrix([1, float(x[0]), float(x[1])]).transpose())
		ys.append(int(x[2]))


def g(z):
	return 1. / (1. + np.exp(-z))


def J(theta):
	j = np.zeros([1, 1])  # 1-dim matrix
	for (x, y) in zip(xs, ys):
		z = theta.transpose() * x
		j = j + (y * z + np.log(1. - g(z)))
	return np.asscalar(j)


def grad(theta):
	gr = np.matrix([0, 0, 0]).transpose()
	for (x, y) in zip(xs, ys):
		z = np.asscalar(theta.transpose() * x)
		gr = gr + (y - g(z)) * x
	return gr


def hesse(theta):
	h = np.zeros([3, 3])
	for (x, y) in zip(xs, ys):
		z = np.asscalar(theta.transpose() * x)
		gz = g(z)
		h = h + (gz * (1. - gz)) * (x * x.transpose())
	return -h


# initial estimate
theta = np.matrix([0, 0, 0]).transpose()

# smallest change
eps = 1e-6

j = J(theta)
print("objf=%f" % j)

# should terminate at around 7 iterations
for i in range(15):
	gr = grad(theta)
	h = hesse(theta)

	theta = theta - np.linalg.inv(h) * gr

	j_ = J(theta)
	print("objf=%f" % j_)
	if abs(j - j_) < eps:
		break
	j = j_

print("theta=%s" % theta.transpose())

# try on a few sample points
for (x, y) in random.sample(zip(xs, ys), 20):
	p = g(theta.transpose() * x)
	f = p < 0.5 and y == 1 or p > 0.5 and y == 0
	print("x=%s y=%d p(1|x)=%.3f%s" % (x.transpose(), y, p, ' x' if f else '' ))

# gnuplot instructions for debug
print("set palette model RGB defined (0 'red', 1 'blue')")
# straight line based on parameters 0 = a + bx + cy...
print("f(x)=-((%f)+(%f)*x)/%f" % (theta[0], theta[1], theta[2]))
print("plot 'admission.asc' u 1:2:3 w p palette, f(x)")
