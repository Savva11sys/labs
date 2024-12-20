import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Создание таблицы студентов
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    course TEXT NOT NULL
)
''')
conn.commit()

def add_student():
    """Функция для добавления студента в таблицу"""
    name = input("Введите имя студента: ")
    email = input("Введите электронный ящик студента: ")
    phone = input("Введите телефон студента: ")
    course = input("Введите курс студента: ")

    try:
        cursor.execute('''
        INSERT INTO students (name, email, phone, course)
        VALUES (?, ?, ?, ?)
        ''', (name, email, phone, course))
        conn.commit()
        print("Студент успешно добавлен!")
    except sqlite3.IntegrityError:
        print("Ошибка: такой email уже существует.")

def view_students():
    """Функция для вывода всех студентов"""
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\nСписок студентов:")
    for student in students:
        print(f"ID: {student[0]}, Имя: {student[1]}, Email: {student[2]}, Телефон: {student[3]}, Курс: {student[4]}")
    print()

def main():
    """Основное меню программы"""
    while True:
        print("1. Добавить студента")
        print("2. Показать всех студентов")
        print("3. Выход")
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

# Закрытие подключения
conn.close()
