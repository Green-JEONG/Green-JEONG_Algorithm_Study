function solution(dot) {
    const x = dot[0];
    const y = dot[1];
    
    if (x > 0 && y > 0) {
        return 1;  // 제1사분면
    } else if (x < 0 && y > 0) {
        return 2;  // 제2사분면
    } else if (x < 0 && y < 0) {
        return 3;  // 제3사분면
    } else {
        return 4;  // 제4사분면
    }
}