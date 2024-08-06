function solution(n) {
    // 순서쌍의 개수를 저장할 변수
    let count = 0;

    // 1부터 n까지 모든 숫자를 확인
    for (let i = 1; i <= n; i++) {
        // n이 i로 나누어 떨어지면 카운트 증가
        if (n % i === 0) {
            count++;
        }
    }

    return count;
}