import matplotlib.pyplot as plt
import random

x = []
y = []
size = []
for i in range(200):
    x.append(random.randint(10,100))
    y.append(random.randint(10,100))
    size.append(random.randint(10,100))

plt.scatter(x,y, s= size, c =x, cmap='jet', alpha = 0.7)
plt.colorbar()
plt.show()