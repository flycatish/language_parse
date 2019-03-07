import MeCab
import re
from lib import database

for i in range(0, -5):
    print(i)
    # pass

t = MeCab.Tagger('')
t.parse('')
sentence = t.parse("お祭り気分").split('\n')
line = re.split("\s|,", sentence[0])
other = database.session.query(database.Other).filter_by(word=line[0]).first()

print(line[0])
# other = database.session.query(database.Other).filter(database.Other.word.contains('怜悧')).first()
# print(other.word)
