#!/bin/bash

echo "Выбери действие:"
echo "1 - Показать текущую папку"
echo "2 - Показать список файлов"

read choice

if [ "$choice" = "1" ]; then
    pwd
elif [ "$choice" = "2" ]; then
    ls
else
    echo "Неверный выбор"
fi
