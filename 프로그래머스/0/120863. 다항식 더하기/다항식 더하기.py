def solution(polynomial):
    apart = polynomial.split(' + ')
    x_sum = 0
    n_sum = 0
    
    for a in apart:
        if 'x' in a:
            if a == 'x':
                x_sum += 1
            else:
                x_sum += int(a.replace('x', ''))
        else:
            n_sum += int(a)
            
    result = []
    if x_sum:
        result.append(f'{x_sum}x' if x_sum > 1 else 'x')
    if n_sum:
        result.append(str(n_sum))
        
    return ' + '.join(result)