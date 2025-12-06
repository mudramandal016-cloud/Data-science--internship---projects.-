#suppose  a company claims theat their new smaryphones  has an average battery life of 12 hours .
#A consumer group tests 100 phones and find average battery life of 11.8 hours with a known population standard deviation of 0.5hours 
import numpy as np 
from statsmodels.stats.weightstats import ztest
data = [11.8] * 100  
population_mean = 12
population_std_dev = 0.5

z_statistic, p_value = ztest(data, value=population_mean)

print(f"Z-Statistic: {z_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The average battery life is different from 12 hours.")
else:
    print("Fail to reject the null hypothesis: The average battery life is not significantly different from 12 hours.")

## two sample z test 
## there are two groups of students one online and offline preparing for exam 
#group A: n=50 x:75 s.d:10 group B n:60 x:80 s.d :12
# at 5% significant perform z test to ceck if there is any differnece in the result  
 

import numpy as np
import scipy.stats as stats

# Group A 
n1 = 50
x1 = 75
s1 = 10

# Group B
n2 = 60
x2 = 80
s2 = 12

# Hypothesized difference (under the null hypothesis)
D = 0

# significance level
alpha = 0.05

# Calculate the test statistic (z-score)
z_score = ((x1 - x2) - D) / np.sqrt((s1**2 / n1) + (s2**2 / n2))
print('Z-Score:', np.abs(z_score))

# Calculate the critical value
z_critical = stats.norm.ppf(1 - alpha/2)
print('Critical Z-Score:',z_critical)

# Compare the test statistic with the critical value
if np.abs(z_score) > z_critical:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")    