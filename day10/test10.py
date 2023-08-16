# class MyException(Exception):
#     message = '自定义异常'
#
#
# def main():
#     try:
#         n = int(input('请输入: '))
#         if n == 0:
#             raise MyException()
#     except MyException as me:
#         print(me.message)
#     else:
#         print('else')
#     finally:
#         print('finally')
import os

# #获取当前路径下所有文件名
# mylist=os.listdir(os.getcwd())
# print(mylist)
# #修改文件名
# os.rename(os.getcwd()+'/1.txt',os.getcwd()+'/2.txt')
funFlag = 2  # 1表示添加标志,2表示删除标志
folderName = os.getcwd()
# 获取指定路径下所有文件的名字
dirList = os.listdir(folderName)
# 遍历输出所有文件的名字
for name in dirList:
    print(name)
    if funFlag == 1:
        newName = 'test' + name
    elif funFlag == 2:
        num = len('test')
        newName = name[num:]
    print(newName)
    os.rename(folderName + os.sep + name, folderName + os.sep + newName)
