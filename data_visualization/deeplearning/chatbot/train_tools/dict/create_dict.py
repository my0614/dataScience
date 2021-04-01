from Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

def read_corpus_data(filename):
    f = open(filename, 'r', encoding ='UTF8')
    data= [line.split('\t') for line in f.read().splitlines()]
    data =data[1:]
    return data

corpus_data = read_corpus_data('./corpus.txt')

p = Preprocess()
dict = []
for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        dict.append(k[0])
tokenizer = preprocessing.text.Tokenizer(oov_token = 'OOV')
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

f = open('chatbot_dict.bin',"wb")
try:
    pickle.dump(word_index,f)
except Exception as e:
    print(e)
finally:
    f.close()
