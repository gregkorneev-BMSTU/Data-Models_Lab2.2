
import json
import sqlite3
from pathlib import Path

# Определяем пути
project_dir = Path(__file__).resolve().parent.parent
database_path = project_dir / "database" / "LR1_part2.sqlite"
output_path = project_dir / "exports" / "python" / "teacher.json"

# Проверяем наличие базы
if not database_path.is_file():
    raise FileNotFoundError(database_path)

# Создаём папку экспорта
output_path.parent.mkdir(parents=True, exist_ok=True)

# Подключаемся к базе данных
connection = sqlite3.connect(database_path)
connection.row_factory = sqlite3.Row

try:
    cursor = connection.cursor()

    cursor.execute("""
        SELECT teacher_id, surname, first_name, patronymic, position
        FROM teacher
        ORDER BY teacher_id;
    """)

    # Преобразуем строки таблицы в словари
    rows = [dict(row) for row in cursor.fetchall()]
finally:
    connection.close()

# Записываем данные в JSON
with open(output_path, "w", encoding="utf-8") as file:
    json.dump(rows, file, ensure_ascii=False, indent=4)

print("Экспорт JSON завершён успешно.")
print(f"Количество экспортированных записей: {len(rows)}")
print(f"Файл сохранён: {output_path}")
