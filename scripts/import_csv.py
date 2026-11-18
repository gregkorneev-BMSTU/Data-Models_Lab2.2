
import csv
import sqlite3
from pathlib import Path

# Определяем пути к файлам
project_dir = Path(__file__).resolve().parent.parent
database_path = project_dir / "database" / "LR1_part2.sqlite"
csv_path = project_dir / "exports" / "python" / "teacher.csv"

# Читаем CSV-файл
with open(csv_path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Подключаемся к существующей базе данных
if not database_path.is_file():
    raise FileNotFoundError(database_path)

with sqlite3.connect(database_path) as connection:
    cursor = connection.cursor()

    # Создаём таблицу для импорта
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher_import_python (
            teacher_id INTEGER PRIMARY KEY,
            surname TEXT NOT NULL,
            first_name TEXT NOT NULL,
            patronymic TEXT,
            position TEXT NOT NULL
        );
    """)

    # Очищаем только таблицу импорта
    cursor.execute("DELETE FROM teacher_import_python;")

    # Добавляем записи из CSV
    for row in rows:
        cursor.execute("""
            INSERT INTO teacher_import_python (
                teacher_id,
                surname,
                first_name,
                patronymic,
                position
            )
            VALUES (?, ?, ?, ?, ?);
        """, (
            int(row["teacher_id"]),
            row["surname"],
            row["first_name"],
            row["patronymic"] or None,
            row["position"]
        ))

    # Проверяем количество записей
    cursor.execute("SELECT COUNT(*) FROM teacher_import_python;")
    count = cursor.fetchone()[0]

print("Импорт CSV завершён успешно.")
print(f"Количество импортированных записей: {count}")
