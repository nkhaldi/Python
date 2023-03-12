# План миграции базы данных

## [Условие задачи] (https://github.com/nkhaldi/Python/blob/master/saber/Task.md)

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

### Схема БД после миграции
```
base_table
+----+---------+--------+-----------+
| id | name_id | status | timestamp |
+----+---------+--------+-----------+

names
+----+------+
| id | name |
+----+------+
```

#### Получение значений из таблицы
```sql
SELECT t.id, n.name, t.status, t.timestamp
FROM base_table t JOIN names n ON t.name_id = p.id
```

## План миграции
0. Сделать бэкапы.
1. 
