# План миграции базы данных

## [Условие задачи](https://github.com/nkhaldi/Python/blob/master/saber/Task.md#2-%D0%BC%D0%B8%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%B0%D0%B7%D1%8B-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

### БД до миграции
#### Cхема
```
base_table
+----+------+--------+-----------+
| id | name | status | timestamp |
+----+------+--------+-----------+
```
#### Получение значений из таблицы
```sql
SELECT id, name, status, timestamp
FROM base_table
```

### БД после миграции
#### Cхема
```
names             base_table
+----+------+     +----+---------+--------+-----------+
| id | name |     | id | name_id | status | timestamp |
+----+------+     +----+---------+--------+-----------+
   |                        |
   +------one-to-many-------+
```

#### Получение значений из таблицы
```sql
SELECT b.id, n.name, b.status, b.timestamp
FROM base_table b JOIN names n ON b.name_id = n.id;
```

## План миграции
0. Сделать бэкапы!<br>
1. Преобразовать взаимодействующие с БД модули сервисов А таким образом,<br>
чтобы функции, работающие с БД могли бы работать и со старой схемой, и с новой.<br>
Опираясь на текущую схему БД преобразовать, выбирать методы работы с БД.<br>
2. Перезапустить сервисы А.<br>
3. Аналогично преобразовать взаимодействующие с БД модули сервисов Б.<br>
4. Перезапустить сервисы Б.<br>
5. Создать новую таблицу для хранения имён<br>
```sql
CREATE TABLE names
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
);
```
6. Заполнить таблицу имён<br>
```sql
INSERT INTO names (name)
SELECT DISTINCT(name)
FROM base_table;
```
7. Создать новую таблицу по новой схеме, которая заменит оригинальную.<br>
```sql
CREATE TABLE new_table
  id INT PRIMARY KEY,
  name_id INT FOREIGN KEY REFERENCES names(id) NOT NULL,
  status VARCHAR(255),
  timestamp datetime DEFAULT CURRENT_TIMESTAMP
);
```
8. Заполнить временную таблицу значениями из старой.<br>
```sql
INSERT INTO new_table (name_id, status, timestamp)
SELECT n.id, b.status, b.timestamp
FROM base_table b JOIN names n ON b.name_id = n.id;
```
9. Удалить старую таблицу.<br>
```sql
DROP TABLE IF EXISTS base_table;
```
10. Переименовать новую таблицу под оригинальную.<br>
```sql
ALTER TABLE new_table RENAME base_table;
```
11. Тестировать.
