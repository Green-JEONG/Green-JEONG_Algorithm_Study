function solution(rsp) {
    // 각 패에 대해 이기는 패를 정의
    const winningMoves = {
        '2': '0',  // 가위(2)를 이기는 건 바위(0)
        '0': '5',  // 바위(0)를 이기는 건 보(5)
        '5': '2'   // 보(5)를 이기는 건 가위(2)
    };
    
    // 입력받은 rsp의 각 문자에 대해 이기는 패를 찾아 새 문자열 생성
    let result = '';
    for (let i = 0; i < rsp.length; i++) {
        result += winningMoves[rsp[i]];
    }
    
    return result;
}