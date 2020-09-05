function requestsServed(timestamp, top) {
    // Write your code here
    timestamp.sort((a,b) => a-b)
    top.sort((a,b)=> a-b)

    let topOfTimestamp  = timestamp.length - 1;
    let topOftop = top.length -1 ;
    let count = 0;

    while(topOfTimestamp >= 0 && topOftop >= 0) {
        while(topOfTimestamp >= 0 && timestamp[topOfTimestamp] > top[topOftop]) {
            timestamp.pop();
            topOfTimestamp --;
        }

        for(let i = 0; i < 5; i ++) {
            if (topOfTimestamp < 0) break;
            timestamp.pop();
            topOfTimestamp --;
            count++;
        }
        topOftop--;
        top.pop()
    }
    return count;
}