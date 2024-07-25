function solution(my_string, letter) {
    // 새 문자열
    let answer = '';
    
    // 전체 문자 확인
    for (let i = 0; i < my_string.length; i++) {
        // 제거할 문자와 다른 경우
        if (my_string[i] !== letter) {
            answer += my_string[i]; // 새 문자열에 추가
        }
    }
    
    return answer;
}