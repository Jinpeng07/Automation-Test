# def remove_all(mylist, item):
#     i = 0
#     index = 0
#     length = len(mylist)
#     while i < length:
#         if mylist[index] == item:
#             mylist.remove(item)
#         else:
#             index += 1
#         i += 1
#
#
# if __name__ == '__main__':
#     mylist = [1, 1, 1, 2, 1]
#     remove_all(mylist, 1)
#     print(mylist)
# mylist = [1, 2, 3, 4, 5]
# ml2 = mylist[::-1]
# print(ml2)
# import random
#
# print(random.randrange(1, 20, 2))
# mylist = [1, 2, 3, 4, 5]
# random.shuffle(mylist)
# print(mylist)

# mylist = [3, 421, 4, 54, 23, 3]
# for i in range(len(mylist)):
#     for j in range(len(mylist) - 1 - i):
#         if mylist[j] < mylist[j + 1]:
#             mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
# print(mylist)
#
# list2 = [1, 2, 3, [1, 2, 34, 4]]
# tup = tuple(list2)
# print(tup)
# tup[3][0] = 100
# print(tup)
import random
set1=set()
for i in range(20):
    n=random.randint(1,100)
    set1.add(n)

print(set1)

for i in range(len(set1)-1):
    set1.pop()

print(set1)