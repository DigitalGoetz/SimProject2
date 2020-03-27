import numpy as np
import math
import matplotlib.pyplot as plt


mu, sigma = 1.5, 0.5

s = np.random.lognormal(mu, sigma, 1000)
n = len(s)

count, bins, ignored = plt.hist(s, 40, density=True, align='mid')
x = np.linspace(min(bins), max(bins), 10000)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / ( x * sigma * np.sqrt(2 * np.pi)))
plt.plot(x, pdf, linewidth=2, color='r')

## estimate parameters from data 
#sum = 0 
#for v in s: 
#
#    sum = sum + np.log(v) 
#mu = sum / n 
#
#sum = 0 
#for v in s: 
#    sum = sum + (np.log(v) - mu)**2 
#sigma = math.sqrt(sum / n) 
#
#x = np.linspace(min(bins), max(bins), 10000) 
#pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi))) 
#plt.plot(x, pdf, linewidth=2, color='y') 
#plt.axis('tight') 

plt.show() 