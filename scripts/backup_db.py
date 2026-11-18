
import sqlite3
from pathlib import Path
from datetime import datetime
from contextlib import closing

# Определяем пути
project_dir = Path(__file__).resolve().parent.parent
database_path = project_dir / "database" / "LR1_part2.sqlite"
backup_dir = project_dir / "backups"

# Проверяем существование базы
if not database_path.is_file():
    raise FileNotFoundError(database_path)

# Создаём папку для резервных копий
backup_dir.mkdir(parents=True, exist_ok=True)

# Получаем дату и время
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")

# Формируем имя резервной копии
backup_path = backup_dir / f"LR1_part2_backup_{timestamp}.sqlite"

# Создаём резервную копию SQLite
with closing(sqlite3.connect(database_path)) as source:
    with closing(sqlite3.connect(backup_path)) as backup:
        source.backup(backup)

# Проверяем резервную копию
with closing(sqlite3.connect(backup_path)) as connection:
    integrity = connection.execute(
        "PRAGMA integrity_check;"
    ).fetchone()[0]

    teacher_count = connection.execute(
        "SELECT COUNT(*) FROM teacher;"
    ).fetchone()[0]

if integrity != "ok":
    raise RuntimeError("Ошибка проверки резервной копии")

print("Резервное копирование завершено успешно.")
print(f"Резервная копия: {backup_path}")
print(f"Проверка целостности: {integrity}")
print(f"Количество преподавателей: {teacher_count}")
