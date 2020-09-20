function solution(h, w, n, board) {
  let answer = 0;
  // horizontal
  for(let i = 0;i<h;i++) {
    let acc = 0;
    for(let j = 0; j < w; j++) {
      if (board[i][j] === '1') acc +=1;
      else {
        if(acc === n) answer +=1;
        acc = 0;
      }
    }
    if(acc === n) answer +=1;
  }

  // vertical
  for(let j = 0;j < w;j++) {
    let acc = 0;
    for(let i = 0; i < h; i++) {
      if (board[i][j] === '1') acc +=1;
      else {
        if(acc === n) answer +=1;
        acc = 0;
      }
    }
    if(acc === n) answer +=1;
  }

  // leftbottom to righttop
  let startI = 0, startJ = 0;
  while(startJ < w){
    let acc = 0;
    let moveI = 0, moveJ = 0;
    while (startI + moveI >=0 && startJ + moveJ < w) {
      const i = startI + moveI, j = startJ + moveJ;
      if (board[i][j] === '1') acc +=1;
      else {
        if(acc === n) answer +=1;
        acc = 0;
      }
      moveI-=1
      moveJ+=1;
    }
    if(acc === n) answer +=1;
    if (startI < h-1) startI+=1;
    else startJ+=1;
  }

  // lefttop to rightbottom
  startI = h-1; startJ = 0;
  while(startJ < w){
    let acc = 0;
    let moveI = 0, moveJ = 0;
    while (startI + moveI <h && startJ + moveJ < w) {
      const i = startI + moveI, j = startJ + moveJ;
      if (board[i][j] === '1') acc +=1;
      else {
        if(acc === n) answer +=1;
        acc = 0;
      }
      moveI+=1
      moveJ+=1;
    }
    if(acc === n) answer +=1;
    if (startI > 0) startI-=1;
    else startJ+=1;
  }

  return answer;
}

console.log(solution(7,	9,	4,	["111100000","000010011","111100011","111110011","111100011","111100010","111100000"]))
console.log(solution(5,	5,	5,	["11111","11111","11111","11111","11111"]))
