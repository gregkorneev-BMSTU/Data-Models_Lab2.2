
import json
import sqlite3
from pathlib import Path

# Определяем пути к файлам
project_dir = Path(__file__).resolve().parent.parent
database_path = project_dir / "database" / "LR1_part2.sqlite"
json_path = project_dir / "exports" / "python" / "teacher.json"

# Проверяем наличие файлов
if not database_path.is_file():
    raise FileNotFoundError(database_path)

if not json_path.is_file():
    raise FileNotFoundError(json_path)

# Читаем JSON-файл
with open(json_path, "r", encoding="utf-8") as file:
    rows = json.load(file)

# Проверяем структуру JSON
if not isinstance(rows, list):
    raise ValueError("JSON должен содержать массив объектов")

# Подключаемся к базе SQLite
with sqlite3.connect(database_path) as connection:
    cursor = connection.cursor()

    # Создаём отдельную таблицу для импорта
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher_import_json_python (
            teacher_id INTEGER PRIMARY KEY,
            surname TEXT NOT NULL,
            first_name TEXT NOT NULL,
            patronymic TEXT,
            position TEXT NOT NULL
        );
    """)

    # Очищаем только таблицу импорта
    cursor.execute("DELETE FROM teacher_import_json_python;")

    # Загружаем данные из JSON
    for row in rows:
        cursor.execute("""
            INSERT INTO teacher_import_json_python (
                teacher_id,
                surname,
                first_name,
                patronymic,
                position
            )
            VALUES (?, ?, ?, ?, ?);
        """, (
            row["teacher_id"],
            row["surname"],
            row["first_name"],
            row["patronymic"],
            row["position"]
        ))

    # Проверяем количество записей
    cursor.execute("""
        SELECT COUNT(*)
        FROM teacher_import_json_python;
    """)

    count = cursor.fetchone()[0]

print("Импорт JSON завершён успешно.")
print(f"Количество импортированных записей: {count}")
