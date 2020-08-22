/**
 * @param {string[]} logs
 * @return {string[]}
 */

var reorderLogFiles = function(logs) {
    const digs = [], letters = []
    logs.forEach((log)=>{
        if (!isNaN(log.split(' ')[1]))
            digs.push(log)
        else
            letters.push(log)
    })
    function sortAl(a,b)  {
        const aa = a.split(' ').slice(1).join(' '), bb =b.split(' ').slice(1).join(' ')
        if (aa === bb) return (a.split(' ')[0] <= b.split(' ')[0])?-1:1
        const r = aa <= bb
        if (r) return -1
        else return 1
    }

    letters.sort(sortAl)
    return letters.concat(digs)
};