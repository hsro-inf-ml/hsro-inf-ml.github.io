
// Notes for next time:
// - kmeans live is great
// - medoid live would be great :-)

X = [[2, 6], [3, 4], [3, 8], [4, 7], [6, 2], [6, 4], [7, 3], [7, 4], [8, 5], [7, 6]]

console.log(X)

function l1(a, b) {
  return Math.abs(a[0]-b[0]) + Math.abs(a[1]-b[1])
}

function l2(a, b) {
  d1 = a[0]-b[0]
  d2 = a[1]-b[1]
  return Math.sqrt(d1*d1+d2*d2)
}

D = []

for (i = 0; i < X.length; i++) {
  dx = []
  for (j = 0; j < X.length; j++)
    dx.push(l1(X[i], X[j]))
  D.push(dx)
}

k = 2  // Anzahl Cluster


function assign(xs) {
  L = []
  for (let x of xs) {
    if (l1(x, m1) < l1(x, m2))
      L.push([x, 'm1'])
    else
      L.push([x, 'm2'])
  }
  return L
}

function est(ls, target) {
  m = [0, 0]
  c = 0
  for (let l of ls) {
    if (l[1] == target) {
      m[0] += l[0][0]
      m[1] += l[0][1]
      c++;
    }
  }
  m[0] /= c
  m[1] /= c
  return m
}

m1 = X[7]
m2 = X[8]
console.log(m1, m2)

for (i = 0; i < 5; i++) {
  L = assign(X)
  m1 = est(L, 'm1')
  m2 = est(L, 'm2')
  console.log(m1, m2)
}

