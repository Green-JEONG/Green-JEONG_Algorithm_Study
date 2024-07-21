function solution(n) {
    // 피자 조각 수
    const pizzaPiece = 7;
    
    // 필요한 피자 수: 한 조각씩 먹어야 하므로 올림 계산
    let pizzaNum = Math.ceil( n / pizzaPiece );
    
    return pizzaNum;
}