# a = 1
# for i in "Python312fdewf43242134fdet54":
#     if i.isdigit():
#         print(i, end=' ')
# for i in range(20, 10, -2):
#     print(i, end=' ')
nums = [1, 2, 'a', 3, 'b', 4]
sums = [nums[0]]
index = 1
# print(nums[1:])
for num in nums[1:]:
    if str(num).isdigit():
        sums.append(sums[index - 1] + num)
    else:
        sums.append(sums[index - 1] * 2)
    index += 1
print(sums)
