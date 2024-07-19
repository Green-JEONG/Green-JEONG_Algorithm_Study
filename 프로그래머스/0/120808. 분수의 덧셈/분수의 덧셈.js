// 기약분수: 분모와 분자의 공약수가 1뿐인 분수 (분자와 분모의 최대공약수를 사용하여 나눈 분수)
function solution(numer1, denom1, numer2, denom2) {
    
    // 공통 분모를 구합니다.
    const commonDenom = denom1 * denom2;
    
    // 공통 분모를 가진 각각의 분자의 값을 계산합니다.
    const newNumer1 = numer1 * denom2;
    const newNumer2 = numer2 * denom1;
    
    // 두 분자의 합을 구합니다.
    const addNumer = newNumer1 + newNumer2;
    
    // 최대공약수를 구합니다.
    function gcd(a, b) {
        // b가 0이면, a가 최대공약수
        // b가 0이 아니면, a를 b로 나눈 나머지로 b가 0이 될 때까지 gcd 함수 반복
        return b === 0 ? a : gcd(b, a % b);
    }
    
    const gcdVal = gcd(addNumer, commonDenom);
    
    // 최대공약수로 분자와 분모를 나눕니다.
    const Numer = addNumer / gcdVal;
    const Denom = commonDenom / gcdVal;
    
    return [Numer, Denom];
}