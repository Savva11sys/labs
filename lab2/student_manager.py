import sqlite3

# Создаем подключение к базе данных
def connect_db():
    return sqlite3.connect("students.db")

# Добавление студента в таблицу
def add_student(name, email, phone, course):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO students (name, email, phone, course)
    VALUES (?, ?, ?, ?);
    ''', (name, email, phone, course))
    conn.commit()
    conn.close()

# Показ всех студентов из таблицы
def show_all_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()

    if not students:
        print("Нет студентов в базе данных.")
    else:
        print("\nСписок студентов:")
        for student in students:
            print(f"ID: {student[0]}")
            print(f"Имя: {student[1]}")
            print(f"Электронный ящик: {student[2]}")
            print(f"Телефон: {student[3]}")
            print(f"Курс: {student[4]}")
            print("-" * 40)

# Основная программа
def main():
    while True:
        print("\nМеню:")
        print("1. Добавить студента")
        print("2. Показать всех студентов")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя студента: ")
            email = input("Введите электронный ящик студента: ")
            phone = input("Введите телефон студента: ")
            course = input("Введите курс студента: ")
            add_student(name, email, phone, course)
            print("Студент успешно добавлен!")

        elif choice == "2":
            show_all_students()

        elif choice == "3":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
