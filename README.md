# Лабораторная работа № 2.2 — Импорт и экспорт данных

## Цель работы

Освоение импорта и экспорта данных SQLite в форматы CSV и JSON с использованием DBeaver и Python, выполнение миграции структуры базы данных, создание резервных копий и проверка восстановления.

## Используемые технологии

- SQLite — система управления базами данных.
- DBeaver — графическая среда работы с базой данных.
- Python 3 — автоматизация операций с данными.
- Стандартные библиотеки Python: `sqlite3`, `csv`, `json`, `pathlib`, `datetime`, `shutil`, `contextlib`.

## Структура проекта

```text
Data-Models_Lab2.2/
├── database/
│   ├── LR1_part2.sqlite
│   ├── LR1_part2_structure.sql
│   └── LR2_part1_seed.sql
├── models/
│   ├── ER.png
│   └── infological_model.pdf
├── queries/
│   └── LR2_part1_queries.sql
├── exports/
│   ├── dbeaver/
│   │   ├── teacher.csv
│   │   └── teacher.json
│   └── python/
│       ├── teacher.csv
│       └── teacher.json
├── migrations/
│   └── 001_add_teacher_phone.sql
├── scripts/
│   ├── export_csv.py
│   ├── import_csv.py
│   ├── export_json.py
│   ├── import_json.py
│   ├── backup_db.py
│   └── restore_db.py
├── .gitignore
└── README.md
```

Папки `backups/` и `restored/` создаются автоматически и исключены из Git.

## Выполнение лабораторной работы

### Задание 1. Экспорт в CSV

Выполнен экспорт данных таблицы `teacher` через DBeaver и Python.

Скрипт: `scripts/export_csv.py`

Результат: CSV-файл с 4 записями преподавателей и 5 столбцами.

### Задание 2. Импорт из CSV

Выполнен импорт CSV через DBeaver в таблицу `teacher_import_csv` и через Python в таблицу `teacher_import_python`.

Скрипт: `scripts/import_csv.py`

Результат: успешно импортированы 4 записи.

### Задание 3. Экспорт в JSON

Выполнен экспорт таблицы `teacher` через DBeaver и Python.

Скрипт: `scripts/export_json.py`

Результат: JSON-массив из 4 объектов с полями таблицы.

### Задание 4. Импорт из JSON

Импорт JSON через Python выполнен в таблицу `teacher_import_json_python`.

Скрипт: `scripts/import_json.py`

Дополнительно в DBeaver импорт данных продемонстрирован через SQL Editor с использованием функций SQLite `json_each()` и `json_extract()`. В используемом мастере импорта DBeaver формат JSON не был доступен, поэтому импорт через графический мастер не выполнялся.

### Задание 5. Миграция структуры базы данных

В таблицу `teacher` добавлен столбец `phone` типа `TEXT`.

```sql
ALTER TABLE teacher
ADD COLUMN phone TEXT;
```

После миграции все 4 исходные записи сохранились. Значения нового столбца первоначально равны `NULL`.

Скрипт: `migrations/001_add_teacher_phone.sql`

Миграция рассчитана на однократное выполнение. В текущем файле SQLite столбец уже добавлен.

### Задание 6. Резервное копирование и восстановление

Реализованы Python-скрипты:

- `backup_db.py` — создание резервной копии SQLite с датой и временем в имени.
- `restore_db.py` — восстановление последней резервной копии в отдельный файл и проверка её целостности.

Результат проверки: `PRAGMA integrity_check` возвращает `ok`, в восстановленной базе присутствуют 4 преподавателя и столбец `phone`.

## Запуск Python-скриптов

Команды выполняются из корневой директории проекта.

```bash
python3 scripts/export_csv.py
python3 scripts/import_csv.py
python3 scripts/export_json.py
python3 scripts/import_json.py
python3 scripts/backup_db.py
python3 scripts/restore_db.py
```

Дополнительные сторонние Python-библиотеки для выполнения этих скриптов не требуются.

## Итог

В работе реализованы операции импорта и экспорта CSV и JSON, выполнена миграция структуры существующей базы SQLite и проверено резервное копирование с последующим восстановлением.

Импорт JSON через графический мастер DBeaver остаётся ограничением текущей реализации; вместо него применён SQL Editor.
