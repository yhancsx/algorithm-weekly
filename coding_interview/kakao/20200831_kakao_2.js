function segment(x, space) {
    // Write your code here
    let max = -1
    const deque = []
    space.forEach((item,index) => {
        if (deque.length && deque[0] <= index - x)
            deque.splice(0,1)
        while (deque.length>0 && space[deque[deque.length-1]] >= space[index])
            deque.pop();
        deque.push(index)
        if (index < x-1)  return;
        max = Math.max(max, space[deque[0]])
    })
    return max
}