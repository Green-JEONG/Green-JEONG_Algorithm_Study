function solution(slice, n) {
    // n명을 피자 조각 수로 나누어 올림
    let answer = Math.ceil(n / slice);
    
    return answer;
}