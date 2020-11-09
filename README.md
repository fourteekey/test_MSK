#Django-Template 
``
Пустой шаблон для проекта джанго с конфигурационными файлами.
Инструкция на Notion.
``

## Бэкенд
 Все действия производятся в директории `backend`
 
### Настройки
```
$ pip install -r requirements
$ cp config/example.env config/.env
$ python manage.py makemigrations
$ python manage.py migrate
```

### Запуск бэкенда

```
$ python manage.py runserver
```

# ТЗ
```
Требования:
    API-методы должны быть реализованы с помощью DRF
    нужно спроектировать простые модели с нужными полями (например, инвестор, паспорт, документ и т. д.)
    необходимо сделать тесты для реализованных методов
Необходимые методы:
    1. олучение текущего статуса квалификации
    GET api/v1/investor investor_id
    2. зарузка паспорта (файла)
    PUT api/v1/passport investor_id
    3. загрузка паспортных данных (1 шаг)
    POST api/v1/investor/passport
    4. подтверждение присоединения к правилам (2 шаг)
    PUT api/v1/investor/qualification
    5. загрузка документа о квалификации
    PUT api/v1/investor/qualification
    6. подтверждение или отказ от квалификации (3 шаг) 
    PUT api/v1/investor/qualification
```
