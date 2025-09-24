def solution(ineq, eq, n, m):
    if ineq+eq == ">=":
        return int(bool(n >= m))
    elif ineq+eq == "<=":
        return int(bool(n <= m))
    elif ineq+eq == ">!":
        return int(bool(n > m))
    elif ineq+eq == "<!":
        return int(bool(n < m))