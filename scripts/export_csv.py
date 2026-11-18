
import csv
import sqlite3
from pathlib import Path

# Определяем пути к базе и выходному файлу
project_dir = Path(__file__).resolve().parent.parent
database_path = project_dir / "database" / "LR1_part2.sqlite"
output_path = project_dir / "exports" / "python" / "teacher.csv"

# Создаём папку для экспорта
output_path.parent.mkdir(parents=True, exist_ok=True)

# Подключаемся к базе данных
with sqlite3.connect(database_path) as connection:
    cursor = connection.cursor()

    cursor.execute("""
        SELECT teacher_id, surname, first_name, patronymic, position
        FROM teacher
        ORDER BY teacher_id;
    """)

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

# Записываем результат в CSV
with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(rows)

print(f"Экспорт завершён. Записей: {len(rows)}")
print(f"Файл сохранён: {output_path}")
