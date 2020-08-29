function reverse(a) {
  return a === 0 ? 1 : 0;
}

function solution(A) {
  let min = Number.MAX_VALUE;

  function dfs(index, count) {
    if (count >= min) return;
    if (index === A.length - 1) {
      min = Math.min(min, count);
      return;
    }
    if (A[index] !== A[index+1]) dfs(index+1, count)
    else {
      A[index+1] = reverse(A[index+1]);
      dfs(index+1, count +1);
      A[index+1] = reverse(A[index+1]);
    }
  }

  dfs(0, 0);
  if (A[0]  === A[1]) {
    A[0] = reverse(A[0]);
    dfs(0, 1);
  }

  return min;
}

const A = [1,1,1,1,1,0,1];
console.log(solution(A))
