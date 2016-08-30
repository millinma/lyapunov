from pyx import *
import matplotlib.pyplot as plt
import numpy as np
import math


def MatrixWithPixelValues(x, minmatrix):
    matrix = np.zeros((pixelsa,pixelsb))   #erzeugt matrix mit der gewaehlten Aufloesung. Datenwert entspricht lyapunv exponent

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
    return matrix

def PlottingWithPyx(matrix, min_x, max_x, min_y, max_y, step, width, height):
    d=[]

    ValueNormMatrix = matrix/np.max(matrix)
    Steps_x = len(matrix[:,0])
    Steps_y = len(matrix[0,:])
    for i in range(Steps_x):
        for j in range(Steps_x):
            Wert = matrix[Steps_x -1 - i,j]
            if Wert < 0:
                d.append([(j + 0.5) * step + min_x,
                              (i + 0.5)* step + min_y , 0])
            else:
                d.append([(j + 0.5) * step + min_x,
                              (i + 0.5)* step + min_y , ValueNormMatrix[Steps_x -1-i,j ] ])

    quadrat = graph.style.density(gradient=color.gradient.BlackYellow)

    g = graph.graphxy(
            width  = width,
            height = height,
            x      = graph.axis.linear(min = min_x, max = max_x,
                     title = 'a'),
            y      = graph.axis.linear(min =min_y, max = max_y,
                     title = 'b'))

    g.plot(graph.data.points(d, x=1, y=2, color=3), styles = [quadrat])
    g.writePDFfile()

def PlotWithMatplotlib(matrix):
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

if __name__ == "__main__":
    minmatrix=0.
    pixels = 1000 #Aufloesung des Bildes
    preiterations = 600
    lyap_iterations = 4000
    sequence = "aaaabbbb"
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

    x = 0.04 #start_value
    stepa = diffa/pixelsa
    stepb = diffb/pixelsb


    matrix = MatrixWithPixelValues(x, minmatrix)
    PlottingWithPyx(matrix, mina, maxa, minb, maxb, stepa, diffa, diffb)
    #PlotWithMatplotlib(matrix)

