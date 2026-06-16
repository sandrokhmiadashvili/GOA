def my_split(text, separator):
    result = []
    word = ""

    for char in text:
        if char == separator:
            result.append(word)
            word = ""
        else:
            word += char

    result.append(word)
    return result

print(my_split("a-b-c", "-"))  # ['a', 'b', 'c']