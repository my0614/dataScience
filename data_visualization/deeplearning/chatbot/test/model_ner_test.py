from Preprocess import Preprocess
from NerModel import NerModel

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin', userdic = '../utils/user_dic.tsv')

ner = NerModel(model_name1 = '../models/ner/ner_model.h5', proprocess = p)
query = '오전 13시 2분에 탕수육 주문하고 싶어요'
predicts = ner.predict(query)
print(predicts)