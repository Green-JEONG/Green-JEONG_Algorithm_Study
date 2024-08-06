function solution(emergency) {
    // 원본 배열을 내림차순으로 정렬한 새 배열 생성
    const sorted = [...emergency].sort((a, b) => b - a);
    
    // 원본 배열의 각 요소에 대해 정렬된 배열에서의 위치(순위)를 찾아 반환
    return emergency.map(e => sorted.indexOf(e) + 1);
}