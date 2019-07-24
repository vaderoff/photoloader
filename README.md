# PHOTOLOADER

## Содержание

- [Задача](#about)
- [Подготовка](#prerequisites)
- [Деплой](#deployment)
- [Примеры запросов](#usage)

## Задача <a name = "about"></a>

Разработать REST API сервер для хранения фотографий. Сервер предполагает наличие двух запросов, с помощью которых можно будет отправлять для хранения фотографии и просматривать все добавленные ранее фотографии. Помимо запросов требуется реализовать панель администратора, в которой можно просматривать добавленные фотографии.

### Подготовка <a name = "prerequisites"></a>

Нужен docker и docker-compose

```
sudo apt install docker docker-compose
```

### Деплой <a name = "deployment"></a>

Просто запускаем магию докера
```
sudo docker-compose up -d --build
```

Делаем миграции и создаем суперюзера
```
sudo docker-compose exec app bash
>> python manage.py migrate
>> python manage.py createsuperuser
```

### Примеры запросов <a name = "usage"></a>

Есть всего два REST запроса:
* Добавление фотографий в систему
* Выгрузка информации по всем загруженным фотографиям
  
| Method | Request | Parameters                                                | Response                                                         |
| ------ | ------- | --------------------------------------------------------- | ---------------------------------------------------------------- |
| GET    | photos  | Параметры для фильтрации: { "date": string, "size": int } | 200 [{ "date": string, "place": string, "path_to_img": string }] |
| POST   | photo   | { "place": string, "img": image }                         | 200                                                              |
  