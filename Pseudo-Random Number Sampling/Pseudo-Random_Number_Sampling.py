import numpy as np
from matplotlib import pyplot as plt

# Part a (Inverse Transform Method)
U = []
def createRandom():
    return np.random.uniform()


Xa = []
av_Xa = []
vr_Xa = []

# Populate the given arrays.
### YOUR CODE HERE ###
def InverseTransformation(x):
    #Our equation was x ** 2 so its inverse equation is x ** 1/2
    return x ** (1/2)


for i in range(5000):
    x = createRandom()
    U.append(x)
    Xa.append(InverseTransformation(x))
    av_Xa.append(sum(Xa) / len(Xa))
    vr_Xa.append(np.var(Xa))

# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.figure()
hU = plt.hist(U,100,alpha=0.5,density=True)
hXa = plt.hist(Xa,100,alpha=0.5,density=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))
plt.figure()
plt.plot(av_Xa)
plt.figure()
plt.plot(vr_Xa)

# Plot the average and variance values.
### YOUR CODE HERE ###


#Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []
a = 0
b = 1
# Populate the given arrays.
### YOUR CODE HERE ###

def isReject(x):
    c = 2
    v = np.random.uniform()
    y = c * v
    fx = 2 * x
    # We use 2 * x because in rejection method the equation is 2 * x
    # x ** 2 was cumulative
    if y > fx:
        return True
    return False

i = 0
while i < 5000:
    x = (b - a) * U[i] + a
    if(isReject(x)):
        continue
    else:     
        Xb.append(U[i])
        av_Xb.append(sum(Xb) / len(Xb))
        vr_Xb.append(np.var(Xb))
        i += 1


# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,density=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.
### YOUR CODE HERE ###

plt.figure()
plt.plot(np.linspace(0,1,50000),av_Xb)
plt.figure()
plt.plot(np.linspace(0,1,50000),vr_Xb)

plt.show()
