sentences = ["HELLO WORLD", "The ugly goose", "The end"]

for i in sentences:
    sent = i
    print("Предложение:", sent)
    print("Длина:", len(sent))
    print("В нижнем регистре:", sent.lower())
    vowels = 0
    for char in sent:
        if char in "aeiouAEIOU":
            vowels += 1
    print("Гласных:", vowels)
    print("Замена слов:", sent.replace("ugly", "beauty"))
    if sent.startswith("The"):
        print("Начинается с 'The'")
    else:
        print("Не начинается с 'The'")
    if sent.endswith("end"):
        print("Заканчивается на 'end'")
    else:
        print("Не заканчивается на 'end'\n")
