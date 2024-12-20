import sqlite3
from datetime import datetime

# Создаем подключение к базе данных
def connect_db():
    return sqlite3.connect("todo.db")

# Создание новой задачи
def add_task(task, due_date, comments=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO tasks (task, due_date, comments)
    VALUES (?, ?, ?);
    ''', (task, due_date, comments))
    conn.commit()
    conn.close()

# Показ задач по заданной дате (год, месяц, день)
def show_tasks(date_str):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM tasks WHERE due_date LIKE ?;
    ''', (f'{date_str}%',))  # Используем LIKE для поиска по части даты (например, 2024, 2024-10, 2024-10-15)
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("Нет задач на эту дату.")
    else:
        for task in tasks:
            print(f"ID: {task[0]}")
            print(f"Задача: {task[1]}")
            print(f"Дата выполнения: {task[2]}")
            print(f"Комментарии: {task[3]}")
            print("-" * 40)

# Основное меню программы
def main():
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Показать задачи по дате")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            task = input("Введите описание задачи: ")
            due_date = input("Введите дату выполнения задачи (в формате YYYY-MM-DD): ")

            # Проверяем корректность формата даты
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Неверный формат даты. Используйте формат YYYY-MM-DD.")
                continue

            comments = input("Введите комментарии (если есть, иначе оставьте пустым): ")
            add_task(task, due_date, comments)
            print("Задача добавлена!")

        elif choice == "2":
            date_str = input("Введите дату (год, месяц или день) для поиска (например, 2024, 2024-10, 2024-10-15): ")
            show_tasks(date_str)

        elif choice == "3":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
