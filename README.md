# bot_anekdot

Данный репозиторий создан в качестве домашнего проекта и несет в себе только образовательную ценность.

Основная идея создания данного проекта:
- Зачастую мы узнаем от друзей смешные шутки и анекдоты, которые рассказываем потом всем подряд
- Но иногда хотелось бы быть более оригинальным и рассказать что-нибудь другое, но при этом похожее

Описание репозиория:
- ml: папка, в которой хранится код для работы модели
- app: содержит код для запуска приложения
- data: папка с предобученными эмбеддингами
- notebooks: ноутбуки с примерами по работе с данными

Запуск проекта:
```console
python -m venv env
env/Scripts/activate
python -m pip install --upgrade pip
pip install -U -e .
uvicorn app.app:app --host 0.0.0.0 --port 8080
```

Запуск через контейнер:
```console
docker-compose up --build
```

Пример работы:
- input
![image](https://github.com/user-attachments/assets/28f790cc-af95-4a6c-874f-892ce718bf5e)

- output
![image](https://github.com/user-attachments/assets/25196ae3-1796-4137-91f0-cd3efe868081)


