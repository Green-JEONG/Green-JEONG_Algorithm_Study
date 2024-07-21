function solution(array) {
    // 배열을 오름차순으로 정렬
    array.sort((a, b) => a - b);
    
    // 배열의 길이를 반으로 나눈 값
    let half = parseInt(array.length / 2);
    
    return array[half];
}