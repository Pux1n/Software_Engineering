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
