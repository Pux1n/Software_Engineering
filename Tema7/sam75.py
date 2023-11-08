def find(string_to_find):
    with open('sam71input.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.lower()
        count = text.count(string_to_find.lower())
        return count


string = input("Введите текст для поиска: ")
word_count = find(string)

print(f"'{string}' встречается в тексте {word_count} раз(а).")
