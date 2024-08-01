function solution(age) {
    // 0~9를 a~j에 순서대로 대응
    const alphabet = 'abcdefghij';
    
    // 1. 숫자를 문자열로 변환
    // 2. 문자열을 각 문자로 나누기
    // 3. 숫자를 알파벳으로 대응하게 변환
    // 4. 하나의 문자열로 합치기
    return String(age).split('').map(num => alphabet[num]).join('');
}