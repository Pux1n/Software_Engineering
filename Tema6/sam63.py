def top3(string):
    counts = {}
    for digit in string:
        digit = int(digit)
        if digit in counts:
            counts[digit] += 1
        else:
            counts[digit] = 1
    sorted_counts = sorted(counts.items(), key=lambda item: item[1])
    last3 = sorted_counts[-3:]
    result = dict(sorted(last3, key=lambda item: item[0]))
    return result


input_string = "1234567778899000"
print(top3(input_string))
