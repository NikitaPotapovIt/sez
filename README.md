Документация API через POSTMAN

1. Введение  

Документация описывает методы тестирования API для регистрации пользователей, управления заметками и удаления пользователей. Все запросы требуют аутентификации через JWT, кроме регистрации. 
2. Тестирование регистрации пользователя  
POST /api/register/  

Описание : Создает нового пользователя и возвращает JWT-токены.   
Запрос : 

    Method : POST  
    URL : http://localhost:8000/api/register/  
    Body (raw JSON) :
    json
     
    {
      "username": "testuser",
      "email": "test@example.com",
      "password": "test123"
    }
     
Ответ : 

    201 Created  (успешно):
    json
     
    {
      "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com"
      },
      "refresh": "eyJ0eXAi...",
      "access": "eyJ0eXAi..."
    }
     

3. Тестирование аутентификации  
POST /api/token/  

Описание : Получение JWT-токенов для авторизации.   
Запрос : 

    Method : POST  
    URL : http://localhost:8000/api/token/  
    Body (raw JSON) :
    json
     
    {
      "username": "testuser",
      "password": "test123"
    }

Ответ : 

    200 OK  (успешно):
    json
    {
      "access": "JWT-access-токен",
      "refresh": "JWT-refresh-токен"
    }
     
     
     

4. Тестирование заметок  
POST /api/notes/  

Описание : Создание новой заметки.   
Запрос : 

    Method : POST  
    URL : http://localhost:8000/api/notes/  
    Headers :
        Authorization: Bearer <access_token>  
        Content-Type: application/json
         
    Body (raw JSON) :
    json

    {
      "title": "Заметка 1",
      "content": "Содержимое заметки"
    }

Ответ : 

    201 Created  (успешно):
    json
     
    {
      "id": 1,
      "title": "Заметка 1",
      "content": "Содержимое заметки",
      "created_at": "2023-10-05T12:00:00Z",
      "updated_at": "2023-10-05T12:00:00Z"
    }

GET /api/notes/  

Описание : Получение списка всех заметок текущего пользователя.   
Запрос : 

    Method : GET  
    URL : http://localhost:8000/api/notes/  
    Headers :
        Authorization: Bearer <access_token>
         
     

Ответ : 

    200 OK  (успешно):
    json
     
    [
      {
        "id": 1,
        "title": "Заметка 1",
        "content": "Содержимое заметки",
        "created_at": "...",
        "updated_at": "..."
      }
    ]

PUT/PATCH /api/notes/{id}/  

Описание : Обновление заметки.   
PUT (полное обновление) : 

    Method : PUT  
    URL : http://localhost:8000/api/notes/1/ (замените 1 на ID заметки)  
    Headers :
        Authorization: Bearer <access_token>  
        Content-Type: application/json
         
    Body (raw JSON) :
    json
     
    {
      "title": "Обновленный заголовок",
      "content": "Новое содержимое"
    }
     
PATCH (частичное обновление) : 

    Method : PATCH  
    Body (raw JSON) :
    json
     
    {
      "title": "Новый заголовок"
    }

Ответ : 

    200 OK  (успешно):
    json

    {
      "id": 1,
      "title": "Обновленный заголовок",
      "content": "Новое содержимое",
      "created_at": "...",
      "updated_at": "..."
    }
     
DELETE /api/notes/{id}/  

Описание : Удаление заметки.   
Запрос : 

    Method : DELETE  
    URL : http://localhost:8000/api/notes/1/  
    Headers :
        Authorization: Bearer <access_token>

Ответ : 

    204 No Content  (успешно удалено).

5. Тестирование удаления пользователя  
DELETE /api/users/{id}/  

Описание : Удаление пользователя (требуется права администратора).   
Запрос : 

    Method : DELETE  
    URL : http://localhost:8000/api/users/1/ (замените 1 на ID пользователя)  
    Headers :
        Authorization: Bearer <admin_access_token>

Ответ :

    204 No Content  (успешно удалено).

Примечание :   

    Для удаления пользователя требуется роль администратора.  
    Если у пользователя нет прав, вернется 403 Forbidden .
     

Документация API через curl 

Документация для API, разработанного на Django с использованием JWT для аутентификации и управления заметками. Все запросы требуют аутентификации, кроме регистрации и авторизации. 
1. Регистрация пользователя  

Описание : Создает нового пользователя и возвращает JWT-токены.
Метод : POST
URL : http://localhost:8000/api/register/ 
bash
`curl -X POST http://localhost:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "test123"
}'`
 

