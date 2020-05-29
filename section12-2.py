# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

conn = sqlite3.connect('./database/database.db')

c = conn.cursor()

c.execute("SELECT * FROM users")

# print('one -> \n', c.fetchone())
# print()
# print('three -> \n', c.fetchmany(size=3))
# print()
# print('All -> \n',c.fetchall())

print('---------------------------------------------------')

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 >>', row)

print('---------------------------------------------------')

# 순회2
for row in c.fetchall():
    print('retrieve2 >', row)  # 조회 없음

print('---------------------------------------------------')
# 순회3
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print('retrieve3 > ', row)

print('---------------------------------------------------')
print()

# WHERE Retrieve1
param1 = (2,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())
print()

param2 = 4
c.execute("SELECT * FROM users WHERE id='%s'" % param2)
print('param2', c.fetchone())
print('param2', c.fetchall())
print()

c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 1})
print('param3', c.fetchone())
print('param3', c.fetchall())
print()

param4 = (1, 4)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4', c.fetchall())
print()

c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 4))
print('param5', c.fetchall())
print()

c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 1, "id2": 4})
print('param6', c.fetchall())
print()

with conn:
    # Dump 출력(데이터베이스 백업 시 중요)
    with open('./database/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete.')