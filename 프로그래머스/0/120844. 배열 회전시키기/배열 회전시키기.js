function solution(numbers, direction) {
    if (direction === "right") {
        // 마지막 원소를 꺼내서 배열의 앞에 추가
        const lastElement = numbers.pop();
        numbers.unshift(lastElement);
    } else {
        // 첫 번째 원소를 꺼내서 배열의 끝에 추가
        const firstElement = numbers.shift();
        numbers.push(firstElement);
    }
    
    return numbers;
}