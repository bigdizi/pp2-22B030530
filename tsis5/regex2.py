import re


def text_match(text):
    patterns = '^a(bb+)$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("ac"))
print(text_match("a"))
print(text_match("abb"))