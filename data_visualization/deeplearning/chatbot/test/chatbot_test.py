from DatabaseConfig import *
from Database import Database
from Preprocess import Preprocess

p = Preprocess(word2index_dic = '../train_tools/dict/chatbot_dict.bin', userdic= '../utils/user_dic.tsv')

db = Database(host = DB_HOST, user= DB_USER, password = DB_PASSWORD, db_name = DB_NAME)
db.connect()
query = "오늘 오전에 짬뽕 주문합니다"

from IntentModel import IntentModel
intent = IntentModel(model_name = '../models/intent/intent_model.h5', proprocess = p)
predict = intent.predict_class(query)
intent_name = intent.labels[predict]

from NerModel import NerModel
ner = NerModel(model_name1 = '../models/ner/ner_model.h5', proprocess = p)
predicts = ner.predict(query)
ner_tags = ner.predict_tags(query)

print("질문 : ", query)
print("=" * 40)
print("의도 파악", intent_name)
print("개체명 인식 : ", predicts)
print("답변 검색에 대한 필요한 NER 태그 : ", ner_tags)
print("=" * 40)

from FindAnswer import FindAnswer

try:
    f = FindAnswer(db)
    answer_text, answer_image = f.search(intent_name, ner_tags)
    answer= f.tag_to_word(predicts, answer_text)
except:
    answer = "죄송해요, 무슨 말인지 모르겠어요"
print("답변 : ", answer)
db.close()
