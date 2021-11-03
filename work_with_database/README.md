## Знакомство с работой Django & PostgreSQL

## **Есть вероятность что структура match/case не будет работать на версиях python ниже 3.10**

Для начала работы в консоли выполнить следующие команды:

- Установить зависимости ```pip install -r requirements.txt```
- Создание БД и миграций ```python manage.py migrate```
- Команда для загрузки данных из csv в БД ```python manage.py import_phones```
- Команда для запуска приложения ```python manage.py runserver```