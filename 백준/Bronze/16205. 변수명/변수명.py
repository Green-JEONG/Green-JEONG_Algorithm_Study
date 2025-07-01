style, name = input().split()

if style == '2':
    words = name.split('_')
else:
    words = []
    word = ''
    for ch in name:
        if ch.isupper():
            if word:
                words.append(word)
            word = ch.lower()
        else:
            word += ch
    words.append(word) 
     
camel = words[0] + ''.join(w.capitalize() for w in words[1:])

snake = '_'.join(words)

pascal = ''.join(w.capitalize() for w in words)

print(camel)
print(snake)
print(pascal)