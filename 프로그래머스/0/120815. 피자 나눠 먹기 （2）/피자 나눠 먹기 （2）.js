function solution(n) {
    // 초기 피자 조각 수 및 판 수
    const pizzaPiece = 6;
    let pizzaNum = 1;
    
    // 초기 피자 조각 수 및 판 수의 곱이 n으로 나누어지는 값이 최소 피자 판 수
    while ((pizzaPiece * pizzaNum) % n !== 0) {
        pizzaNum++;
    }
    
    return pizzaNum;
}