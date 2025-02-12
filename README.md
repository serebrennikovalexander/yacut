# Сервис укорачивания ссылок YaCut
### Описание
Сервис позволяет ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.\
Ключевые возможности сервиса:
* генерация коротких ссылок и их связь с исходными длинными ссылками
* переадресация на исходный адрес при обращении к коротким ссылкам
### Технологии
Python 3.10\
Flask 3.1.0\
SQLAlchemy 2.0.21\
alembic 1.12.0\
Jinja2 3.1.4
### Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:serebrennikovalexander/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Запустить проект:

```
flask run
```

### Автор
Александр Серебренников