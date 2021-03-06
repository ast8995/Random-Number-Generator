#!/usr/bin/env python
# coding: utf-8

# In[65]:


# This is a code to generate Random Number using Linear Congruential Generator Method or LCG method
# LCG method is a pseudo  random number generation mehod
# The formula used to produce random numbers is Xi+1 = (aXi+c)mod(m), for i = 1,2,3,....,k
# X0 is called seed, starting value
# a is called Multiplier
# m is called Modulus
# c is the increment

# This code takes increment c = 0 and this form of generation where c is 0 is called Multiplicative Linear Congruential Generator Method

# Random Numbers are generated by dividing Xi by m, and this is 

a = 16807
m = (2**31)-1
X = list(range(100001))
Random = list(range(100000))
X[0] = 10000

for i in range(100000):
    X[i+1] = (a*X[i])%m
    Random[i] = X[i]/m
Random = Random[1:100000]
rn = Random
print(Random)


# In[66]:


# Plot a cdf curve
import matplotlib.pyplot as plt
import numpy as np
x = np.sort(Random)
y = np.arange(1,len(x)+1)/len(x)
plt.plot(x,y, marker = '.', linestyle = 'none')
plt.xlabel('Random Numbers')
plt.ylabel('ECDF')
plt.margins(0.02)


#This plot indicates that the random numbers generated, have a uniform distribution


# In[67]:


# Test the generator using Chi-Squared Test
# Null Hypothesis H0 = Numbers generated are iid Uniform  (0,1)
# Alt Hypothesis  H1 = Numbers generated are not Unifrm (0,1)
# Confidence interval CI = 95%, alpha = 0.05
# If the chi-sq value of the distribution is greater than critical chi-sq value at 99 degrees of freedom and 95% CI
# Then we reject the NULL Hypothesis, numbers are not iid uniform 
import scipy.stats as stats

k = 1000 # Number of Bins
e = 100 #expected Frequency
count = list(range(1000))
D = list(range(1000))
j = 0
Random = sorted(Random)
for i in range(1000):
    inc = 0
    while(Random[j]>((i)/1000) and Random[j]<((i+1)/1000)):
            inc = inc + 1
            j = j+1
            if(j==len(Random)):
                break
    count[i] = inc
print(count)
for l in range(len(count)):
    D[l] = ((count[l]-e)**2)/e

z = sum(D)    # chi-sq value of distribution
print(z)
crit = stats.chi2.ppf(q=0.95, df=999)
print(crit)

if(z<crit):
    print("Generator has passed the chi-sqaured test")
else:
    print("Generator has failed the chi-square test")
    

# As z is less than critical value hence we accpet the Null Hypothesis that the numbers are iid uniform (0,1)
# The generator has passed the Chi-Sq test


# In[73]:


#Lagged Correlation Test
from array import *
import scipy.stats as st
lag = [1,2,3,4]
rho = list(range(4))
sigma = list(range(4))
zval = list(range(4))
for i in range(len(lag)):
    M = int((((len(rn)-1)/lag[i])-1))
    print(M)
    z1 = 0
    for j in range(M):
        y = (rn[0+(j*lag[i])]*rn[0+((j+1)*lag[i])])
        z1 = z1+y
    print(y)    
    rho[i] = (z1/(M+1)) - 0.25
    sigma[i] = ((13*M)+7)**0.5/(12*(M+1))
    zval[i] = rho[i]/sigma[i]
print(rho)
print(sigma)
print(zval)
Zcrit = st.norm.ppf(.975)
print(Zcrit)
for k in range(len(zval)):
    if(zval[k] > -Zcrit and zval[k] < Zcrit):
        print("The generator has passed the Lagged Correlation Test")
    else:
        print("The generator has failed the Lagged Correlation Test")


# In[ ]:




