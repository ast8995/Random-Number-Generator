#!/usr/bin/env python
# coding: utf-8

# In[34]:


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
X = list(range(10001))
Random = list(range(10000))
X[0] = 10000

for i in range(10000):
    X[i+1] = (a*X[i])%m
    Random[i] = X[i]/m

print(Random)


# In[38]:


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


# In[58]:


# Test the generator using Chi-Squared Test
# Null Hypothesis H0 = Numbers generated are iid Uniform  (0,1)
# Alt Hypothesis  H1 = Numbers generated are not Unifrm (0,1)
# Confidence interval CI = 95%, alpha = 0.05
# If the chi-sq value of the distribution is greater than critical chi-sq value at 99 degrees of freedom and 95% CI
# Then we reject the NULL Hypothesis, numbers are not iid uniform 
import scipy.stats as stats

k = 100 # Number of Bins
count = list(range(100))
D = list(range(100))

for i in range(100):
    inc = 0
    for j in range(len(Random)):
        if(Random[j]>((i)/100) and Random[j]<((i+1)/100)):
            inc = inc + a1
    count[i] = inc
    
for l in range(len(count)):
    D[l] = ((count[l]-k)**2)/k

z = sum(D)    # chi-sq value of distribution
print(z)
crit = stats.chi2.ppf(q=0.95, df=99)
print(crit)

# As z is less than critical value hence we accpet the Null Hypothesis that the numbers are iid uniform (0,1)
# The generator has passed the Chi-Sq test


# In[ ]:




