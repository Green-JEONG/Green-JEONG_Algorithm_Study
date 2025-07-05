function solution(numer1, denom1, numer2, denom2) {
    // 기약분수: 분모와 분자의 공약수가 1뿐인 분수 (분자와 분모의 최대공약수를 사용하여 나눈 분수)
    const numer = numer1 * denom2 + numer2 * denom1;
    const denom = denom1  * denom2;
    
    function gcd(a, b) {
        while (b !== 0) {
            const temp = b;
            b  =  a % b;
            a  = temp;
        }
        return a;
    }
    const common = gcd(numer,  denom);
    
    return [numer / common, denom / common]
}