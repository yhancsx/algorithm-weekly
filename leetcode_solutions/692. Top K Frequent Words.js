/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function(words, k) {
    const counts = {}
    words.forEach((word) => {
        if (word in counts) counts[word] +=1;
        else counts[word] = 1;
    })

    const entries = Object.entries(counts);

    function quickSelect(left, right) {
        const pivot = left;
        let l = left, r = right;
        while(l < r) {
            while(l < r && (entries[r][1] < entries[pivot][1] || entries[r][1] === entries[pivot][1] && entries[r][0]  > entries[pivot][0]))
                r-=1;

            while(l < r && (entries[l][1] > entries[pivot][1] || entries[l][1] === entries[pivot][1] && entries[l][0]  < entries[pivot][0]))
                l+=1;

            const tmp = entries[l];
            entries[l] = entries[r];
            entries[r] = tmp;
        }

        const tmp = entries[pivot];
        entries[pivot] = entries[l];
        entries[l] = tmp;


        if (l + 1 === k) return entries.slice(0, l+1)
        if (l + 1 < k) return quickSelect(l+1, right)
        if (l + 1 > k) return quickSelect(left, l-1)
    }

    return quickSelect(0, entries.length - 1).map(([k,v]) => k)
};