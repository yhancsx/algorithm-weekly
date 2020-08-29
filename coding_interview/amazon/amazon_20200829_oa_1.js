function foo(flightDuration, movieDuration) {
  // Write your code here
  const sum = flightDuration - 30;
  let maxSum = -1;
  let maxSumRes = [-1,-1];
  const durations = movieDuration.map((duration, i) =>
      [duration, i],
  ).sort((a, b) => b[0] - a[0]);

  for(let i = 0; i < durations.length ; i++){
    const curSize = durations[i][0];
    const curIndex= durations[i][1];
    const target = sum - curSize;
    let l = 0, r = durations.length-1;
    let m;
    while(l < r) {
      m = Math.floor((l+r) /2);
      if(target > durations[m][0]) r = m;
      else if (target < durations[m][0]) l = m+1;
      else {
        l = m;
        break;
      }
    }
    if (durations[l][1] === curIndex) {
      if (durations[l-1] && durations[l-1][0] === durations[l][0]) l--;
      else l+=1
    }
    if (l > -1 && l < movieDuration.length){
      const findSize = durations[l][0];
      const findIndex = durations[l][1];
      if (curSize + findSize> maxSum && curSize + durations[l][0] <= sum) {
        maxSum = curSize + findSize;
        maxSumRes = [curIndex, findIndex]
      }
    }
  }

  return maxSumRes.sort((a,b) => a-b)
}
const flightDuration = 30;
const movieDuration = [ 20,30,40,0,10,0];
console.log(foo(flightDuration, movieDuration));
