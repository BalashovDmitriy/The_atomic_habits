# Бэкенд-часть SPA веб-приложения "Атомарные привычки"

### Установка:

### Docker-compose:
- Установить docker и docker-compose командой ```apt install docker.io docker-compose```
- Сбилдить и запустить ```docker-compose build``` ```docker-compose up```

### Другой вариант:

- Убедитесь, что у вас установлен python 3.11 или более новая версия
- Убедитесь, что у вас установлен PostgreSQL и запущен локальный сервер базы данных
- Убедитесь, что у вас установлен Redis и запущен redis-сервер
- Склонировать репозиторий
- Создать и активировать виртуальное окружение```python -m venv ваша_папка_для_виртуального_окружения```
- Установить зависимости командой ```pip install -r requirements.txt```
- Создать вашу базу данных для работы с проектом ```CREATE DATABASE ваша_база_данных;```
- Создать миграции через ```python3 manage.py makemigrations``` и применить их ```python3 manage.py migrate```
- Открыть командную строку и запустить ```python3 manage.py runserver```
- Для запуска Celery открыть другой экземпляр командной строки и запустить ```celery -A config worker -l INFO```
- Для запуска django-celery-beat открыть другой экземляр командной строки и
  запустить ```celery -A config beat -l INFO```
- Создать бота в телеграм
- В файле .env.sample заполнить данные для работы с проектом и переименовать его в .env

### Используемые технологии:

- DjangoRestFramework
- Swagger/ReDoc ```host://swagger/``` ```host://redoc/```, работает авторизация по Bearer токену
- Redis
- Celery
- CORS
- Сервис рассылок сообщений через Telegram
- Пагинация для вывода списка привычек

### Логика работы системы:

- Зарегистрировать пользователя ```/users/register/```, указать telegram_id
- Получить токен пользователя ```/users/token/```
- Создать привычку, при этом если это полезная ```is_pleasant=False``` привычка, то необходимо указать также
  вознаграждение ```reward```, либо связанную приятную ```is_pleasant=True``` привычку ```foreign_habit```, а также
  время выполнения привычки и время на выполнение этой привычки
- При этом стоит валидация, по следующим условиям:
  - Одновременный выбор связанной привычки и указание вознаграждения для полезной привычки недопустимо
  - Время на выполнение привычки должно быть не больше 120 секунд
  - В связанные привычки могут попадать только привычки с признаком приятной привычки
  - У приятной привычки не может быть вознаграждения или связанной привычки
  - Нельзя выполнять привычку реже, чем 1 раз в 7 дней
- Если в привычке указать ```is_public=True```, то она будет доступна в списке всех публичных привычек для других
  пользователей
- После создания привычек отрабатывает функция, которая проверяет время, и если до привычки осталось 15 минут -
  отправляет уведомление в Telegram для пользователя
- Необходимо создавать привычку со временем хотя бы за 1 час до её старта, иначе для выполнения она будет доступна на
  следующий день.

### Права доступа:

- Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
- Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

### Эндпоинты:
- Регистрация пользователя
- Просмотр деталей профиля
- Редактирование профиля
- Получение токена
- Обновление токена
- Список публичных привычек
- Список своих привычек с пагинацией
- Создание привычки
- Редактирование привычки(через PUT)
- Удаление привычки
