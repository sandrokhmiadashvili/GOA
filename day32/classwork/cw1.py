def my_join(separator, items):
    result = ""

    for i in range(len(items)):
        result += items[i]

        if i != len(items) - 1:
            result += separator

    return result

print(my_join("-", ["a", "b", "c"]))  # a-b-c