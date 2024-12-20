import sqlite3

# Создаем или подключаемся к базе данных
def connect_db():
    return sqlite3.connect("students.db")

# Создание таблицы студентов, если она не существует
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        course TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

# Вызов функции для создания таблицы
if __name__ == "__main__":
    create_table()
    print("Таблица 'students' успешно создана или уже существует.")
