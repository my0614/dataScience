import pandas as pd
import tensorflow as tf
from tensorflow.keras import preprocessing
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout, Conv1D, GlobalMaxPool1D, concatenate
import jpype
from konlpy.tag import Komoran
import pickle

class Preprocess:
    def __init__(self, word2index_dic='', userdic=None):
        print('hi')
        # 단어 인덱스 사전 불러오기
        if(word2index_dic != ''):
            f = open(word2index_dic, "rb")
            self.word_index = pickle.load(f)
            f.close()
        else:
            self.word_index = None

        # 형태소 분석기 초기화
        self.komoran = Komoran(userdic=userdic)

        # 제외할 품사
        # 참조 : https://docs.komoran.kr/firststep/postypes.html
        # 관계언 제거, 기호 제거
        # 어미 제거
        # 접미사 제거
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ',
            'JX', 'JC',
            'SF', 'SP', 'SS', 'SE', 'SO',
            'EP', 'EF', 'EC', 'ETN', 'ETM',
            'XSN', 'XSV', 'XSA'
        ]

    # 형태소 분석기 POS 태거
    def pos(self, sentence):
        jpype.attachThreadToJVM()
        return self.komoran.pos(sentence)

    # 불용어 제거 후, 필요한 품사 정보만 가져오기
    def get_keywords(self, pos, without_tag=False):
        f = lambda x: x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list

    # 키워드를 단어 인덱스 시퀀스로 변환
    def get_wordidx_sequence(self, keywords):
        if self.word_index is None:
            return []

        w2i = []
        for word in keywords:
            try:
                w2i.append(self.word_index[word])
            except KeyError:
                # 해당 단어가 사전에 없는 경우, OOV 처리
                w2i.append(self.word_index['OOV'])
        return w2i
    
train_file = "total_train_data.csv"
data= pd.read_csv(train_file, delimiter=',')
queries = data['query'].tolist()
intents = data['intent'].tolist()

p = Preprocess(word2index_dic = '../../train_tools/dict/chatbot_dict.bin',
               userdic='../../utils/user_dict.tsv')

sequences = []
for sentence in queries:
    pos= p.pos(sentence)
    keywords = p.get_keywords(pos, without_tag = True)
    seq = p.get_wordidx_sequence(keywords)
    sequences.append(seq)

from GlobalParams import MAX_SEQ_LEN
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen = MAX_SEQ_LEN, padding = 'post')

#학습용데이터셋 생성
ds = tf.data.Dataset.from_tensor_slices((padded_seqs, intents))
ds = ds.shuffle(len(queries))

train_size = int(len(padded_seqs) * 0.7)
val_size = int(len(padded_seqs) * 0.2)
test_size = int(len(padded_seqs) * 0.1)

train_ds = ds.take(train_size).batch(20)
val_ds = ds.skip(train_size).take(val_size).batch(20)
test_ds = ds.skip(train_size + val_size).take(test_size).batch(20)

dropout_prob = 0.5
EMB_SIZE = 128
EPOCH = 5
VOCAB_SIZE = len(p.word_index) + 1

input_layer = Input(shape=(MAX_SEQ_LEN,))
embedding_layer = Embedding(VOCAB_SIZE, EMB_SIZE, input_length= MAX_SEQ_LEN)(input_layer)
dropout_emb = Dropout(rate= dropout_prob)(embedding_layer)
#학습모델
conv1 = Conv1D(filters = 128, kernel_size =3, padding = 'valid',activation = tf.nn.relu)(dropout_emb)
pool1 = GlobalMaxPool1D()(conv1)

conv2 = Conv1D(filters = 128, kernel_size =4, padding = 'valid',activation = tf.nn.relu)(dropout_emb)
pool2 = GlobalMaxPool1D()(conv2)

conv3 = Conv1D(filters = 128, kernel_size =5, padding = 'valid',activation = tf.nn.relu)(dropout_emb)
pool3 = GlobalMaxPool1D()(conv3)

concat = concatenate([pool1,pool2,pool3]) #합치기
hidden = Dense(128, activation=tf.nn.relu)(concat)
dropout_hidden = Dropout(rate=dropout_prob)(hidden)
logits = Dense(5, name='logits')(dropout_hidden)
predictions = Dense(5, activation=tf.nn.softmax)(logits)

model = Model(inputs= input_layer, outputs = predictions)
model.compile(optimizer = 'adam', loss ='sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(train_ds, validation_data = val_ds, epochs = EPOCH, verbose = 1)

loss, accuracy = model.evaluate(test_ds, verbose = 1)
print('Accuracy : %f' %(accuracy * 100))
print('loss : %f' %(loss))

model.save('intent_model.h5')
print('finish')

