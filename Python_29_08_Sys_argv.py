#  sys.argv is a list that contains command-line arguments passed to a Python script.

import sys
import math
maximum=0
minimum=100
k=len(sys.argv)
print("Size  =" , k)
print(sys.argv[0])

for i in range(1,k):

    if int(sys.argv[i]) > maximum:
        maximum=int(sys.argv[i])
    if int(sys.argv[i]) < minimum:
        minimum=int(sys.argv[i])


print("Minimum  =" , minimum)
print("Maximum =", maximum)
