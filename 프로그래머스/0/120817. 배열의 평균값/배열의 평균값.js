function solution(numbers) {
    // 모든 원소 값을 더해 원소 수만큼 나누기
    let answer = numbers.reduce((a, c) => a + c) / numbers.length;
    
    return answer;
}