import seaborn as sns
import matplotlib.pyplot as plt
print(sns.__version__)
sns.set()
sns.set_style('whitegrid')
sns.set_color_codes()
# 컬러 팔레트
current_palette = sns.color_palette()
sns.palplot(current_palette)

#relplot
tips = sns.load_dataset('tips')
sns.relplot(x = 'total_bill', y = 'tip', hue='smoker', style = 'smoker', data = tips)

#Catplot
sns.catplot(x = 'day', y='total_bill' ,hue='smoker', col= 'time', aspect = .6, kind='swarm', data = tips)

#pairplot
iris = sns.load_dataset('iris')
sns.pairplot(iris)

g = sns.PairGrid(iris)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot, n_levels = 6);

#Heatmap
flights = sns.load_dataset('flights')
flights = flights.pivot('month','year','passengers')
plt.figure(figsize=(10,10))
ax = sns.heatmap(flights, annot= True, fmt = 'd')
