from pyx import *
import matplotlib.pyplot as plt
import numpy as np
import math


minmatrix=0.
pixels = 10000 #Aufloesung des Bildes
preiterations = 600
lyap_iterations = 4000
sequence = "ab"
mina = 1.
maxa = 4.
minb = 1.
maxb = 4.

diffa = maxa-mina
diffb = maxb-minb

pixelsa = int(math.sqrt(pixels*diffa/diffb))
pixelsb = int(pixelsa * (diffa/diffb))
print("pixels a", pixelsa)
print("pixels b", pixelsb)
matrix = np.zeros((pixelsa,pixelsb))   #erzeugt matrix mit der gewaehlten Aufloesung. Datenwert entspricht lyapunv exponent

x = 0.25 #start_value
stepa = diffa/pixelsa
stepb = diffb/pixelsb
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
        lyap=total / (lyap_iterations)
        if(lyap<minmatrix):
            minmatrix=lyap
        matrix[pixelsa - 1 - k][j]=lyap   #ergebnis wird der matrix zugewiesen

d=[]


NeueNormMatrix = matrix/np.max(matrix)

for i in range(pixelsa):
    for j in range(pixelsb):
        Wert = matrix[pixelsa -1 - i,j]
        if Wert < 0:
            d.append([(j + 0.5) * stepa + mina,
                          (i + 0.5)* stepb + minb , 0 ])
        else:
            d.append([(j + 0.5) * stepa + mina,
                          (i + 0.5)* stepb + minb , Wert ])


print(d)
quadrat = graph.style.density(gradient=color.gradient.BlackYellow)

g = graph.graphxy(
        width  = diffa,
        height = diffb,
        x      = graph.axis.linear(min = mina, max = maxa,
                 title = 'a'),
        y      = graph.axis.linear(min =minb, max = maxb,
                 title = 'b'))

g.plot(graph.data.points(d, x=1, y=2, color=3), styles = [quadrat])
g.writePDFfile()

print(matrix)

#plot_colormap(data)
matrix = np.ma.masked_where(matrix<0,matrix)
cmap = plt.cm.YlOrBr
cmap.set_bad(color='black')
plt.ylabel('a')
plt.xlabel('b')
plt.imshow(matrix, interpolation='none', cmap=cmap, extent = [minb, maxb, mina, maxa])
filename = "./pictures/p" + str(pixelsa) +  "_" + sequence + "_" + str(mina) + "-" + str(maxa) + ".png"
plt.savefig(filename)
plt.show()
