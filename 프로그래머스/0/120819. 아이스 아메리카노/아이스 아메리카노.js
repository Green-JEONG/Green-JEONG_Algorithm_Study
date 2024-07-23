// 가지고 있는 돈을, 아메리카노 한잔의 가격으로 나누어 볼까?
function solution(money) {
    // 일단 아메리카노 가격을..
    const americano = 5500;
    
    // 머쓱이가 최대로 마실 수 있는 아메키라노 잔 수? (소수점 무시)
    const maxAmericano = parseInt(money / americano);
    
    // 그런 다음 남는 돈 계산을..
    const remainingAmount = money - americano * maxAmericano
    
    // 결과를 배열로 반환하기!
    return [maxAmericano, remainingAmount]; 
}