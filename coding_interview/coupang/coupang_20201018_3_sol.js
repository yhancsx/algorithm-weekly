function extractInt(num) {
    if(num == 100) return [1,0,0];
    if(num > 9) {
        return [Math.floor(num / 10) , num % 10]
    }
    return [num]
}
function distribute2NumbersToBeFair(num1, num2) {
    const sum = num1 + num2;
    const avg = sum/2
    return [Math.floor(avg), Math.ceil(avg)]
}
function solution(ages){
    const intCounts = new Array(10).fill(0);

    ages.forEach(age=>{
        const ints = extractInt(age);
        ints.forEach(int => intCounts[int] +=1)
    })
    const [count6, count9] = distribute2NumbersToBeFair(intCounts[6], intCounts[9])
    intCounts[6] = count6;
    intCounts[9] = count9;

    return Math.max(...intCounts)
}