def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    return ''.join([ch for ch in my_string if ch not in vowel])