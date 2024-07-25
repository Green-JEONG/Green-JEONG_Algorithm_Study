function solution(n, k) {
    const skewers = 12000;
    const beverage = 2000;
    
    const skewersCost = n * skewers;
    const freeBeverage = parseInt(n / 10);
    
    const beverageNum = k - freeBeverage;
    const beverageCost = beverageNum * beverage;
    
    const totalCost = skewersCost + beverageCost;
    
    return totalCost;
}