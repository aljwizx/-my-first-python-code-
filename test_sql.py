import sqlite3

from practice5 import user_steps

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        city TEXT
    )
''')
cursor.execute('''
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        item TEXT,
        price INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')
cursor.executemany(''' 
    INSERT INTO users (id, name, city) VALUES (?, ?, ?)''', [
    (1,'Алла', 'Тараз'),
    (2,'Антон', 'Каратау'),
    (3,'Марсель', 'Алматы')
])
cursor.executemany('''
    INSERT INTO orders (id, user_id, item, price) VALUES (?, ?, ?, ?)''', [
    (101, 1, 'Наушники', 15000),
    (102, 1, 'Чехол', 2000),
    (103, 2, 'Клавиатура', 25000)
])
conn.commit()
query = '''
SELECT users.name, COUNT(orders.id) AS orders_count
FROM users 
JOIN orders ON users.id = orders.user_id
GROUP BY users.name
'''
cursor.execute(query)
results = cursor.fetchall()
print("--- РЕЗУЛЬТАТ ЗАПРОСА---")
for row in results:
    user_name = row[0]
    count = row[1]
    print(f"Пользователь: {user_name} | Количество заказов: {count}")
conn.close()
