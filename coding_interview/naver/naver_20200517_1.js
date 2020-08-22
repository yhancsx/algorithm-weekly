function solution(N) {
  if (N === 0) return 50;

  let n = N >=0? N : -N;
  let q = 0;
  let divide = 1;
  while (n >= 10){
    divide *= 10;

    n = Math.floor(n / 10);
  }

  if (N >= 0) {
    n = N;
    while (n && divide){
      q = Math.floor(n / divide);
      if (q>0 && q <= 5) break;

      n %= divide;
      divide /= 10;
    }
    return Math.floor(N / (divide*10))*divide*100 + 5*(divide*10) + n
  }else{
    n = -N;
    while (n && divide){
      q = Math.floor(n / divide);
      if (q>0 && q >= 5) break;

      n %= divide;
      divide /= 10;
    }
    return -1 * (Math.floor(-N / (divide*10))*divide*100 + 5*(divide*10) + n)
  }
}

console.log(solution(986213));
