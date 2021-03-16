class FindAnswer:
    def __init__(self,db):

    def _make_query(self, intent_name, ner_tags):
        sql = "select * from chatbot_train_data"
        if intent_name != None and ner_tags == None:
            sql = sql + "where intent = '{}'".format(intent_name)
        elif intent_name != None and ner_tags  == None:
            where = 'where intent = "%s' %intent_name
            if (len(ner_tags) > 0):
                where += 'and ('
                for ne in ner_tags:
                    where += "ner like '%{}%' or ".format(ne)
                where =where[:-3] + ')'
            sql = sql + where
        sql= sql + "  order by rand() limit 1"
        reutrn sql

    def search(self, intent_name, ner_tags):
        sql = self._make_query(intent_name, ner_tags)
        answer = self.db.select_one(sql)

        if answer is None:
            sql =self._make_query(intent_name, None)
            answer= self.db.select_one(sql)

        return (answer['answer'], asnwer['answer_image'])
    
    def tag_to_word(self, ner_predicts, answer):
        for word, tag in ner_predicts:
            if tag =='B_FOOD':
                answer= answer.replace(tag, word)
        answer = answer.replace('{','')
        answer = answer.replace('}','')
        return answer
        