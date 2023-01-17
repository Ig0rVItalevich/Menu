## Задание

Написать проект на FastAPI с использованием PostgreSQL в качестве БД. В проекте следует реализовать
REST API по работе с меню ресторана, все CRUD операции. Для проверки задания, к презентаций будет
приложена Postman коллекция с тестами. Задание выполнено, если все тесты проходят успешно.

Даны 3 сущности: Меню, Подменю, Блюдо.

Зависимости:
- У меню есть подменю, которые к ней привязаны.
- У подменю есть блюда.
Условия:
- Блюдо не может быть привязано напрямую к меню, минуя подменю.
- Блюдо не может находиться в 2-х подменю одновременно.
- Подменю не может находиться в 2-х меню одновременно.
- Если удалить меню, должны удалиться все подменю и блюда этого меню.
- Если удалить подменю, должны удалиться все блюда этого подменю.
- Цены блюд выводить с округлением до 2 знаков после запятой.
- Во время выдачи списка меню, для каждого меню добавлять кол-во подменю и блюд в этом меню.
- Во время выдачи списка подменю, для каждого подменю добавлять кол-во блюд в этом подменю.
- Во время запуска тестового сценария БД должна быть пуста.

## Инструкция по запуску

Тестирование проводилось на ОС Linux Ubuntu.

1. Склонировать репозиторий с помощью команды ```git clone https://github.com/Ig0rVItalevich/Menu.git```

2. Перейти в каталог проекта ```cd ./Menu/app```

3. Подставить свои данные БД в файл **config.ini** 

4. Создать виртуальное окружение ```python3 -m venv venv```

5. Активировать виртуальное окружение ```source venv/bin/activate```

6. Установить библиотеки и зависимости ```pip install -r requirements.txt```

7. Запустить сервер ```uvicorn main:app --reload```