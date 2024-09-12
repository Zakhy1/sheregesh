## Авторизация и регистрация

### Регистрация

`/users/register/`
Необходимо отправить в теле:

```json
{
  "email": "email@mail.ru",
  "password": "passwrdo#rc"
}
```

### Авторизация

Происходит при отправке в теле:

```json 
{
  "email": "email@mail.ru",
  "password": "passwrdo#rc"
}
```

В ответ приходит токен

```json
{
  "token": "4c91eda070d33b0ce3ffbe2de3a70eebe04b914e"
}
```

Который необходимо использовать в заголовке
`Authorization: Token <token>`