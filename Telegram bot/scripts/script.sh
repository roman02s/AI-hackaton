#!/bin/bash

# Укажите путь к файлу с переменными окружения
env_file="config.env"

# Проверяем, существует ли файл
if [ -f "$env_file" ]; then
    # Читаем файл построчно
    while IFS= read -r line; do
        # Игнорируем комментарии и пустые строки
        if [[ $line != \#* ]] && [[ ! -z $line ]]; then
            # Разделяем строку на имя переменной и значение
            var_name=$(echo "$line" | cut -d '=' -f 1)
            var_value=$(echo "$line" | cut -d '=' -f 2-)
			printf "$var_name=$var_value\n"
            
            # Устанавливаем переменную окружения
            export "$var_name"="$var_value"
        fi
    done < "$env_file"
    echo "Переменные окружения успешно загружены из файла $env_file"
else
    echo "Файл $env_file не найден"
fi
