# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import datetime
import sqlite3

# 삽입날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)

# sqlite3 버전
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version', sqlite3.sqlite_version)

# DB 생성 & Autocommit
# autocommit option : isolation_level=None
conn = sqlite3.connect('./database/database.db', isolation_level=None)

c=conn.cursor()
print('Cursor type : ', type(c))

c.execute(
    "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)"
    )  # AUTOINCREMENT

# 데이터 삽입
c.execute(
    "INSERT INTO users VALUES (1 ,'Kim','Kim@naver.com', '010-0000-0000', 'Kim.com', ?)", 
    (nowDatetime,)
    )
c.execute(
    "INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)",
    (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', nowDatetime)
    )

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)
c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)


# 테이블 데이터 삭제
# print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")