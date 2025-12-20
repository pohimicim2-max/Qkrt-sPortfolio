#!/bin/bash
# Это комментарий - скрипт для создания проекта

echo "Создание нового проекта..."
read -p "Введите имя проекта: " project_name

mkdir "$project_name"
cd "$project_name" || exit

# Создание структуры
mkdir src tests docs
touch README.md main.py requirements.txt

echo "Проект '$project_name' создан!"
echo "Структура:"
tree