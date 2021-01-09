import matplotlib.pyplot as plt
import numpy as np

t = []
p2 = []
p3 = []

for i in range(0,50,2):
    t.append(i/10)
    p2.append((i/10) **2)
    p3.append((i/10)**3)
t = np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,p2,'bs',t,p3,'g^')
plt.show()