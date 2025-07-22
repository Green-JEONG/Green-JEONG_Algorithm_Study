def solution(spell, dic):
    order = ''.join(sorted(spell))

    for i in dic:
        if ''.join(sorted(i)) == order:
            return 1

    return 2