# MAX-бот на maxapi

Пример бота на [maxapi](https://github.com/love-apples/maxapi) (Python), которого можно развернуть в **Timeweb Cloud Apps**.

Бот работает через long polling и отвечает на простые команды:

| Команда | Ответ |
| --- | --- |
| `/start` | приветствие |
| `/help` | список команд |
| `/ping` | `pong` |
| любой текст | повторяет сообщение |

:rocket: [Создать свой Apps](https://timeweb.cloud/my/apps/create)

:books: [Документация Timeweb Cloud Apps](https://timeweb.cloud/docs/apps)

## Параметры деплоя

Выберите язык **Python**, фреймворк **maxapi** и тип приложения **backend**.

| Параметр | Значение |
| --- | --- |
| Фреймворк | maxapi |
| Версия Python | 3.13 |
| Тип приложения | `backend` |
| Команда сборки | `pip install --upgrade -r requirements.txt` |
| Команда запуска | `python3 main.py` |

## Переменные окружения

| Переменная | Описание |
| --- | --- |
| `BOT_TOKEN` | токен бота мессенджера MAX (выдаётся при создании бота на платформе для партнёров MAX) |

## <a name="dev"></a>Локальный запуск проекта

```bash
# установка зависимостей
pip3 install -r requirements.txt

# запуск бота
BOT_TOKEN=<токен> python3 main.py
```
