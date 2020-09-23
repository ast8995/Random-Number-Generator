# Random-Number-Generator
This Python notebook file contains a code to generate 100,000 Random Numbers using Linear Congruential Method. 
Linear Congruential Method is a pseudo random number generating algorithm.
This code also contains a cdf plot to visualize the random numbers generated.
Chi-square test is used to test the generator. Null Hypothesis is that the numbers follow iid Uniform (0,1) distribution. A 95% confidence interval is used.
Degrees of freedom are 999 (1000 bins are used). If Null Hypothesis is accepted then the generator passes the test. Null Hypothesis is accepted if the chi-sq value of the distribution is less than the critical chi-sq value at 95% confidence interval and 99 degrees of freedom.
Lagged Correlation Test is also used to test the independence of the numbers. If the Z-value of the distribution of numbers lies between -Z(alpha/2) and Z(alpha/2) where
alpha is the significance level. For this test, alpha = 0.05
