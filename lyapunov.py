import matplotlib.pyplot as plt
import numpy as np

'''function to plot the population development
   in: r                - system parameter (determines chaotic behavior)
   in: preiterations    - number of iterations before the plot starts
   in: start_value      - initial value of the population
   in: plot_iterations  - number of iterations for the plot
'''
def plotpopulation(r, preiterations, start_value, plot_iterations):
    # run preiterations
    x = start_value
    for _ in range(preiterations):
        x = r*x*(1-x)
    #initialize arrays for the plot
    it_array = np.arange(0, plot_iterations, 1)
    population = np.zeros(plot_iterations)
    #set initial value of the population for the plot
    population[0]= x
    #run iterations for the plot
    for i in it_array[1::]:
        population[i] = r*population[i-1]*(1-population[i-1])
    #plot population
    plt.plot(it_array, population)

# plots for different parameters r: 1 attraction point, 2 attraction points, chaos
plotpopulation(2.5, 600, 0.5, 80)
plotpopulation(3.2, 600, 0.5, 80)
plotpopulation(3.7, 600, 0.5, 80)
plt.show()


# plots for chaotical behavior with different start_values
plotpopulation(3.7, 600, 0.3999, 80)
plotpopulation(3.7, 600, 0.4, 80)
plotpopulation(3.7, 600, 0.4001, 80)
plt.show()
