def solution(numbers):
    names = ['zero', 'one', 'two', 'three', 'four',
            'five','six', 'seven', 'eight', 'nine']
    
    for i, name in enumerate(names):
        numbers = numbers.replace(name, str(i))
        
    return int(numbers)