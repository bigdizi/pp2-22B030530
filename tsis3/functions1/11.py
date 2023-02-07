def check(word):
    if word == word[::-1]:
        return True
    return False

word = input()
print(check(word))