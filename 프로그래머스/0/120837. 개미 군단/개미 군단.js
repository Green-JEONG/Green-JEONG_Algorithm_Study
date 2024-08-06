function solution(hp) {
    let antCount = 0;  // 총 개미의 수
    
    // 장군개미 사용 (공격력 5)
    antCount += Math.floor(hp / 5);
    hp = hp % 5;  // 남은 체력 계산
    
    // 병정개미 사용 (공격력 3)
    antCount += Math.floor(hp / 3);
    hp = hp % 3;  // 남은 체력 계산
    
    // 일개미 사용 (공격력 1)
    antCount += hp;  // 남은 체력이 곧 필요한 일개미의 수
    
    return antCount;
}