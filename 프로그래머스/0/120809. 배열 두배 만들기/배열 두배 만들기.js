function solution(numbers) {
    // 새 배열 생성
    const answer = [];
    
    // 'numbers' 배열의 원소 하나씩 꺼내기
    // for (초기값; 조건; 증감)
            // 반복할 코드
    for (let i = 0; i < numbers.length; i++) {
        // 각 원소에 두배 적용
        answer.push(numbers[i] * 2);
    }
    
    return answer;
}