function solution(balls, share) {
    // 조합 계산 함수
    function combination(n, r) {
        if (n === r || r === 0) return 1;
        return combination(n - 1, r - 1) + combination(n - 1, r);
    }
    
    return combination(balls, share);
}