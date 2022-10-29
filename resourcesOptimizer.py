import random
import matplotlib.pyplot as plt
import numpy as np

k = 3 # Number of resources

R = [r for r in range(1, k + 1)] # Set of resources

# W = [random.randint(1, 10) for r in range(1, k + 1)] # Weights for each resource

n = 50 # Number of rows in the matrix of resources

m = 50 # Number of colums in the matrix of resources

M = [[random.randint(0, k) 
      for j in range(0, m)] 
         for i in range(0, n)] # Matrix of resource positions (generated at random)

# Distance functions
def d1(i1, j1, r, M): # Distance between position (i1,j1) and the closest resource r (dMinToR)
    dMin = len(M) + len(M[0]) # If resource r is not available we assume the minimum distance is the maximum possible one
    for i2 in range(0, n):
        for j2 in range(0, m):
            if M[i2][j2] == r:
                dMin = min(abs(i1 - i2) + abs(j1-j2), dMin)
    return dMin

def d2(i1, j1, r, M): # Average distance between position (i1,j1) and resources of type r (dAvgToR)
    dAvg = len(M) + len(M[0]) # If resource r is not available we assume the average distance is the maximum possible one
    c = 0
    for i2 in range(0, n):
        for j2 in range(0, m):
            if M[i2][j2] == r:
                c += 1
                dAvg += abs(i1 - i2) + abs(j1-j2)
    return dAvg/c

# Scores functions
# Sum dMinToR (the hottest places are those where the sum of dMinTor is minimum)
S1 = [[1/(1 + sum([d1(i, j, r, M) for r in R ])) 
      for j in range(0, m)] 
         for i in range(0, n)]

# Sum dAvgToR (the hottest places are those where the sum of dAvtToR is minimum)
S2 = [[1/(1 + sum([d2(i, j, r, M) for r in R ])) 
      for j in range(0, m)] 
         for i in range(0, n)]

# Max dMinToR (the hottest places are those where the max of dMinTor is minimum, i.e., the furthest resource is as close as possible -> worst case scenario)
S3 = [[1/(1 + max([d1(i, j, r, M) for r in R ]))
      for j in range(0, m)] 
         for i in range(0, n)]

# Avg dMinToR (the hottest places are those where the avg of dMinTor is minimum -> avg case scenario)
S4 = [[1/(1 + np.average([d1(i, j, r, M) for r in R ])) 
      for j in range(0, m)] 
         for i in range(0, n)]

# Visualize resources and scores
plt.title('Heats maps of resources and scores')

plt.subplot(3,2,1)
plt.pcolormesh(M, cmap = 'rainbow')
plt.title('Resources')
 
plt.subplot(3,2,2)
plt.pcolormesh(S1, cmap = 'summer')
plt.title('Score Sum dMinToR')
 
plt.subplot(3,2,3)
plt.pcolormesh(S2, cmap = 'summer')
plt.title('Score Sum dAvgToR')

plt.subplot(3,2,4)
plt.pcolormesh(S3, cmap = 'summer')
plt.title('Score Max dMinToR')

plt.subplot(3,2,5)
plt.pcolormesh(S4, cmap = 'summer')
plt.title('Score Avg dMinToR')

plt.tight_layout()
 
plt.show()