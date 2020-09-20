function solution(table) {
  const categoryCount = table[0].length;
  const itemList = table.map(item => item.split('').
      map((simbol, index) => simbol === 'O' ? index : -1).
      filter(simbol => simbol >= 0));
  let left = 1, right = itemList.length;
  let mid;
  while (left < right) {
    mid = Math.floor((left + right) / 2);
    if (canMakeEntireList(itemList, mid, categoryCount)) right = mid;
    else left = mid + 1;
  }
  return left;
}

function canMakeEntireList(itemList, itemCount, categoryCount) {
  function dfs(index, itemIndexes) {
    if (index >= itemList.length) {
      if (itemIndexes.length === itemCount) {
        const concat = itemIndexes.flatMap((a) => a);
        if (new Set(concat).size === categoryCount) return true;
      }
      return false;
    }

    for (let i = index; i < itemList.length; i++) {
      itemIndexes.push(itemList[index]);
      if (dfs(index + 1, itemIndexes)) return true;
      itemIndexes.pop();
      if (dfs(index + 1, itemIndexes)) return true;
    }
    return false;
  }

  return dfs(0, []);
}

console.log(solution(['XOXO', 'OXXO', 'XXOX', 'XOOO']));
console.log(solution(['OXXO', 'XOXO', 'XXOO']));
console.log(solution(['OXOXO', 'OOOOO', 'XOXOX']));
