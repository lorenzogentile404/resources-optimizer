import random
import matplotlib.pyplot as plt
import numpy as np

k = 3 # Number of resources

R = [r for r in range(1, k + 1)] # Set of resources

# W = [random.randint(1, 10) for r in range(1, k + 1)] # Weights for each resources - Can be added later...

n = 10 # Number of rows in the matrix of resources

m = 10 # Number of colums in the matrix of resources

M = [[random.randint(0, k) 
      for j in range(0, m)] 
         for i in range(0, n)] # Matrix of resource-positions (generated at random)

# Distance functions
def distance1(i1, j1, r, M): # Distance function with inputs: index i1, j1 and resource r and matrix M
    dmin = len(M) + len(M[0])
    for i2 in range(0, n):
        for j2 in range(0, m):
            if M[i2][j2] == r:
                dmin = min(abs(i1 - i2) + abs(j1-j2), dmin)
    return dmin

def distance2(i1, j1, r, M): # Distance function with inputs: index i1, j1 and resource r and matrix M
    davg = 0
    count = 0
    for i2 in range(0, n):
        for j2 in range(0, m):
            if M[i2][j2] == r:
                count += 1
                davg += abs(i1 - i2) + abs(j1-j2)
    return davg/count

# Scores functions
S1 = [[1/(1 + sum([distance1(i, j, r, M) for r in R ]))
      for j in range(0, m)] 
         for i in range(0, n)] # Score matrix with distance1

S2 = [[1/(1 + sum([distance2(i, j, r, M) for r in R ])) 
      for j in range(0, m)] 
         for i in range(0, n)]

S3 = [[1/(1 + max([distance1(i, j, r, M) for r in R ])) 
      for j in range(0, m)] 
         for i in range(0, n)]

S4 = [[1/(1 + np.average([distance1(i, j, r, M) for r in R ])) 
      for j in range(0, m)] 
         for i in range(0, n)]

# Visualize resources and scores

plt.title('Heats maps of resources and scores')

plt.subplot(3,2,1)
plt.pcolormesh(M, cmap = 'rainbow')
plt.title('Resources')
 
plt.subplot(3,2,2)
plt.pcolormesh(S1, cmap = 'summer')
plt.title('Score w. distance1')
 
plt.subplot(3,2,3)
plt.pcolormesh(S2, cmap = 'summer')
plt.title('Score w. distance2')

plt.subplot(3,2,4)
plt.pcolormesh(S3, cmap = 'summer')
plt.title('Score with distance1, but w. max')

plt.subplot(3,2,5)
plt.pcolormesh(S4, cmap = 'summer')
plt.title('Score with distance1, but w. avg')

plt.tight_layout()
 
plt.show()