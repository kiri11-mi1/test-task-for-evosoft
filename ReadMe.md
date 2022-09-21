# DRF шаблон

## Запуск бэкенд приложения

1. Склонировать репозиторий на удаленный сервер или себе на компьютер
2. Установить _docker_ и _docker-compose_
3. Создать в папке *docker* файл _.dockerenv_ и заполнить его аналогично как файл _.dockerenv.example_
4. Собрать и запустить докер-контейнеры
    ```
    docker-compose up -d
   ```
5. Выполнить миграции командой:
   ```
   docker-compose exec app python manage.py migrate
   ```
6. Раздать статику:
      ```
   docker-compose exec app python manage.py collectstatic
   ```
7. Создать суперпользователя:
   ```
   docker-compose exec app python manage.py createsuperuser
   ```
8. Перейти по адресу http://127.0.0.1/admin
