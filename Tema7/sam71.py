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
