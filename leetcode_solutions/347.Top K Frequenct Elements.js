/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const counts = nums.reduce((acc, cur)=> {
        if (cur in acc)
            acc[cur] +=1
        else
            acc[cur] = 1
        return acc
    }, {})
    const entries = Object.entries(counts)
    function quickSelection(left, right) {
        let l = left, r = right;
        const pivot = left;
        while (l < r) {
            while (entries[r][1] <= entries[pivot][1] && l < r) r-=1
            while (entries[l][1] >= entries[pivot][1] && l < r) l+=1

            const tmp = entries[l];
            entries[l] = entries[r];
            entries[r] = tmp;
        }

        const tmp = entries[pivot];
        entries[pivot] = entries[l];
        entries[l] = tmp;

        if (l +1 == k) return entries.slice(0, l+1);
        else if (l + 1 < k) return quickSelection(l+1, right)
        else return quickSelection(left, l-1)
    }

    return quickSelection(0, entries.length-1).map((c) => c[0])
};