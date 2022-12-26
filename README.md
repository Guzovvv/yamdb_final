![Github CI/CD](https://github.com/guzovvv/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Проект YaMDb

Проект нацелен на сбор **отзывов** на всевозможные **произведения**, без возможности хранения или воспроизведения произведений. 
Основные категори произведений: "Книги", "Фильмы", "Музыка".
Список **категорий** не закрытый и может быть расширен администратором.

На каждое произведение пользователь может оставить отзыв и оценку.
На основе оценок пользователей формируется рейтинг произведения.


## Используемые технологии

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)


## Запуск проекта YaMDb на сервере: 

- Сделайте fork репозитория с проектом на странице https://github.com/Guzovvv/yamdb_final.

В вашем аккаунте на GitHub появится новый репозиторий.
- Клонируйте репозиторий на локальную машину. Для этого в терминале выполните такие команды:
``` 
git clone git@github.com:<ваш_username>/yamdb_final.git
``` 

### Добавьте в Secrets GitHub переменные окружения: 
```
DB_ENGINE=django.db.backends.postgresql
DB_HOST=db
DB_NAME=postgres
DB_PASSWORD=postgres
DB_PORT=5432
DB_USER=postgres
SECRET_KEY='YOUR_SECRET_KEY'
```
Для работы с  Docker Hub:
```
DOCKER_USERNAME=<ваш_username_dockerhub>
DOCKER_PASSWORD=<ваш_пароль_dockerhub>
```
Для деплоя:
```
USER=<username_для_подключения_к_серверу>
HOST=<IP-адрес_вашего_сервера>
PASSPHRASE=<PASSPHRASE_если_при_создании_ssh-ключа_использовали_фразу-пароль>
SSH_KEY=<приватный_ключ_с_компьютера_имеющего_доступ_к_серверу>
```
- Для получения приватного ключа выполните команду в терминале:
```
cat ~/.ssh/id_rsa
```
Скопируйте приватный ключ включая строки BEGIN и END и сохраните в переменную SSH_KEY.

Для отправки отчета:
```
TELEGRAM_TO=<ID_своего_телеграм-аккаунта>
TELEGRAM_TOKEN=<Токен_вашего_бота>
```
Узнать свой ID можно у бота @userinfobot.
Узнать токен вашего бота можно у бота @BotFather.

### Подготовьте сервер:

- Войдите на сервер, выполнив в терминале команду
```
ssh <username>@<IP-адрес_вашего_сервера>
```
- Остановите службу nginx:
```
 sudo systemctl stop nginx
 ```
- Установите docker:
```
sudo apt install docker.io
```
- Установите docker-compose согласно инструкции:
```
https://docs.docker.com/compose/install/
```
- Скопируйте файл docker-compose.yaml из вашего проекта на сервер в home/username/docker-compose.yaml
```
scp docker-compose.yaml <username>@<server_address>:/home/<username>/
```
- Скопируйте директорию с файлом default.conf из вашего проекта на сервер в /home/username/nginx/default.conf 
```
scp -r nginx <username>@<server_address>:/home/<username>/
```

### Запуште проект на Github. После успешного деплоя зайдите на сервер и выполните команды:

```
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py createsuperuser
sudo docker-compose exec web python manage.py collectstatic --no-input
```
или в зависимости от версии:
```
sudo docker compose exec web python manage.py migrate
sudo docker compose exec web python manage.py createsuperuser
sudo docker compose exec web python manage.py collectstatic --no-input
```

## После запуска контейнеров проект доступен по следующим адресам:
- API http://<IP-адрес_вашего_сервера>/api/v1/
- ReDoc http://<IP-адрес_вашего_сервера>/redoc/
- Админ зона Django http://<IP-адрес_вашего_сервера>/admin/


**Автор**
----------

* [Гузов Владимир] (https://github.com/guzovvv)
Яндекс.Практикум, когорта № 40