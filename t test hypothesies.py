#The weights of 25 obese people were taken before enrolling them into the nutrition camp. The population mean weight is found to be 45 kg before starting the camp.
#  After finishing the camp for the same 25 people the sample mean was found to be 75 with a standard deviation of 25. Did the fitness camp work?
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

from scipy import stats
import numpy as np

#####Independent sample T-test
from scipy import stats
import numpy as np

A = np.array([78,84,92,88,75,80,85,90,87,7978,84,92,88,75,80,85,90,87,79])
B = np.array([82,88,75,90,78,85,88,77,92,8082,88,75,90,78,85,88,77,92,80])

t_val, p_val = stats.ttest_ind(A, B)

alpha = 0.05
df = len(A)+len(B)-2

crit_t = stats.t.ppf(1 - alpha/2, df)

print("T-value:", t_val)
print("P-Value:", p_val)
print("Critical t-value:", crit_t)

print('T-test Result:')
if np.abs(t_val) >crit_t:
    print('Significant difference found.')
else:
    print('No significant difference.')

print('P-test Result:')
if p_val >alpha:
    print('Fail to reject H0. No strong evidence of difference.')
else:
    print('Reject H0. Significant difference found.')

#Paired Two-sample T-test
from scipy import stats
import numpy as np

A = np.array([4, 4, 7, 16, 20, 11, 13, 9, 11, 15])
B = np.array([15, 16, 14, 14, 22, 22, 23, 18, 18, 19])

t_val, p_val = stats.ttest_rel(A, B)

alpha = 0.05
df = len(A)-1

c_t = stats.t.ppf(1 - alpha/2, df)

print("T-value:", t_val)
print("P-Value:", p_val)
print("Critical t-value:", c_t)

print('T-test:')
if np.abs(t_val) >c_t:
    print('Significant difference found.')
else:
    print('No significant difference.')

print('P-test:')
if p_val >alpha:
    print('Reject H0')
else:
    print('Fail to reject H0')
