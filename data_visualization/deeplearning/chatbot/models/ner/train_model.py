import tensorflow as tf
from tensorflow.keras import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
from Preprocess import Preprocess

def read_file(file_name):
    sents = []
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for idx, l in enumerate(lines):
            if l[0] == ';' and lines[idx + 1][0] == '$':
                this_sent = []
            elif l[0] =='$' and lines[idx -1][0] == ';':
                continue
            elif l[0] =='\n':
                sents.append(this_sent)
            else:
                this_sent.append(tuple(l.split()))
    return sents

p = Preprocess(word2index_dic='../../train_tools/dict/chatbot_dict.bin',userdic='../../utils/user_dic.tsv')

corpus = read_file('ner_train.txt')
sentences, tags= [],[]
for t in corpus:
    tagged_sentence = []
    sentence, bio_tag = [],[]
    for w in t:
        tagged_sentence.append((w[1],w[3]))
        sentence.append(w[1])
        bio_tag.append(w[3])
    sentences.append(sentence)
    tags.append(bio_tag)
print('샘플 크기 : \n',len(sentences))
print("0번째 샘플 단어 시퀸스 : \n", sentences[0])
print("0번째 bio 태그 : \n", tags[0])
print("샘플 단어 시퀸스 최대 길이 : ", max(len(l) for l in sentences)) # 최대 단어 길이
print("샘플 시퀸스 평균 길이 : ",(sum(map(len, sentences))/len(sentences)))

#토크나이저 정의
tag_tokenizer = preprocessing.text.Tokenizer(lower=False)
tag_tokenizer.fit_on_texts(tags)

vocab_size = len(p.word_index) +1
tag_size = len(tag_tokenizer.word_index) + 1
print("BIO 태그 사전 크기 : ",tag_size)
print("단어 사전 크기 :", vocab_size)

#학습용 예제
x_train = [p.get_wordidx_sequence(sent) for sent in sentences]
y_train = tag_tokenizer.texts_to_sequences(tags)

index_to_ner = tag_tokenizer.index_word
index_to_ner[0] = 'PAD'

max_len = 40
x_train = preprocessing.sequence.pad_sequences(x_train, padding='post', maxlen = max_len)
y_train = preprocessing.sequence.pad_sequences(y_train, padding= 'post', maxlen =max_len)

x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size= .2, random_state = 1234)
#출력데이터
y_train = tf.keras.utils.to_categorical(y_train, num_classes=tag_size)
y_test = tf.keras.utils.to_categorical(y_test,num_classes=tag_size)

print("학습 시퀸스 형상 : ", x_train.shape)
print("학습 샘플 레이블 형상 : ", x_test.shape)
print("텍스트 샘플 시퀸스 형상 : ", y_train.shape)
print("텍스트 샘플 레이블 형상 : ", y_test.shape)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Embedding, Dense, TimeDistributed, Dropout, Bidirectional
from tensorflow.keras.optimizers import Adam

model = Sequential()
model.add(Embedding(input_dim= vocab_size, output_dim=30, input_length=max_len, mask_zero=True))
model.add(Bidirectional(LSTM(200, return_sequences=True, dropout=0.50, recurrent_dropout= 0.25)))
model.add(TimeDistributed(Dense(tag_size, activation='softmax')))
model.compile(loss='categorical_crossentropy', optimizer=Adam(0.01), metrics=['accuracy'])
model.fit(x_train, y_train, batch_size = 128, epochs = 10)

print("평과 결과 :", model.evaluate(x_test, y_test)[1])
model.save('ner_model.h5')

def sequences_to_tag(sequences):
    result = []
    for sequence in sequences:
        temp= []
        for pred in sequence:
            pred_index = np.argmax(pred)
            temp.append(index_to_ner[pred_index].replace("PAD","0"))
        result.append(temp)
    return result
from seqeval.metrics import f1_score, classification_report
#데이터셋 ner 예측
y_predicted = model.predict(x_test)
pred_tags = sequences_to_tag(y_predicted)
test_tags = sequences_to_tag(y_test)

print(classification_report(test_tags, pred_tags))
print("F1_score : {:.1%}".format(f1_score(test_tags, pred_tags)))

