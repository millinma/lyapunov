import matplotlib.pyplot as plt
import numpy as np


matrix = np.matrix('0.000 -0.120 -0.043 -0.094 0.037 0.045; 0.120 0.000 0.108 0.107 0.105 0.108; 0.043 0.108 0.000 0.083 -0.043 0.042; 0.094 0.107 0.083 0.000 -0.083 0.089; -0.037 0.105 -0.043 -0.083 0.000 2.440; -0.045 -0.108 -0.042 0.089 2.440 0.000')
print(matrix)
cmap = [('Sequential (2)', 'afmhot')]
minmatrix=0.
minhelp=0.
#find min of array
for i in range (1,len(matrix)):
    for j in range (1,len(matrix[0])):
        if matrix[i,j]>0:
            matrix[i,j]=1
        minhelp=matrix[i,j]
        if minhelp<minmatrix:
            minmatrix=minhelp
            
#vmin = 1;
#vmax = minmatrix;
fig, ax = plt.subplots()
#im = ax.pcolor(matrix, cmap=cmap, vmin=1, vmax=minmatrix, edgecolors='black')
#cbar=fig.colorbar(im)
#cbar.set_ticks(range(4)) # Integer colorbar tick locations
#ax.set(frame_on=False, aspect=1, xticks=[], yticks=[])
#ax.invert_yaxis()
plt.show()