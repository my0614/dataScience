import csv
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
size = [2441,2312,1031,1233]
label = ['A형','B형','AB형','O형']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%')
plt.legend()
plt.show()