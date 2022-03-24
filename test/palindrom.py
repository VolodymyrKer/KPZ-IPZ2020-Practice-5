import re


def palindrom(string):
    result = []
    array = re.findall(r"[\w']+", string)
    for value in array:
        if len(value) > 1:
            for i in range(0, int(len(value) / 2)):
                if value[i] == value[len(value) - i - 1]:
                    result.append(value)
    return result
