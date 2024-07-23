function solution(array) {
    
    // 각 숫자 카운트를 위한 객체 생성
    const count = {};

    // 배열 숫자 하나씩 살펴보기
    for(let num of array) {
        // 객체에 그 숫자가 있으면 1 더하고, 없으면 새로 1로 설정
        if (count[num]) {
            count[num] += 1;
        } else {
            count[num] = 1;
        }
    }
    
    console.log(count);
    
    // maxCount: 지금까지 찾은 숫자 중 가장 많이 나온 횟수 저장
    let maxCount = 0;    
    // mode: 가장 많이 나온 숫자 저장
    let mode = -1;
    // 동일한 최빈값이 여러 개 있는지 여부 저장
    let isMultiple = false;
    
    // 객체의 각 숫자와 그 개수 비교
    for (let num in count) {
        // 현재 숫자가 지금까지 가장 많이 나온 숫자보다 많이 나오면 갱신
        if (count[num] > maxCount) {
            maxCount = count[num];
            mode = num;
            isMultiple = false; // 새 최빈값 찾은 후, 중복 여부 초기화
        } else if (count[num] === maxCount) {
            isMultiple = true; // 동일한 최빈값을 또 찾으면, 중복으로 설정
        } 
    }
    
    // 최빈값이 여러 개 있는지 확인하고, 있다면 -1 반환
    if (isMultiple) {
        return -1;
    } else {
        return parseInt(mode);
    }
    
    /* 
       아래 코드는 위와 동일
       return multiple ? -1 : mode;
    */
}