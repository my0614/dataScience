import matplotlib.pyplot as plt
import numpy as np

a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a)) # sin 형태로
plt.plot(a, np.cos(a))
plt.plot(a+np.pi/1.5, np.sin(a))
plt.show()
