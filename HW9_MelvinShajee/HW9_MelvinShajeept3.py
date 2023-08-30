# problem 3
def repeat_words (in_file, out_file):
    counted = []
    repeated = []
    for word in in_file:
        if word not in counted:
            counted.append(word)
        elif word not in repeated:
            out_file.write(word)
            repeated.append(word)

