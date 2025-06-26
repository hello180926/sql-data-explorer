import sqlite3

# 创建并连接数据库
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT
    )
''')

# 插入数据
cursor.executemany('INSERT INTO users (id, name, age, email) VALUES (?, ?, ?, ?)', [
    (1, 'Alice', 23, 'alice@example.com'),
    (2, 'Bob', 30, 'bob@example.com'),
    (3, 'Charlie', 28, 'charlie@example.com'),
])

conn.commit()

# 查询年龄大于25岁
cursor.execute('SELECT * FROM users WHERE age > 25')
results = cursor.fetchall()
for row in results:
    print(row)

conn.close()
