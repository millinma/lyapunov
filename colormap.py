import matplotlib.pyplot as plt
import numpy as np
import math

#def plot_colormap(matrix):
    
    #matrix = np.array([[0.000, -0.120, -0.043, -0.094, 0.037, 0.045], [0.120, 0.000, 0.108, 0.107, 0.105, 0.108], [0.043, 0.108, 0.000, 0.083, -0.043, 0.042], [0.094, 0.107, 0.083, 0.000, -0.083, 0.089], [-0.037, 0.105, -0.043, -0.083, 0.000, 2.440], [-0.045, -0.108, -0.042, 0.089, 2.440, 0.000]])
   

minmatrix=0.
pixels = 4096     #Aufloesung des Bildes
matrix = np.zeros((pixels,pixels))   #erzeugt matrix mit der gewaehlten Aufloesung. Datenwert entspricht lyapunv exponent
min= 1.
max= 4.
x = 0.23 #start_value
step=(max-min)/pixels
for k in range(pixels): #iteriert durch die Zeilen der matrix
    a=min + k*step
    print(k)
    for j in range(pixels): #iteriert durch die spalten der matrix
        b=min + j*step
        total = 0.
        for _ in range(2000):   #hier lauft der pseudocode aus dem paper durch
            #for i in range(1,2):
                #if(i==1):
            r=a
            x = r*x*(1-x)
            total= total+(math.log(abs(r-(2*r*x)))/math.log(2))
                    #print(total)
                #if(i==2):
            r=b
            x = r*x*(1-x)
            total= total+(math.log(abs(r-(2*r*x)))/math.log(2))
        lyap=total/4000
        if(lyap<minmatrix):
            minmatrix=lyap
        matrix[k][j]=lyap   #ergebnis wird der matrix zugewiesen
        #print(lyap)
#plot_colormap(data)
matrix = np.ma.masked_where(matrix>0,matrix)
cmap = plt.cm.YlOrBr
cmap.set_bad(color='black')
plt.imshow(matrix, interpolation='none', cmap=cmap)
plt.show()
plt.savefig('image.png')            
