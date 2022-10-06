def rangeDecrement(n):
    x = 0
    for i in range(n, -1, -1):
        x += i

def reversedDecrement(n):
    x = 0
    for i in reversed(range(n)):
        x += i

def reversedWord(word):
    rev = reversed(word)
    print(rev)

def revSlice(word):
    rev = word[::-1]
    print(rev)