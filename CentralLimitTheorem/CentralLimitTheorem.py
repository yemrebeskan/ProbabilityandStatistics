
import random
import numpy as np
from matplotlib import pyplot as plt

# The normal distrubiton formula stdd is standart derivation and mean is mu.
def gaussianFormula(xvalues,stdd,mean):
    y = 1 / (stdd * np.sqrt(2 * np.pi)) * np.exp(-(xvalues - mean) ** 2 / (2 * stdd ** 2)) 
    # square of standart derivation is sigma
    return y

def calculateMean(sumOfVars):
    sumOfSums = 0
    for i in sumOfVars:
        sumOfSums += i
    return sumOfSums / len(sumOfVars)

# Sum of all values that difference of mean divided by size of list.
def calculateVariance(sumOfVars):
    mean = calculateMean(sumOfVars)
    sumOfDiffFromMean = 0
    for i in sumOfVars:
        dif = (i - mean) ** 2
        sumOfDiffFromMean += dif
    return (sumOfDiffFromMean / (len(sumOfVars) - 1))

#Histogram methods
def plotAGraph(N,sumOfVars,mean,variance,XValues):
    p,ax = plt.subplots()
    ax.hist(sumOfVars,bins=100,label="sumOfVars",color='#008080', density=True)
    YValues = gaussianFormula(XValues,np.std(sumOfVars),mean) 
    plt.plot(XValues,YValues,color="r")
    plt.legend()
    plt.show()


# In standart uniform distribution we took a random variable between 0 and 1 
# Most important function,function creates the sum list.
def graphPlotter(N,sumOfVars,M,XValues):
    for n in N:
        sumOfVar = 0
        for i in range(M):
            var = random.uniform(0,1)
            sumOfVar += var
        sumOfVars.append(sumOfVar)
    mean = calculateMean(sumOfVars)
    variance = calculateVariance(sumOfVars)
    plotAGraph(N,sumOfVars,mean,variance,XValues)

#2 values are sampled independently from a standard uniform distribution and summed.
def calcExperiment1(N,sumOfVars):
    X1Values = np.arange(0,2,0.01)
    graphPlotter(N,sumOfVars,2,X1Values)

#4 values are sampled independently from a standard uniform distribution and summed.
def calcExperiment2(N,sumOfVars):
    X2Values = np.arange(0,4,0.02)
    graphPlotter(N,sumOfVars,4,X2Values)

#50 values are sampled independently from a standard uniform distribution and summed.
def calcExperiment3(N,sumOfVars):
    X3Values = np.arange(15,35,0.1)
    graphPlotter(N,sumOfVars,50,X3Values)

#50 values are sampled dependently from a uniform distribution and summed.Dependence is introduced by the following rule : If a value is smaller than 99,the next value issampled from a uniform distribution between 0 and 200, otherwise between 99 and 101.
def calcExperiment4(N,sumOfVars):
    X4Values = np.arange(4000,6000,10)
    M = 50
    for n in N:
        first = True #it controls first variable
        sumOfVar = 0
        for i in range(M):
            if first:
                var1 = random.uniform(98,102)
                first = False
            else:
                if(var1 < 99):
                    var1 = random.uniform(0,200)
                else:
                    var1 = random.uniform(98,102)
            sumOfVar += var1
        sumOfVars.append(sumOfVar)
    mean = calculateMean(sumOfVars)
    variance = calculateVariance(sumOfVars)
    plotAGraph(N,sumOfVars,mean,variance,X4Values)

# Experiment 5:50 values are sampled independently from different uniform distributions and summed.For each value generation,the uniform distribution parameters (a and b-a) should be sampled from a standard uniform distribution.
def calcExperiment5(N,sumOfVars,a,b):
    M = 50
    for n in N:
        sumOfVar = 0  
        for i in range(M):
            var = random.uniform(a,b-a) #generate random float number
            sumOfVar += var
        sumOfVars.append(sumOfVar)
    X5Values = np.arange(min(sumOfVars),max(sumOfVars),(max(sumOfVars)-min(sumOfVars))/200)
    mean = calculateMean(sumOfVars)
    variance = calculateVariance(sumOfVars)
    plotAGraph(N,sumOfVars,mean,variance,X5Values)
    


def main():
    sumOfVars = [] # sum of variables list
    N = np.arange(200000) # For each experiment, generate 200000 sums
    x = int(input("Enter your experiment:"))
    if x == 1:
        calcExperiment1(N,sumOfVars)
    elif x == 2:
        calcExperiment2(N,sumOfVars)
    elif x == 3:
        calcExperiment3(N,sumOfVars)
    elif x == 4:
        calcExperiment4(N,sumOfVars)
    elif x == 5:
        a = int(input('Enter the min:'))
        b = int(input('Enter the max:'))
        calcExperiment5(N,sumOfVars,a,b)
main()
    
    
    




