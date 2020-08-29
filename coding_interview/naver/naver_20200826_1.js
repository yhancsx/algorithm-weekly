function solution(A) {
  let len = 1;
  let index = 0;
  while (A[index] !== -1) {
    index = A[index];
    len +=1
  }
  return len
}
const A = [2,-1,1];
// const A = [1,4,-1,3,2]
console.log(solution(A))