# DOCUMENTATION sezbase

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
     