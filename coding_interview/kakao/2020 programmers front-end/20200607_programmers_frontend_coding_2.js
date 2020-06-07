function solution(N, facility) {
  let sol = Number.MAX_SAFE_INTEGER;
  for (let i = 1; i <= N; i++) {
    for (let j = 1; j <=N; j++) {
      let new_sol = -1;
      for (const fa of facility) {
        const cost = (Math.abs(i-fa[0]) + Math.abs(j-fa[1])) * fa[2];
        if (cost > new_sol) new_sol = cost;
        if (cost >= sol) break;
      }
      if (new_sol < sol) sol = new_sol
    }
  }
  return sol;
}



const n = 3;
const facility = [[1,1,1]];


console.log(solution(n, facility))
