## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&multiline=true&repeat=false&width=435&height=70&lines=%D0%A4%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82+%D1%81%D0%BF%D1%80%D0%B8%D0%BD%D1%82%D0%B0%3A;API+%D0%B4%D0%BB%D1%8F+Yatube)](https://git.io/typing-svg)

## Описание

Данный проект реализует следующие возможности с помощью REST API(DRF):
* получение списка публикаций или отдельной публикации по id
* добавление, обновление, удаление публикаций
* получение списка доступных сообществ и получение информации о сообществе по id
* получение всех комментариев к публикации или комментария к публикации по id
* добавление, обновление, удаление комментариев
* подписывание на пользователей
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
cd API_FINAL_YATUBE
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```