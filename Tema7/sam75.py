def find(word_to_find):
    with open('sam71input.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.lower()
        count = text.count(word_to_find.lower())
        return count


word = input("Введите текст для поиска: ")
word_count = find(word)

print(f"'{word}' встречается в тексте {word_count} раз(а).")
