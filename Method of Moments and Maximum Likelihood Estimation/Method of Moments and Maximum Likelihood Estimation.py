import numpy as np
from matplotlib import pyplot as plt

# Inverse transformation
def inverseTransformationMethod(x,Theta):
    a = (5.76/(1-x))** 0.5
    #Inverse of given function
    return a 

# Pdf function
def function(theta,x):  
    return (2 * (theta ** 2) / (x ** 3)) # given function
    
# It is used for calculating values with estimates   
def calculator(theta,x):
    if x >= theta:
        return function(theta,x)
    else:
        return 0

# Calculate theta of MoM
def MoMFunction(sample):
    total = 0
    for i in sample:
        total += i
    average = total / len(sample) # mean is calculated 
    theta = average / 2 # It comes from expectation value formula in continious distribition.
    return theta


# Calculate theta of MLE
def MLEFunction(sample):
    productOfElements = 0
    for i in sample:
        productOfElements += np.log(i) # total of ln(x)
    # 2nlnO = 0 so theta is e power 0.
    LTheta = min(sample)
    return LTheta
    #After derrivation LTheta


def experimentalFunc(lenOfSample,population):
    thetasOfMoM = []
    thetasOfMLE = []
    lenOfPopulation = len(population)
    resultOfMoM = []
    resultOfMLE = []
    
    # Creating a sample:
    for i in range(100000):
        sample = []
        random_ints = np.random.randint(0,lenOfPopulation,lenOfSample)
        for k in random_ints:
            sample.append(population[k])      
        thetaMoM = MoMFunction(sample)
        thetaMLE = MLEFunction(sample)
        thetasOfMoM.append(thetaMoM)
        thetasOfMLE.append(thetaMLE)
        for k in sample:
            resultOfMoM.append(calculator(thetaMoM,k))
            resultOfMLE.append(calculator(thetaMLE,k))

    meanOfMLE = np.mean(thetasOfMLE) # Calculate mean of MLE estimates.
    varOfMLE = np.var(thetasOfMLE) # Calculate standart derivation of MLE estimates.
    meanOfMoM = np.mean(thetasOfMoM) # Calculate mean of MoM estimates
    varOfMoM = np.var(thetasOfMoM) # Calculate standart derivation of MoM estimates.
    plt.figure()
    plt.title(f'Histogram for given N = {lenOfSample}')
    plt.hist(thetasOfMoM,bins=np.linspace(0,4.8,100) ,alpha = 0.5,density = True,label=f"MoM estimate histogram for N = {lenOfSample}")
    plt.hist(thetasOfMLE,bins=np.linspace(0,4.8,100) ,alpha = 0.5,density = True,label=f"MLE estimate histogram for N = {lenOfSample}")
    plt.legend()
    
    return meanOfMLE,varOfMLE,meanOfMoM,varOfMoM

    
    

def main():
    population = []
    lenOfPopulation = 10000000
    Theta = 2.4
    x_estimates_MoM = []
    x_estimates_MLE = []
    X = [0.3,0.6,0.8,0.9]
    N = [1,2,3,4,5,10,50,100,500,1000]
    for i in X:
        x_estimates_MoM.append(round(calculator(MoMFunction(X),i),2))
        x_estimates_MLE.append(round(calculator(MLEFunction(X),i),2))
    
    print(f"Theta of the given distribution X is {MLEFunction(X)} which was obtained from MLE function.") 
    print(f"Theta of the given distribution X is {MoMFunction(X)} which was obtained from MoM function.\n")
    print(f"Result array of MoM is {x_estimates_MoM} which was obtained from MoM estimate.")
    print(f"Result array of MLE is {x_estimates_MLE} which was obtained from MLE estimate.\n")
    # Creating a population:
    for i in range(lenOfPopulation):
        random_var = np.random.rand()
        population.append(inverseTransformationMethod(random_var,Theta))
    plt.figure()
    x = np.linspace(2.4,20.0,100)
    plt.plot(x, function(Theta,x), color='red',label = "PDF")
    plt.hist(population,bins=np.linspace(2.5,20.0,100) ,alpha = 0.5,density = True,color = "orange",label="Histogram")
    plt.legend()
    plt.show()
    
    for i in N:
        meanOfMLE,varOfMLE,meanOfMoM,varOfMoM = experimentalFunc(i,population)
        print(f"For N = {i}: \n")
        print("MoM estimate mean: ",round(meanOfMoM,2), "MoM estimate std: ",round(varOfMoM ** 0.5,2) )
        print("MLE estimate mean: ",round(meanOfMLE,2), "MLE estimate std: ",round(varOfMLE ** 0.5,2),"\n")
    
    plt.show()
    

main()
