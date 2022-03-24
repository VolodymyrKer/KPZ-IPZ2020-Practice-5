import re


def palindrom(string):
    result = []
    array = re.findall(r"[\w']+", string)
    for value in array:
        if len(value) > 1:
            if len(value) > 1:
                if value == value[::-1]:
                    result.append(value)
    return result
