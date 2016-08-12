import matplotlib.pyplot as plt
import numpy as np
import math

def plot_colormap(matrix):
    
    #matrix = np.array([[0.000, -0.120, -0.043, -0.094, 0.037, 0.045], [0.120, 0.000, 0.108, 0.107, 0.105, 0.108], [0.043, 0.108, 0.000, 0.083, -0.043, 0.042], [0.094, 0.107, 0.083, 0.000, -0.083, 0.089], [-0.037, 0.105, -0.043, -0.083, 0.000, 2.440], [-0.045, -0.108, -0.042, 0.089, 2.440, 0.000]])
    #print(matrix)
    #cmap = [('Sequential (2)', 'afmhot')]
    minmatrix=0.
    minhelp=0.
    #find min of array
    for i in range (1,len(matrix)):
        for j in range (1,len(matrix[0])):
            minhelp=matrix[i,j]
            if minhelp<minmatrix:
                minmatrix=minhelp

    #print(minmatrix)
    matrix = np.ma.masked_where(matrix>0,matrix)

    cmap = plt.cm.YlOrBr
    cmap.set_bad(color='black')
    plt.imshow(matrix, interpolation='none', cmap=cmap)
#vmin = 1;
#vmax = minmatrix;
#fig, ax = plt.subplots()
#im = ax.pcolor(matrix, cmap=cmap, vmin=1, vmax=minmatrix, edgecolors='black')
#cbar=fig.colorbar(im)
#cbar.set_ticks(range(4)) # Integer colorbar tick locations
#ax.set(frame_on=False, aspect=1, xticks=[], yticks=[])
#ax.invert_yaxis()
#plt.show()

data = np.zeros((1024,1024))
a= 1.
b= 1.7
total=0.
x = 0.145 #start_value
step=(2)/1024
for k in range(1,1024):
    a=a+(k-1)*step
    for j in range(1,1024):
        b=b+(j-1)*step
        for n in range(1,2000):
            for i in range(1,2):
                if(i==1):
                    r=a
                    x = r*x*(1-x)
                    total= total+(math.log(abs(r-(2*r*x)))/math.log(2))
                    print(total)
                if(i==2):
                    r=b
                    x = r*x*(1-x)
                    total= total+(math.log(abs(r-(2*r*x)))/math.log(2))
        lyap=total/4000
        data[k][j]=lyap

plot_colormap(data)    
    
            