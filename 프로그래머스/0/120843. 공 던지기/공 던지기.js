function solution(numbers, k) {
    // 공을 던지는 위치 계산
    const position = (k - 1) * 2 % numbers.length;
    
    // 해당 위치의 번호 반환
    return numbers[position];
}