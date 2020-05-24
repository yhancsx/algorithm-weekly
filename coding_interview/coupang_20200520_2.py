# Given a set of integer, return if the given integer set could be divided into groups of array, which length is K and the value inside each array need to be consecutive.
# e.g. {5,2,3,4,3,4}, k = 3, return true as it could be divided to [2,3,4],[3,4,5]


# key: num , value: count


# sort 2 3 3 4 4 5
# count duplicate 2 3 4 5 (3: 2, 4: 2)
# 2 3 4
# 3 4 5
#

# input: {5,2,3,4,3,4} -> {5:1, 2:1, 3:2, 4:2}


# O(n + nk+ nlogn)
import collections


def canDivideWithK(nums, k):
    dic = collections.defaultdict(int)

    for num in nums:
        dic[num] += 1

    sorted_nums = list(set(sorted(nums)))

    while sorted_nums:
        num_decreased = []

        previous = sorted_nums[0]
        num_decreased.append(previous)

        for i in range(1, k):
            if sorted_nums[i] > previous + 1:
                return False
            previous = sorted_nums[i]
            num_decreased.append(previous)

        for num in num_decreased:
            dic[num] -= 1
            if dic[num] == 0:
                sorted_nums.remove(num)

    return True


nums = [5, 2, 3, 4, 2, 4]
print(canDivideWithK(nums, 3))

# Product detail page,
# customer views this item also views other items.
# Can you design an algorithm first to get the recommendation candidates?
# Given that we have all the customer viewed history data


# source product -> list recommendation candidates for this source product

# all the data available is the customer view history
# given a product, what are the candidates for this product.

# a: [A, B, C, D]

# b: [A, B, C]

# c: [B, C, E]
# d: [Y, X, Z]


# a-b: 3
# a-d: 0

# A, Z

# A, Z, AZ, 0

# 2^N

# 1B
# 1M
# 1000 Group > N=10



# A: [a,b,c,d]
# B: [a,b,c,d,e]

# session  user1-> {i1, i2, i3} -> {i1, i2}, {i1, ,3}
# user2-> {i1, i2, i3, i4} -> {i1, i2}, {i1, ,3}
#
# {i1, i2} -> 2
# {i1, i4} -> 1

