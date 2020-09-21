# Random-Number-Generator
This Python file contains a code to generate Random Numbers using Linear Congruential Method. 
Linear Congruential Method is a pseudo random number generating algorithm.
This code also contains a cdf plot to visualize the random numbers generated.
Chi-square test is used to test the generator. Null Hypothesis is that the numbers follow iid Uniform (0,1) distribution. A 95% confidence interval is used.
Degrees of freedom are 99 (100 bins are used). If Null Hypothesis is accepted then the generator passes the test. Null Hypothesis is accepted if the chi-sq value of the distribution is less than the critical chi-sq value at 95% confidence interval and 99 degrees of freedom.
