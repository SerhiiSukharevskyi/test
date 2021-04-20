def chek(s):
    for i in range(len(s)//2):
        if s[i] != s[-1 - i]:
            return False

    return True

word = input("слово которое проверить  ")

if chek(word):
    print('word is Palindrom')
else:
    print("word isn't palindrom")