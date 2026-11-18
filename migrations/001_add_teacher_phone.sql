
-- ЛР 2.2. Задание 5.
-- Миграция структуры таблицы teacher.
-- Добавление столбца для номера телефона.

ALTER TABLE teacher
ADD COLUMN phone TEXT;

-- Проверка структуры таблицы
PRAGMA table_info(teacher);

-- Проверка сохранности данных
SELECT *
FROM teacher
ORDER BY teacher_id;

-- Проверка количества записей
SELECT COUNT(*)
FROM teacher;
