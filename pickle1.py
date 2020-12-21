import pickle

list = ["hell world", "I love you", "python"]

with open('list.txt','wb') as f:
    pickle.dump(list,f)

data = {}
with open("list.txt", 'rb') as f:
    data = pickle.load(f)

data  = {i : data[i] for i in range(len(data))}
print(data)

a = ['zero','one','two']
b = ['0','1','2']

value = dict(zip(b,a))
print(value)