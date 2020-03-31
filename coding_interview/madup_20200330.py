import collections

def longest_sum(nums, target):
    queue = collections.deque()
    queue.append((0, len(nums) - 1, sum(nums)))
    source = end = -1
    while queue:
        s, e, su = queue.popleft()
        if su == target:
            source, end = s, e
            break

        if s == e:
            continue
        queue.append((s + 1, e, su - nums[s]))
        queue.append((s, e - 1, su - nums[e]))

    return nums[source:end + 1] if source != -1 else []


nums = [5, 6, -5, 5, 3, 5, 3, -2, 0, 1]
target = 16

print(longest_sum(nums, target))