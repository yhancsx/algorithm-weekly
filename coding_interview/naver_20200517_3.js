function solution(S) {
  const stack = [];
  let top = -1;
  for (const c of S) {
    if (stack.length === 0) {
      stack.push(c)
      top ++;
    }
    else {
      const t = stack[top];
      if ((c==='A' && t ==='B') || (c==='B' && t ==='A') || (c==='C' && t ==='D') || (c==='D' && t ==='C')){
        stack.pop();
        top --;
      } else {
        stack.push(c);
        top++;
      }

    }

  }
  return stack.join('')
}

const s = 'CBACD';
console.log(solution(s));
