import re


def palindrom(input):
    if len(input) < 3:
        raise Exception("The argument must contain a string of more than 3 characters")
    if not isinstance(input, str):
        raise Exception("The argument must contain the string ")
    result = []
    array = re.findall(r"[\w']+", input)
    for value in array:
        if len(value) > 1:
            if len(value) > 1:
                if value == value[::-1]:
                    result.append(value)
    return result
