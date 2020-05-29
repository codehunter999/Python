import sqlite3

conn = sqlite3.connect('./database/database.db')

c = conn.cursor()

c.execute("UPDATE users SET username =? WHERE id = ?", ('niceman',1))

c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'niceman', 'id': 3})

c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 5))

for user in c.execute('SELECT * FROM users'):
    print(user)

print('---------------------------------------------------------------------------------------')

# Row Delete1
c.execute("DELETE FROM users WHERE id = ?", (7,))

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id", {'id': 8})

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 9)

# 중간 데이터 확인2
for user in c.execute('SELECT * FROM users'):
    print(user)

# 테이블 전체 데이터 삭제
# print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

conn.commit()

conn.close()