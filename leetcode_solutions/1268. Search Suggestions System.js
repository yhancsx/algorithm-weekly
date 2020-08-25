
// n: products.length === 1000
// k: products[i].length === 20
// s: searchWord.length === 1000

// sol 1) knslogs
function add(obj, key, value) {
    if (! (key in obj)) obj[key] = [value];
    else {
        obj[key].push(value)
        obj[key].sort()
        if (obj[key].length === 4) {
            obj[key].pop()
        }
    }
}
var suggestedProducts = function(products, searchWord) {
    const obj = {}
    products.forEach(product => {
        for (let i = 0; i < product.length; i++) {
            cont acc = product.slice(0, i+1);
            add(obj, acc, product)
        }
    })
    const ret = []
    for (let i = 0; i < searchWord.length; i++ ) {
        cont acc = product.slice(0, i+1);
        ret.push(acc in obj? obj[acc] : [])
    }
    return ret
};

// sol 2) knlogn + sslogn
var suggestedProducts = function(products, searchWord) {
    products.sort()

    function bsearch(keyword) {
        let l = 0; r = products.length - 1;
        let m;
        while(l < r) {
            m = Math.floor((l+r)/2);
            if (products[m] > keyword) r = m
            else if(products[m] < keyword) l = m + 1
            else return m
        }
        return l;

    }
    const ret = []
    for (let i = 0; i < searchWord.length; i ++) {
        const acc = searchWord.slice(0, i+1)
        const index = bsearch(acc)
        const candidates = products.slice(index, index+3).filter(x=>x.includes(acc))
        ret.push(candidates)
    }
    return ret
};