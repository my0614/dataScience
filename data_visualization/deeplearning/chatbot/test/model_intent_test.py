from Preprocess import Preprocess
from IntentModel import IntentModel

p = Preprocess(word2index_dic = '../train_tools/dict/chatbot_dict.bin', userdic='../utils/user_dic.tsv')

intent = IntentModel(model_name = '../models/intent/intent_mode.h5', proprocess = p)
query = "오늘 탕수육 주문 가능한가요?"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 클래스 : ", predict)
print("의도 예측 레이블 :", predict_label)