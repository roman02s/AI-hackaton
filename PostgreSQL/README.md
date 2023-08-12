# Запуск

1) Установка зависимостей
```bash
source ./scripts/script.sh
python3 -m venv pg_env
source pg_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

2) Инициализация базы знаний
```bash
python3 init_db.py
```