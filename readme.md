### Пет-проект по созданию интернет магазина на базе телеграмм бота.

### Цель:
Cоздать и оформить интернет магазин на базе телеграм бота копирующего 
возможности реального интернет магазина по продаже электроники и 
бытовой техники: @store_mitech_bot;

### Технологии и инструменты:
- Язык программирования: Python версии 3.10; 
- СУБД: SQLite в асинхронном режиме (библиотека aiosqlite);
- Инструменты разработки: IDE PyCharm .
- Взаимодействие с Telegram API: aiogram 2.25.1 
- Версионный контроль: Git.

### Пример работы:

<details><summary><b>Скриншоты:</b></summary>

![catalog](/pictures/p1.jpg "catalog") 

![shopping](/pictures/p2.jpg "shopping")

![cart](/pictures/p3.jpg "cart") 

</details>

### Запуск:

1. Скачать файл базы данных и медиа файлы по ссылке: 
"??????????" и поместить в: 
"директорию размещения проекта/telegram_bot/src/db_api/database
(папка из скаченного архива)".

2. Создать файл .env (использутся для хранения переменных окружения 
в проекте) в дирректории telegram_bot: "директория размещения 
проекта/telegram_bot/.env" после чего указать в нем токен для телеграм 
бота в переменной TOKEN_FOR_BOT (следующим образом TOKEN_FOR_BOT=).

3. Установить все зависимости/библиотеки указанные в requirements.txt 

4. Запустить выполнение файла app.py.