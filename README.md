<h1 align="center">Всем привет! Меня зовут<a href="https://github.com/greengoblinalex" target="_blank"> greengoblinalex</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Я+автор+данного+приложения)](https://git.io/typing-svg)
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Computer+science+student)](https://git.io/typing-svg)

# Api Yatube

## Описание

Проект API Yatube - это сервис блогов, который позволяет пользователям писать свои посты на любые темы, создавать группы по интересам и комментировать посты других пользователей. Также, сервис предоставляет возможность подписки на других авторов и чтения только их постов.

Данный проект решает задачу предоставления возможности пользователям писать свои посты на интересующие их темы, а также комментировать их и следить за другими авторами, чьи посты им интересны.

Благодаря использованию API-подхода, проект api yatube может быть использован в различных сценариях, включая создание мобильных приложений, SPA (Single Page Applications), а также других веб-сервисов.

Использование RESTful API также делает api yatube доступным для работы с различными клиентскими приложениями, такими как приложения для iOS и Android, что делает проект более универсальным среди различных групп разработчиков и пользователей.

## Установка

1. Склонируйте репозиторий
2. Создайте виртуальное окружение
3. Установите все зависимости, использую команду `pip install -r requirements.txt`
4. Перейдите в директорию yatube_api и запустите приложение командой `python manage.py runserver`

## Примеры запросов

```
GET
http://127.0.0.1:8000/api/v1/follow/?search={имя_автора}
```

```
POST
http://127.0.0.1:8000/api/v1/posts/
{
    "text": "example text..."
}
```

## Документация

1. Перейдя по данной ссылке, после запуска проекта, можно посмотреть документацию `http://127.0.0.1:8000/redoc/`
2. Также можно найти `redoc.yaml` по данному пути `/api_final_yatube/yatube_api/static/redoc.yaml` 
