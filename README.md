# formsChecker

## Установка и использование приложения formsChecker

### Установка

1. **Клонирование репозитория:**
   ```bash
   git clone https://github.com/SergeyKurilko/formsChecker.git
   cd formsChecker
   ```
2. **Создание и активировация виртуального окружения:**
   ```bash
     python3 -m venv venv
     source venv/bin/activate  # Для Linux/MacOS
    # или
     venv\Scripts\activate  # Для Windows
   ```
3. **Установка зависимосией**
   ```bash
   pip install -r requirements.txt
   ```
4. **Запуск сервера**
   ```bash
   uvicorn main:app --reload
   ```

После запуска, сервер будет доступен по адресу http://127.0.0.1:8000.
У приложения имеется один единственный API Endpoint с адресом: `/get_form`
Этот эндпоинт принимет POST с данными в формате x-www-form-urlencoded и возвращает 
имя подходящего шаблона формы или типы полей, если подходящий шаблон не найден.

Для запуска тестов исользовать скрипт tests.py:
```bash
python3 tests.py
```
