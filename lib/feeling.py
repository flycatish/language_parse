# -*- coding: utf-8 -*-
import re
import MeCab
from lib import database



def simple_voting(result):
    the_day_point = 0
    for i in range(0, len(result)):
        the_day_point += result[i]
    the_day_point = (0 if(the_day_point==0) else the_day_point/len(result))
    if the_day_point > 0:
        return 'positive'
    elif the_day_point < 0:
        return 'negative'
    else:
        return 'neutrality'


def inui_okazaki(lines):
    list = []
    for i in range(0, len(lines)-2):
        line = re.split("\s|,", lines[i])
        print(line[0])
        if line[1] == '名詞':
            nonn = database.session.query(database.Nonn).filter_by(word=line[0]).first()
            if nonn==None:
                list.append(0)
            else:
                if nonn.point == '?1?-1':
                    list.append(1)
                else:
                    list.append(int(nonn.point))
        else:
            other = database.session.query(database.Other).filter_by(word=line[0]).first()
            if other == None:
                list.append(0)
            else:
                list.append(int(other.point))
    return simple_voting(list)


def first_deal(sentence):
    t = MeCab.Tagger('')
    t.parse('')
    lines = t.parse(sentence).split('\n')
    return inui_okazaki(lines)
