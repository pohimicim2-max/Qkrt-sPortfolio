#!/bin/bash
name="Иван"          # переменная
echo "Привет, $name!"  # использование переменной

# Условные операторы
if [ -f "file.txt" ]; then
    echo "Файл существует"
else
    echo "Файл не найден"
fi

# Циклы
for i in {1..5}; do
    echo "Итерация $i"
done

# Функции
greet() {
    echo "Привет, $1!"
}
greet "Мир"  # Привет, Мир!