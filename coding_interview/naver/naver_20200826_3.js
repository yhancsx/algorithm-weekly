function solution(T) {
  let max = Number.MIN_SAFE_INTEGER;
  let min = Number.MAX_SAFE_INTEGER;
  const maxs = T.map(v => {
    max = Math.max(v, max);
    return max;
  });
  const mins = T.reverse().map(v => {
    min = Math.min(v, min);
    return min;
  }).reverse();
  for (let i = 0; i < T.length-1; i++) {
    if(maxs[i] < mins[i+1]) return i+1;
  }
  return -1
}

function solution2(T) {
  let max = Number.MIN_SAFE_INTEGER;
  let min = Number.MAX_SAFE_INTEGER;
  const mins = [...T].reverse().map(v => {
    min = Math.min(v, min);
    return min;
  }).reverse();
  for (let i = 0; i < T.length-1; i++) {
    max = Math.max(max, T[i]);
    if(max < mins[i+1]) return i+1;
  }
  return -1
}

const T = [5,-2,3,8,6]
// const T = [-5,-5,-5,-42,6,12];
// const T = [-3,-4,-5,-6,-5,-4,0,-2,0];
// const T = [5,4,3,2,1,6,3,7,1];
// const T = [1,2,3,0,4,2,6];
// console.log(solution((T)));
console.log(solution2((T)));


