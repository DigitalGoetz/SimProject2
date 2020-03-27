import numpy as np
import math
import matplotlib.pyplot as plt
import itertools




def chiSquared(theoretical, expected, size):
    sum = 0
    for tvalue, evalue in itertools.izip(theoretical, expected):
        sum = sum + (tvalue - evalue)**2
    return sum / size

def plot(dataset, nbins):
    
    count, bins, ignored = plt.hist(dataset, nbins, density=True, align='mid')

    # Log Normal Theoretical
    sum = 0 
    for v in dataset: 
        sum = sum + np.log(v) 
    mu = sum / len(dataset) 

    sum = 0 
    for v in dataset: 
        sum = sum + (np.log(v) - mu)**2 
    sigma = math.sqrt(sum / len(dataset))
   
    x = np.linspace(min(bins), max(bins), 20)
    
    pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / ( x * sigma * np.sqrt(2 * np.pi)))
    
    plt.plot(x, pdf, linewidth=2, color='r')
    plt.show() 


#t = [ 0.0 , 1.0, 2.0, 3.0]
#e = [ 0.1 , 1.2, 2.0, 3.5]
#print(chiSquared(t, e, 4))