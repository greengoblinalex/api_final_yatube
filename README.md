# Api Final Yatube

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

`GET http://127.0.0.1:8000/api/v1/follow/?search={имя_автора}`

```
POST
http://127.0.0.1:8000/api/v1/posts/
{
    "text": "example text..."
}
```
