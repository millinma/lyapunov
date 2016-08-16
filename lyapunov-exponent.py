import matplotlib.pyplot as plt
import numpy as np

def lyapunov_exponent(r,  preiterations, start_value, iterations):
    # run preiterations
    lyap = 0
    x = start_value
    for _ in range(preiterations):
        #print x
        x = r*x*(1-x)
    for _ in range(iterations):
        x = r*x*(1-x)
        help_v = np.log(np.absolute(r-2*r*x))
        #print "1. help", help_v
        help_v = help_v//np.log(2)
        #print "2. help", help_v
        lyap = lyap + help_v
    return lyap/iterations

print lyapunov_exponent(2, 600, 0.1, 8000)
    
