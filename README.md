# Shainy
Shainy - это проект для поиска людей для какого либо занятия. Например, вы хотите поиграть теннис, но друзей у вас нет. За вас проблему поиска людей решит данное приложение. 
* Есть общий список с постами, в которых люди предлагают чем либо заняться
* Человек посылает response на пост с интересным ему занятием
* Автор поста принимает этот response, и, если хочет, посылает match юзеру, в ответ на что автору приходит почта того, кто послал response

## Установка
`git clone https://github.com/hed0xakep/shainy.git`

`python manage.py runserver`

### Важно! В Headers необходимо отправлять ключ Authorization со значением Token {token}, где token - ваш токен авторизации.
### Как получить токен рассказано ниже 

## Доступные эндпоинты:
* `api/auth/users/` 
Регистрация.
POST-запрос. Параметры: email, username, password 
* `auth/token/login/`
Получение токена.
POST-запрос. Параметры: username, password. В ответ приходит токен
* `api/posts/all/` 
Просмотр всех постов
GET-запрос 
* `api/posts/add/`
Добавление нового поста.
POST-запрос. Параметры: activity, description
* `api/responses/my/`
Отклики на мои посты.
GET-запрос
* `api/responses/match/<int:resp_id>/`
Ответ на отклик.
GET-запрос.
В resp_id - id модели ResponseModel
* `api/responses/<post_id>/`
Отклик на пост.
POST-запрос

