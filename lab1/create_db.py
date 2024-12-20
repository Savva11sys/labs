import sqlite3

# Создание или открытие базы данных
def connect_db():
    return sqlite3.connect("todo.db")

# Создание таблицы tasks, если она не существует
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        due_date TEXT NOT NULL,
        comments TEXT
    );
    ''')
    conn.commit()
    conn.close()

# Вызов функции для создания таблицы
if __name__ == "__main__":
    create_table()
    print("Таблица 'tasks' успешно создана или уже существует.")
