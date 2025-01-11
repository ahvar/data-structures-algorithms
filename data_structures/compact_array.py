from array import array

primes = array("i", [2, 3, 5, 7, 11, 13, 17, 19])

import sys

data = []

for k in range(13):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(k)
