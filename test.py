import pickle

list = ["hell world", "I love you", "python"]

with open('list.txt','wb') as f:
    pickle.dump(list,f)


with open("list.txt", 'rb') as f:
    data = pickle.load(f)

print(data)