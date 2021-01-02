import matplotlib.pyplot as plt
import csv
plt.title('plotting') # 그래프 title만들기
plt.plot([10,20,30,40],'r.',label = "age") #x축,y축
plt.plot([140,160,170,170],'g^' ,label = "height", color='purple')
plt.legend() # 범례 보여주기
plt.show()
