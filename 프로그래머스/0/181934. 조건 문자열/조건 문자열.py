def solution(ineq, eq, n, m):
    cond = {
        '>=': n >= m,
        '<=': n <= m,
        '>!': n > m,
        '<!': n < m,
    }
    
    return 1 if cond[ineq + eq] else 0