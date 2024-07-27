function solution(numbers, num1, num2) {
    // slice 메소드: 첫 번째 인덱스부터 두 번째 인덱스 전까지 요소들 복사하여 새 배열 생성
    return numbers.slice(num1, num2 +1); // num2번째 인덱스까지 포함하기 위해 num2 + 1
}