function foo(itemAssociation) {
  const itemSet = new Set();

  const association = {}
  itemAssociation.forEach(([s,d] )=>{
    if (s in association ) association[s].push(d)
    else association[s] = [d]

    if (d in association ) association[d].push(s)
    else association[d] = [s]

    itemSet.add(s);
    itemSet.add(d)
  })

  let maxSize = -1;
  let maxGroup = [];

  const itemList = Array.from(itemSet).sort();
  const visit = new Set();

  for(let i = 0; i < itemList.length; i++){
    if(visit.has(itemList[i])) continue;
    dfs(itemList[i], [])
  }

  function dfs(item, list) {
    visit.add(item);
    list.push(item);
    let isEnd = true;

    for (const dest of association[item]) {
      if(visit.has(dest)) continue;
      isEnd = false;
      dfs(dest, list)
    }

    if (isEnd) {
      list.sort((a,b)=>a<b?-1:1)
      if (list.length > maxSize || (list.length === maxSize && list < maxGroup)){
        maxSize = list.length;
        maxGroup = list.slice(0)
      }
    }
    list.pop()
  }
  return maxGroup;
}
console.log(foo([['i1', 'i2'], ['i3','i4'], ['i4', `i5`]]))
