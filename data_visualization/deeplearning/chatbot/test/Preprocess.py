from konlpy.tag import Komoran

class Preprocess:
    def __init__(self, userdic=None):
        self.komoran = Komoran(userdic=userdic)
        self.exclusion_tags = [
            'JSK','JKC','JKG','JKO','JKB','JKV','JKQ',
            'JX','JC',
            'SF','SP','SS','SE','SO',
            'EP','EF','ETN','ETM',
            'XSN','XSV','XSA'
        ]
    def pos(self, sentence):
        return self.komoran.pos(sentence)
    def get_keywords(self, pos, without_tag = False):
        f = lambda x : x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list
        