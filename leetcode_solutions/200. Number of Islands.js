/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let count = 0;

    if(!grid.length || !grid[0].length) return count;
    const h = grid.length, w = grid[0].length;
    const visits = new Array(grid.length).fill(0).map(() => new Array(grid[0].length).fill(0))

    for(let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (!visits[i][j] && grid[i][j] == "1")  {
              dfs(i, j);
                count+=1
            }
        }
    }

    function dfs(i, j) {

        const mx = [-1,0,1,0];
        const my = [0,1,0,-1];
        visits[i][j] = 1;
        for (let k = 0; k < 4; k++) {
            const nx = i+mx[k], ny = j+my[k];
            if (nx >= 0 && nx < h && ny >= 0 && ny < w && !visits[nx][ny] && grid[nx][ny] =="1")
                dfs(nx, ny)
        }
    }
    return count
};