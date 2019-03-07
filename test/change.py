import re
import MeCab
from lib import database

temp = -1000


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
    global temp
    list = []
    for i in range(0, len(lines)-2):
        line = re.split("\s|,", lines[i])
        if line[1] == '名詞':
            nonn = database.session.query(database.Nonn).filter_by(word=line[0]).first()
            if nonn==None:
                list.append(0)
            else:
                if nonn.point == '?1?-1':
                    list.append(1)
                else:
                    list.append(int(nonn.point))
        elif i <= temp:
            pass
        else:
            while(True):
                other = database.session.query(database.Other).filter_by(word=line[0]).first()
                if other ==None:
                    other = database.session.query(database.Other).filter(database.Other.word.contains(line[0])).first()
                    if other != None:
                        i += 1
                        k = re.split("\s|,", lines[i])
                        line[0] += ' ' + k[0]
                        temp = i
                    else:
                        list.append(0)
                        break
                else:
                    list.append(int(other.point))
                    break
    return list


def first_deal(sentence):
    t = MeCab.Tagger('')
    t.parse('')
    lines = t.parse(sentence).split('\n')
    return inui_okazaki(lines)
