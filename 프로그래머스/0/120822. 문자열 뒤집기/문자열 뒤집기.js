function solution(my_string) {
    // 일단~ 문자열을 배열로 만들기~
    const array = Array.from(my_string)
    // 일단 함 찍어보자..
    console.log(array);
    
    // 오케이 그 배열 뒤집고~
    const reverse = array.reverse();
    // 맞나?
    console.log(array);
    
    // 굿. 이제 다시 문자열로 변환!
    // 근데 배열 사이에 암것도 없어야 된대.
    const string = reverse.join('');
    console.log(string);
    
    return string;
}