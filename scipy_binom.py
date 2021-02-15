import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

x = np.arange(0,21) #전체 횟수
y = scipy.stats.binom.pmf(x,20,0.5) # 이항분포
plt.figure(figsize = (8,2))
plt.bar(x,y)
plt.xlabel('앞면이 나온 횟수')
plt.ylabel('확률')
