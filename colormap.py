import matplotlib.pyplot as plt
import numpy as np
import math

#def plot_colormap(matrix):
    
    #matrix = np.array([[0.000, -0.120, -0.043, -0.094, 0.037, 0.045], [0.120, 0.000, 0.108, 0.107, 0.105, 0.108], [0.043, 0.108, 0.000, 0.083, -0.043, 0.042], [0.094, 0.107, 0.083, 0.000, -0.083, 0.089], [-0.037, 0.105, -0.043, -0.083, 0.000, 2.440], [-0.045, -0.108, -0.042, 0.089, 2.440, 0.000]])


minmatrix=0.
pixelsa = 75 #Aufloesung des Bildes
pixelsb = 100
preiterations = 600
lyap_iterations = 2000
matrix = np.zeros((pixelsa,pixelsb))   #erzeugt matrix mit der gewaehlten Aufloesung. Datenwert entspricht lyapunv exponent
sequence = "bbaba"
mina = 3.6
maxa = 3.9
minb = 3.2
maxb = 3.6
x = 0.23 #start_value
stepa = (maxa-mina)/pixelsa
stepb = (maxb-minb)/pixelsb
for k in range(pixelsa): #iteriert durch die Zeilen der matrix
    a = mina + k*stepa
    print(k)
    for j in range(pixelsb): #iteriert durch die spalten der matrix
        b = minb + j*stepb
        total = 0.
        for n in range((lyap_iterations + preiterations)/len(sequence)):   #hier lauft der pseudocode aus dem paper durch
            for r_str in sequence:
                if(r_str == "a"):
                    r=a
                elif(r_str == "b"):
                    r=b
                x = r*x*(1-x)
                if(n > preiterations/len(sequence)):
                    total= total+(math.log(abs(r-(2*r*x)))/math.log(2))
        lyap=total / (lyap_iterations * len(sequence))
        if(lyap<minmatrix):
            minmatrix=lyap
        matrix[pixelsa - 1 - k][j]=lyap   #ergebnis wird der matrix zugewiesen
#plot_colormap(data)
matrix = np.ma.masked_where(matrix>0,matrix)
cmap = plt.cm.YlOrBr
cmap.set_bad(color='black')
plt.imshow(matrix, interpolation='none', cmap=cmap, extent = [mina, maxa, minb, maxb])
filename = "./pictures/p" + str(pixelsa) +  "_" + sequence + "_" + str(mina) + "-" + str(maxa) + ".png"
plt.savefig(filename)
plt.show()
