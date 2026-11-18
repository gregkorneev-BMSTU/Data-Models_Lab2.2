
import shutil
import sqlite3
from pathlib import Path

# Определяем пути
project_dir = Path(__file__).resolve().parent.parent
backup_dir = project_dir / "backups"
restore_dir = project_dir / "restored"

# Находим созданные резервные копии
backups = list(backup_dir.glob("LR1_part2_backup_*.sqlite"))

if not backups:
    raise FileNotFoundError("Резервные копии не найдены")

# Выбираем последнюю резервную копию
latest_backup = max(backups, key=lambda path: path.stat().st_mtime)

# Создаём папку восстановления
restore_dir.mkdir(parents=True, exist_ok=True)

# Формируем путь восстановленной базы
restored_path = restore_dir / "LR1_part2_restored.sqlite"

# Восстанавливаем базу из резервной копии
shutil.copy2(latest_backup, restored_path)

# Проверяем восстановленную базу
with sqlite3.connect(restored_path) as connection:
    cursor = connection.cursor()

    cursor.execute("PRAGMA integrity_check;")
    integrity = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM teacher;")
    teacher_count = cursor.fetchone()[0]

    cursor.execute("PRAGMA table_info(teacher);")
    columns = [row[1] for row in cursor.fetchall()]

if integrity != "ok":
    raise RuntimeError("Восстановленная база повреждена")

if "phone" not in columns:
    raise RuntimeError("Столбец phone не найден")

print("Восстановление базы данных завершено успешно.")
print(f"Источник: {latest_backup}")
print(f"Восстановленный файл: {restored_path}")
print(f"Проверка целостности: {integrity}")
print(f"Количество преподавателей: {teacher_count}")
print("Столбец phone присутствует.")
