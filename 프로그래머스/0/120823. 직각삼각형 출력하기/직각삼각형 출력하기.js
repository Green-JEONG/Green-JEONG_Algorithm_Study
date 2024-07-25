const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    // console.log(line)
    for(let i=0; i<line; i++){
        console.log('*'.repeat(i+1))
    }
})

// function isoscelesRightTriangle(n) {
//     // 1부터 n까지 반복
//     for (let i = 1; i <= n; i++) {
//         // 한 줄마다 i개의 "*" 출력
//         console.log("*".repeat(i));
//     }
// }

// isoscelesRightTriangle(3);