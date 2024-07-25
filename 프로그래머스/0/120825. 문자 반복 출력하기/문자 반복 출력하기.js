function solution(my_string, n) {
    const stringToArr = my_string.split('');
    console.log(stringToArr)
    
    const result = [];
    
    for(let i =0 ; i < stringToArr.length; i++){
        
        // case 1 - for 문
        // for(let j=0; j<n; j++){
        //     result.push(stringToArr[i])
        // }
        
        // case 2 - repeat()함수
        result.push(stringToArr[i].repeat(n))
    };
    console.log(result.join(''))
    
    return result.join('');
}