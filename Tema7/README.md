# Тема 4. Функции и стандартные модули/библиотеки
Отчет по Теме #4 выполнил(а):
- Белоусов Андрей Андреевич
- ПИЭ-21-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/1.png)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/2.png)

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/3.png)

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    print(f.readlines())
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/4.png)

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/5.png)

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/6.png)

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

lab47.py:
```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/7.png)

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)


print_docs('/Users/Andrey/Downloads')
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/8.png)

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: 
Приветствие 
Спасибо 
Извините 
Пожалуйста 
До свидания 
Ты готов? 
Как дела? 
С днем рождения! 
Удача! 
Я тебя люблю. 
Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных.

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(longest_words('input.txt'))
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/9.png)

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами: 
• № - номер по порядку (от 1 до 300);
• Секунда – текущая секунда на вашем ПК;
• Микросекунда – текущая миллисекунда на часах. 
Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/10.png)


## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация

###Скриншот файла со статьей:
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/s1.1.png)

###Листинг кода:
```python
with open('sam71input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    word_count = {}
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip('.,!?"«»:;–-—()%')
            if not word.isdigit():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    sorted_count = dict(sorted(word_count.items(), key=lambda item: item[1]))
    most_used_word = sorted_count.popitem()
    print(f"Количество слов в тексте: {sum(word_count.values())}")
    print(f"Самое встречаемое слово: '{most_used_word[0]}', встречается {most_used_word[1]} раз.")
```

### Вывод в консоль:
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/s1.2.png)

## Выводы

В данном коде открываетя файл со статьей в режиме чтения в кодировке utf-8 с помощью конструкции with open,
в переменную lines записываются все строки из файла с помощью readlines().
Создается словарь-счетчик слов
Проход по строкам, при котором строка разделяется на слова через пробел, далее вложенный проход по словам, при котором слова отделяются от лишних знаков с помощью strip(), проверяется что слово не число с помощью isdigit() и если слово уже есть в словаре, увеличивается счетчик для этого слова на 1, иначе это слово добавляется в словарь с начальным счетчиком 1.
После прохода словарь сортируется по возрастанию с помощью sorted().
Последний элемент отсортированного списка записывается в переменную как самый частый.
Выводится результат.
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

###Скриншот файла с учетом расходов:
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/s1.2.png)

###Листинг кода:
```python
def input_expenses():
    name = input("\nВведите название расходов: ")
    amount = float(input("Введите сумму расходов: "))

    with open('expenses.txt', 'a', encoding='utf-8') as f:
        f.write(f"{name}: {amount} руб.\n")


def display_expenses():
    try:
        with open('expenses.txt', 'r', encoding='utf-8') as f:
            expenses = f.read()
            print("\nСуществующие расходы:")
            print(expenses)
    except FileNotFoundError:
        print("\nФайл не найден.")


def main():
    while True:
        print("\n1. Ввести информацию о расходах")
        print("2. Вывести существующие расходы")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            input_expenses()
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            break
        else:
            print("\nВведите от 1 до 3!")


if __name__ == "__main__":
    main()
```

### Вывод в консоль.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/s2.png)

## Выводы

В данном коде определяются 3 функции:
1) input_expenses(): Эта функция запрашивает у пользователя ввод информации о расходах, включая название расходов и сумму. Затем она открывает файл expenses.txt в режиме добавления и записывает туда введенный расход.
2) display_expenses(): Эта функция открывает файл 'expenses.txt' если он есть, читает его содержимое и выводит его на экран.
3) main(): Входная функция - главное меню программы,. Она создает бесконечный цикл, в котором с терминала нужно ввести необходимое действие: 1 - вызывает функцию input_expenses(), 2 - вызывает display_expenses(), 3 - прерывает цикл и выходит из программы.
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. 
• Текст в файле: 
Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
• Ожидаемый результат: 
Input file contains: 108 
letters 20 words 
4 lines

```python
with open('input.txt', 'r') as f:
    lines = f.readlines()
    count_letters = 0
    count_words = 0
    count_lines = 0
    for line in lines:
        count_lines += 1
        words = line.split()
        count_words += len(words)
        for char in line:
            if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                count_letters += 1
    print(count_letters, "letters")
    print(count_words, "words")
    print(count_lines, "lines")
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/s3.png)

## Выводы

Открывается файл input.txt в режиме чтения с помощью with open.
В переменную lines записывается весь текст с помощью .readlines()
Определяются переменные-счетчики букв, слов и строк.
Проход по строкам текста, при котором счетчик строк прибавляет 1, строка разбивается на слова в переменную words с помощью split() и счетчик слов становится длине переменной words, далее проход по символам в строке и если символ находится в кириллице, то счет букв прибавляет 1.
Выводится результат.
  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****. 
• Запрещенные слова: 
hello email python the exam wor is 
• Предложение для проверки: 
Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!! 
• Ожидаемый результат: 
*****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!

```python
import re

sentence = 'Hello, world! Python IS the programming language of thE future. My EMAIL is.... \nPYTHON is awesome!!!!'
with open('input.txt', 'r') as f:
    ban_words = f.readline().split()
    for word in ban_words:
        sentence = re.sub(word, len(word)*'*', sentence, flags=re.IGNORECASE)
print(sentence)
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/s4.png)

## Выводы

Импортируется модуль re.
Вводится предложение.
Открывается файл в режиме чтения с помощью with open.
Строка из файла разделяется через пробел на слова, и они записывается в переменную ban_words.
Проход по словам из ban_words, при котором с помощью re.sub запрещенные слова заменяются звездочки умноженные на длину слова, при этом игнорируя регистр.
Выводится результат.
  
## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

###Задание:
###Напишите программу, которая находит часть текста в текстовом файле и считает ее количество.

```python
string = input("Введите текст для поиска: ")
with open('sam71input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text = text.lower()
    count = text.count(string.lower())
    print(f"'{string}' встречается в тексте {count} раз(а).")
```

### Результат.
![Меню](https://github.com/Pux1n/Software_Engineering/blob/Tema7/Tema7/pic/s5.png)

## Выводы

В данную программу с терминала вводится строка, которую нужно найти.
Затем открывается файл с текстом с помощью конструкции with open в режиме чтения и кодировке utf-8 
Считывает содержимое файла в переменную text с использованием file.read().
Все символы в тексте переводятся в нижний регистр с помощью text.lower(), чтоб регистр не мешал поиску.
С помощью count() считается сколько раз встречается введенная строка, и результат сохраняется в переменной count.
Выводится результат.

## Общие выводы по теме

В результате ознакомления с теоретическим материалом и выполнения лабораторных и самостоятельных работ, я научился работать с файлами в Python.
