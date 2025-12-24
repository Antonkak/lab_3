# Лабораторная работа №3: Алгоритмический мини-пакет
Реализация классических алгоритмов сортировки, рекурсивных и итеративных функций, структур данных и CLI-интерфейса на Python.

Реализовать набор алгоритмов и структур данных без использования встроенных сортировок (list.sort(), sorted()), обеспечить корректную обработку ошибок и предоставить удобный интерфейс для взаимодействия через командную строку.

## Реализованные функции
Обязательная часть (Easy)
 Числовые функции
factorial(n) — итеративное вычисление факториала
factorial_recursive(n) — рекурсивная версия
fibo(n) — итеративное вычисление n-го числа Фибоначчи
fibo_recursive(n) — рекурсивная версия
Все функции корректно обрабатывают отрицательные входные значения (выбрасывают ValueError).

 Алгоритмы сортировки (без sorted() и list.sort())
bubble_sort
quick_sort
counting_sort
radix_sort
bucket_sort
heap_sort
 Структура данных
Стек на list с методами:
push(x: int)
pop() → int
peek() → int
is_empty() → bool
__len__() → int
Все операции на пустом стеке выбрасывают IndexError.
## Дополнительная часть (Medium)
CLI-интерфейс поддержка команд через typer
Интерактивный режим — сессия с командами factorial, fibo, sort, stack
Рекурсивные версии доступны как через CLI (-r), так и в интерактиве (-r)
Тесты — покрытие CLI и интерактивного режима (pytest)
 ## Архитектура решения
 ```

lab3/
├── src/
│   ├── algo/
│   │   ├── factorial.py
│   │   ├── fibo.py
│   │   ├── sorts.py
│   ├── structs.py/
│   │   ├── stack.py
│   ├── const.py
│   └── main.py
├── tests/
```
## Справка по использованию
Общая справка
```
bash
python -m src.main --help
```
Справка по командам
```
bash
python -m src.main factorial-cmd --help
python -m src.main sort-cmd --help
python -m src.main stack --help
```
Примеры использования
Факториал и Фибоначчи
```
bash
python -m src.main factorial-cmd 5
# 5! = 120 (iterative)

python -m src.main factorial-cmd 5 -r
# 5! = 120 (recursive)

python -m src.main fibo-cmd 10 -r
# F(10) = 55 (recursive)
```
Сортировка
```
bash
python -m src.main sort-cmd "3 1 4 1 5" --algo quick
# 1 1 3 4 5

python -m src.main sort-cmd --algo bucket "0.3 0.1 0.9"
# 0.1 0.3 0.9
```
Стек
```
bash
python -m src.main stack "push 10 push 20 pop peek"
# pop: 20
# peek: 10
```
Интерактивный режим
```
bash
python -m src.main interactive
```
Внутри:


```
lab3> factorial 4
4! = 24 (iterative)

lab3> fibo rec 6
F(6) = 8 (recursive)

lab3> sort bubble 5 2 8
 2 5 8

lab3> stack push 100
```
 ## Запуск
Установка зависимостей
```
bash
pip install -r requirements.txt
```
Запуск CLI
```
bash
python -m src.main <command> [options]
```
Запуск интерактивной оболочки
```
bash
python -m src.main interactive
```
## Безопасность и проверки
Все функции проверяют корректность входных данных (n >= 0 и т.д.)
Стек выбрасывает IndexError при операциях над пустым стеком
Сортировки корректно обрабатывают пустые списки
