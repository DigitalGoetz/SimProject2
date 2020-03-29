import numpy as np
import math
import matplotlib.pyplot as plt
import itertools
from scipy.stats import gamma, expon, weibull_min


def chiSquared(theoretical, expected, size):
    sum = 0
    for tvalue, evalue in itertools.izip(theoretical, expected):
        sum = sum + (tvalue - evalue)**2
    return sum / size

def getLogNormalPdf(dataset, nbins, bins):
    sum = 0 
    for v in dataset: 
        sum = sum + np.log(v) 
    mu = sum / len(dataset) 

    sum = 0 
    for v in dataset: 
        sum = sum + (np.log(v) - mu)**2 
    sigma = math.sqrt(sum / len(dataset))
    
    x = np.linspace(min(bins), max(bins), nbins)
    print('LGN: mu=' + str(mu) + ", sigma=" + str(sigma) )
    pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / ( x * sigma * np.sqrt(2 * np.pi)))
    return (x, pdf)

def getGammaPdf(dataset, nbins, bins):
    shape, loc, scale = gamma.fit(dataset, floc=0)
    x = np.linspace(min(bins), max(bins), nbins)
    print('GAM: shape=' + str(shape) + ', loc=' + str(loc) + ", scale=" + str(scale) )
    pdf = gamma.pdf(x, shape, loc, scale)
    return (x, pdf)

def getExpoPdf(dataset, nbins, bins):
    loc, scale = expon.fit(dataset, floc=0)
    x = np.linspace(min(bins), max(bins), nbins)
    print('EXP: loc=' + str(loc) + ", scale=" + str(scale) )
    pdf = expon.pdf(x,loc, scale)
    return (x, pdf)

def getWeibullPdf(dataset, nbins, bins):
    c = 1.5
    shape, loc, scale = weibull_min.fit(dataset, floc=0)
    x = np.linspace(min(bins), max(bins), nbins)
    print('WEI: shape=' + str(shape) + ', loc=' + str(loc) + ", scale=" + str(scale) )
    pdf = weibull_min.pdf(x, shape, loc, scale)
    return (x, pdf)    

def evalFitLogNormal(dataset, count, nbins, bins):
    logNormal = getLogNormalPdf(dataset, nbins, bins)
    print('chi for LogNormal (yellow) vs Observed: ' + str(round(chiSquared(count, logNormal[1], nbins),4)))
    plt.plot(logNormal[0], logNormal[1], linewidth=1, color='xkcd:lemon', label='lognormal')

def evalFitGamma(dataset, count, nbins, bins):
    gamma = getGammaPdf(dataset, nbins, bins)
    print('chi for Gamma (purple) vs Observed: ' + str(round(chiSquared(count, gamma[1], nbins),4)))
    plt.plot(gamma[0], gamma[1], linewidth=1, color='xkcd:electric purple', label='gamma')

def evalFitExponential(dataset, count, nbins, bins):
    expo = getExpoPdf(dataset, nbins, bins)
    print('chi for Exponential (orange) vs Observed: ' + str(round(chiSquared(count, expo[1], nbins),4)))
    plt.plot(expo[0], expo[1], linewidth=1, color='xkcd:red orange', label='exponential') 

def evalFitWeibull(dataset, count, nbins, bins):
    weib = getWeibullPdf(dataset, nbins, bins)
    print('chi for Weibull (pink) vs Observed: ' + str(round(chiSquared(count, weib[1], nbins),4)))
    plt.plot(weib[0], weib[1], linewidth=1, color='xkcd:pink', label='Weibull') 

    
def plot(dataset, nbins, title):
    count, bins, ignored = plt.hist(dataset, nbins, density=True, align='mid', color='xkcd:faded green')
    evalFitGamma(dataset, count, nbins, bins)
    evalFitLogNormal(dataset, count, nbins, bins)
    evalFitExponential(dataset, count, nbins, bins)
    evalFitWeibull(dataset,count,nbins,bins)
    ax = plt.subplot(111)
    ax.set_facecolor("xkcd:light blue")
    ax.legend()
    plt.axis('tight')
    plt.title(title)
    
    plt.show()


#t = [ 0.0 , 1.0, 2.0, 3.0]
#e = [ 0.1 , 1.2, 2.0, 3.5]
#print(chiSquared(t, e, 4))