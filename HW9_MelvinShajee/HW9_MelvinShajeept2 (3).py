# problem 2
def file_stats(in_file):
    open(in_file, 'r')
    lines = 0
    words = 0
    characters = 0
    for line in in_file:
        lines += 1
        for word in line:
            words += 1
            for character in word:
                characters += 1
    return lines, words, characters

