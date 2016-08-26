import matplotlib.pyplot as plt
import numpy as np
import math


minmatrix=0.
pixels = 300000 #Aufloesung des Bildes
preiterations = 600
lyap_iterations = 4000
sequence = "ab"
mina = 3.808
maxa = 3.8670
minb = 3.808
maxb = 3.8670
pixelsa = int(math.sqrt(pixels*(maxa-mina)/(maxb-minb)))
pixelsb = int(pixelsa * (maxb-minb)/(maxa-mina))
print "pixels a", pixelsa
print "pixels b", pixelsb
matrix = np.zeros((pixelsa,pixelsb))   #erzeugt matrix mit der gewaehlten Aufloesung. Datenwert entspricht lyapunv exponent

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
plt.ylabel('a')
plt.xlabel('b')
plt.imshow(matrix, interpolation='none', cmap=cmap, extent = [minb, maxb, mina, maxa])
filename = "./pictures/p" + str(pixelsa) +  "_" + sequence + "_" + str(mina) + "-" + str(maxa) + ".png"
plt.savefig(filename)
plt.show()
