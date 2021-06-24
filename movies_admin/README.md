# Панель администратора

## Необходимые требования
Для разврачивания проекта на хостовой машине необходимо наличие:
1. [Docker](https://docs.docker.com/engine/install/)  
1. [docker-compose](https://docs.docker.com/compose/install/)
1. VCS, например [GIT](https://git-scm.com/download/win)

## Копирование и запуск проекта
1. Скопировать/склонировать репозиторий на хостовую машину,
1. В директории **movies_admin** проекта переименовать файл .env.dist в .env
1. В файле .env заполнить учетные данные:  
   - PROJECT_SECRET_KEY - секретный ключ приложения Django  
   - POSTGRES_HOST - установить значение bd по имени сервиса, в котором запускается контейнер с Postgresql  
   - POSTGRES_PORT - порт, на котором работает БД postgres, по умолчанию 5432
   - POSTGRES_DB - имя базы данных  
   - POSTGRES_USER - имя пользователя, должно совпадать с именем базы данных
   - POSTGRES_PASSWORD - пароль для пользователя
1. В директории **movies_admin** проекта выполнить две команды
    - ```$ docker-compose build```
    - ```$ docker-compose up-d```
1. После первого запуска:  
   - зайти внутрь контейнера **movie_admin** командой ```$ docker exec -it movie_admin bash```; 
   - внутри контейнера выполнить команду создания суперюзера
```# python manage.py createsuperuser```.  
   - выйти из контейнера командой ```# exit```  
   Согласно созданным учетным записям можно зайти в административную панель приложения по [ссылке](http://0.0.0.0/admin/).
     
   
    
## Остановка проекта
В директории **movies_admin** проекта выполнить команду ```$ docker-compose down```