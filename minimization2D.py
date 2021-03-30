import numpy as np
from scipy.optimize import minimize

def function(x,y):
    F = (x-1)**2+np.exp(y)
    return F

x0 = .5
y0 = .5
result = minimize(function, x0, y0)

print(result)