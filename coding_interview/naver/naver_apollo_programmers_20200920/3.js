function solution(play_list, listen_time) {
  let max = 0;
  const num_play_list = play_list.length;
  const play_list_end_times = play_list.map((sum => value => sum += value)(0));
  const end_time_of_play_list = play_list_end_times[num_play_list - 1];

  if (listen_time >= end_time_of_play_list) return num_play_list;

  function findItemIndexByTime(end_time, left = 0) {
    let right = num_play_list - 1;
    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (play_list_end_times[mid] === end_time) return mid;
      if (play_list_end_times[mid] > end_time) right = mid;
      else left = mid + 1;
    }
    return left;
  }

  play_list_end_times.forEach((item_end_time, index) => {
    let num_play_item = 0;
    let start_time = item_end_time - 1;
    let end_time = start_time + listen_time;

    if (end_time > end_time_of_play_list) {
      num_play_item += num_play_list - index;
      end_time = listen_time - (end_time_of_play_list - start_time);
      start_time = 0;

      // start index === end index
      const end_index = findItemIndexByTime(end_time);
      if (end_index === index) num_play_item -= 1;
      const start_index = start_time === 0 ? 0 : index;
      num_play_item += end_index - start_index + 1;
    } else {
      const start_index = start_time === 0 ? 0 : index;
      const end_index = findItemIndexByTime(end_time, start_index);
      num_play_item += end_index - start_index + 1;
    }

    max = Math.max(num_play_item, max);
  });
  return max;
}
console.log(solution([2,3,1,4],1))
// console.log(solution([1,2,3,4],5))
// console.log(solution([1,2,3,4], 20))
// console.log(solution([2,3,2,3],1))