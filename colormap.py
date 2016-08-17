import matplotlib.pyplot as plt
import numpy as np
import math

#def plot_colormap(matrix):
    
    #matrix = np.array([[0.000, -0.120, -0.043, -0.094, 0.037, 0.045], [0.120, 0.000, 0.108, 0.107, 0.105, 0.108], [0.043, 0.108, 0.000, 0.083, -0.043, 0.042], [0.094, 0.107, 0.083, 0.000, -0.083, 0.089], [-0.037, 0.105, -0.043, -0.083, 0.000, 2.440], [-0.045, -0.108, -0.042, 0.089, 2.440, 0.000]])
   

minmatrix=0.
pixels = 1000 #Aufloesung des Bildes
lyap_iterations = 2000
matrix = np.zeros((pixels,pixels))   #erzeugt matrix mit der gewaehlten Aufloesung. Datenwert entspricht lyapunv exponent
sequence = "ab"
min = 3
max = 4.
x = 0.23 #start_value
step=(max-min)/pixels
for k in range(pixels): #iteriert durch die Zeilen der matrix
    a=min + k*step
    print(k)
    for j in range(pixels): #iteriert durch die spalten der matrix
        b=min + j*step
        total = 0.
        for _ in range(lyap_iterations):   #hier lauft der pseudocode aus dem paper durch
            for r_str in sequence:
		if(r_str == "a"):
		    r=a
		elif(r_str == "b"):
		    r=b
                x = r*x*(1-x)
                total= total+(math.log(abs(r-(2*r*x)))/math.log(2))
        lyap=total / (lyap_iterations * len(sequence))
        if(lyap<minmatrix):
            minmatrix=lyap
        matrix[k][j]=lyap   #ergebnis wird der matrix zugewiesen
#plot_colormap(data)
matrix = np.ma.masked_where(matrix>0,matrix)
cmap = plt.cm.YlOrBr
cmap.set_bad(color='black')
plt.imshow(matrix, interpolation='none', cmap=cmap)
filename = "./pictures/p" + str(pixels) +  "_" + sequence + "_" + str(min) + "-" + str(max) + ".png"
plt.savefig(filename)
plt.show()
