/**
 * @param {string} S
 * @return {number[]}
 */
var partitionLabels = function(S) {
    const latest = {}
    for (let i = 0; i < S.length; i++) {
        latest[S[i]] = i;
    }
    const res = [];
    let curLatest = 0;
    let curStart = 0;
    for (let i = 0; i < S.length; i++) {
        curLatest = Math.max(curLatest, latest[S[i]])
        if (i === curLatest) {
            res.push(i- curStart + 1);
            curStart = i+1;
        }
    }
    return res
};



// https://leetcode.com/discuss/interview-question/370112
function substrings(str, k) {
  const latest = {}
  const res = new Set()
  let before = -1;
  for (let i = 0; i < str.length; i++) {
    const c = str[i]
    before = Math.max(before, c in latest? latest[c] : -1);
    if (i-before >= k) {
      res.add(str.slice(i-k+1, i+1));
    }
    latest[c] = i;

  }
  console.log(latest)
  console.log(Array.from(res));
}

const str = 'abc';
const k = 3;
substrings(str, k)