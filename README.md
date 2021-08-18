# Бэкенд сервиса опросов

## Авторизация и регистрация пользователей

### Регистрация:

Для регистрации пользователя следует реализовать POST-запрос к эндпоинту:

http://45.82.177.42:8000/v1/users/rest-auth/registration/

В заголовок запроса следует передать:

`Content-Type: application/json`

Само тело запроса будет выглядеть следующим образом:

```json
{
    "username": "",
    "email": "@email.com",
    "password1": "",
    "password2": ""
}
```

В ответ должен вернуться токен авторизации или ошибка

### Авторизация:

Для авторизации реализуется POST-запрос к эндпоинту:

http://45.82.177.42:8000/v1/users/rest-auth/login/

В заголовке которого указывается:

```Content-Type: application/json```

В тело запроса передаётся:

```json
{
    "username": "",
    "email": "gmail.com",
    "password": ""
}
```

В ответ должен прийти или токен авторизации, или ошибка.


### Участие в опросах:

Для участия в опросах нужно передавать нижеуказанный объект по эндпоинту:

http://45.82.177.42:8000/v1/survey/answer/

Заголовок запроса должен содержать:

`Content-Type: application/json`

и

`Authorization: token ...`


Когда пользователь участвует в опросах, на "фронтенде" формируется тело запроса следующего
вида:

```json
{
    "survey": 1,
    "answers": [
        {
            "id": 1,
            "answer": 1
        },
        {
            "id": 2,
            "answer": 6
        } 
    ]
}
``` 

В котором:

`survey` -- это идентификатор самого проводимого опроса,

`список answers` - это список вопросов, на которые даётся ответ,

`словарь внутри списка`, в котором есть поле `id`, содержащее идентификатор вопроса из самого опроса, и поле `answer`, 
содержащее выбранный пользователем вариант ответа.

В случае, если пользователь ответил не на все вопросы (то есть количество отправляемых словарей в списке answers меньше, 
 чем количество вопросов в тесте), то ему вернётся уведомление об этом и результаты не засчитаются.

Если пользователь ответил на все вопросы, то ему вернётся количество правильных и неправильных ответов, а также процент 
правильных.

#### Например:

У нас есть тест по истории, состоящий из четырёх вопросов, у каждого из которых есть
четыре варианта ответа (будем использовать только один вопрос в качестве примера):

```json
[
    {
        "id": 1,
        "question_survey": [
            {
                "id": 1,
                "possible_answer_of_question": [
                    {
                        "id": 1,
                        "title": "1789",
                        "is_correct": true,
                        "question": 1
                    },
                    {
                        "id": 2,
                        "title": "1790",
                        "is_correct": false,
                        "question": 1
                    },
                    {
                        "id": 3,
                        "title": "1812",
                        "is_correct": false,
                        "question": 1
                    },
                    {
                        "id": 4,
                        "title": "1914",
                        "is_correct": false,
                        "question": 1
                    }
                ],
                "title": "Взятие Бастилии",
                "survey": 1
            }
]
}]
``` 

Чтобы ответить на этот опрос нам следует передать вот такой объект:

`"survey": 1` идентификатор опроса,

`"id": 1`,  идентификатор вопроса про взятие Бастилии,

`"answer": 1` // идентификатор варианта ответа про 1789 год,

```json
{
    "survey": 1,
    "answers": [
        {
            "id": 1, 
            "answer": 1
        },
        {
            "id": 2, 
            "answer": 6
        },
        {
            "id": 3,
            "answer": 12
        },
        {
            "id": 4,
            "answer": 13
        }
       
    ]
}
```


### Администрирование:

Доступ к панели администрирования:

http://45.82.177.42:8000/admin/


Добавление новых опросов осуществляется через раздел Survey (Possible answers и Surveys).

Отслеживание результатов можно провести через раздел Profiles, в котором представлена
таблица пользователей, где, перейдя на страницу пользователя, можно посмотреть опросы, в которых он участвовал, 
и его результаты.
