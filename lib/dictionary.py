import re
from lib import database
from lib.database import session, Nonn,Other

result1 = database.session.query(database.Nonn).all()
if len(result1) == 0:
    with open("dic/pn.csv.m3.120408.trim", 'r') as f:
        for line in f.readlines():
            line = re.split(',', line)
            line[0] = line[0].strip('"')
            nonn = Nonn(word=line[0], point=line[1])
            session.add(nonn)

result2 = database.session.query(database.Other).all()
if len(result2) == 0:
    with open("dic/wago.121808.pn", 'r') as f2:
        for line in f2.readlines():
            line = re.split(',', line)
            line[2] = line[2].strip('\n')
            other = Other(word=line[2], point=line[0])
            session.add(other)
    session.commit()