Ответ (успешно) : 
json
`{
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com"
    },
    "refresh": "eyJ0eXAi...",
    "access": "eyJ0eXAi..."
}`
  
2. Авторизация (получение JWT-токенов)  

Описание : Получает access- и refresh-токены.
Метод : POST
URL : http://localhost:8000/api/token/ 
bash
`curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{
    "username": "testuser",
    "password": "test123"
}'`

Ответ (успешно) : 
json
`{
    "access": "JWT-access-токен",
    "refresh": "JWT-refresh-токен"
}
 `
3. Получение списка заметок  

Описание : Возвращает все заметки текущего пользователя.
Метод : GET
URL : http://localhost:8000/api/notes/ 
bash
`curl -X GET http://localhost:8000/api/notes/ \
-H "Authorization: Bearer <access_token>"`

Ответ (успешно) : 
json
`[
    {
        "id": 1,
        "title": "Заметка 1",
        "content": "Содержимое заметки",
        "created_at": "2023-10-05T12:00:00Z",
        "updated_at": "2023-10-05T12:00:00Z"
    }
]`
 
4. Создание заметки  

Описание : Создает новую заметку.
Метод : POST
URL : http://localhost:8000/api/notes/ 
bash
`curl -X POST http://localhost:8000/api/notes/ \
-H "Authorization: Bearer <access_token>" \
-H "Content-Type: application/json" \
-d '{
    "title": "Новая заметка",
    "content": "Это содержимое заметки"
}'`

Ответ (успешно) : 
json
`{
    "id": 2,
    "title": "Новая заметка",
    "content": "Это содержимое заметки",
    "created_at": "...",
    "updated_at": "..."
}`
 
5. Получение заметки по ID  

Описание : Возвращает заметку по ее ID.
Метод : GET
URL : http://localhost:8000/api/notes/<note_id>/ 
bash
`curl -X GET http://localhost:8000/api/notes/1/ \
-H "Authorization: Bearer <access_token>"`

Ответ (успешно) : 
json
`{
    "id": 1,
    "title": "Заметка 1",
    "content": "Содержимое заметки",
    "created_at": "...",
    "updated_at": "..."
}`
 
6. Обновление заметки (PUT)  

Описание : Полное обновление заметки.
Метод : PUT
URL : http://localhost:8000/api/notes/<note_id>/ 
bash
`curl -X PUT http://localhost:8000/api/notes/1/ \
-H "Authorization: Bearer <access_token>" \
-H "Content-Type: application/json" \
-d '{
    "title": "Обновленный заголовок",
    "content": "Новое содержимое"
}'`
 
Ответ (успешно) : 
json
`{
    "id": 1,
    "title": "Обновленный заголовок",
    "content": "Новое содержимое",
    "created_at": "...",
    "updated_at": "..."
}`
 
7. Частичное обновление заметки (PATCH)  

Описание : Обновление отдельных полей заметки.
Метод : PATCH
URL : http://localhost:8000/api/notes/<note_id>/ 
bash
`curl -X PATCH http://localhost:8000/api/notes/1/ \
-H "Authorization: Bearer <access_token>" \
-H "Content-Type: application/json" \
-d '{
    "title": "Новый заголовок"
}'`
 
Ответ (успешно) : 
json
`{
    "id": 1,
    "title": "Новый заголовок",
    "content": "Содержимое заметки",
    "created_at": "...",
    "updated_at": "..."
}`
 
8. Удаление заметки  

Описание : Удаляет заметку по ID.
Метод : DELETE
URL : http://localhost:8000/api/notes/<note_id>/ 
bash
`curl -X DELETE http://localhost:8000/api/notes/1/ \
-H "Authorization: Bearer <access_token>"`
 
Ответ (успешно) : 
HTTP/1.1 204 No Content
 
9. Обновление refresh-токена  

Описание : Получает новый access-токен через refresh-токен.
Метод : POST
URL : http://localhost:8000/api/token/refresh/ 
bash
`curl -X POST http://localhost:8000/api/token/refresh/ \
-H "Content-Type: application/json" \
-d '{
    "refresh": "<refresh_token>"
}'`
 
Ответ (успешно) : 
json
`{
    "access": "новый_access_токен"
}`
 
10. Удаление пользователя (только для администратора)  

Описание : Удаляет пользователя по ID (требуются права администратора).
Метод : DELETE
URL : http://localhost:8000/api/users/<user_id>/ 
bash
`curl -X DELETE http://localhost:8000/api/users/1/ \
-H "Authorization: Bearer <admin_access_token>"`

Ответ (успешно) : 
HTTP/1.1 204 No Content
