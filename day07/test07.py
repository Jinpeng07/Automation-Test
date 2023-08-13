# import Util
#
# lambda x, y: x + y
#
# print(Util.my_add(1, 2, 3, 4, 5))
# with open('with.txt', 'w') as f:
#     f.write('with open test2')
#
# f = open('open test.txt', 'w')
# f.write('open test')
#
# def copy_file(old_file_name, new_file_name, ):
#     with open(old_file_name, 'rb') as f:
#         temp = f.read()
#     with open(new_file_name, 'wb') as f:
#         f.write(temp)
#
#
# if __name__ == '__main__':
#     copy_file('文件读写的原理.png', '文件读写的原理2.png')
# import csv
#
# # 写
# with open("1.csv", 'w', encoding='utf8', newline='') as f:
#     # 需要把f转换为csv对象
#     obj = csv.writer(f)
#     obj.writerow(["id", "name", "age"])
#     obj.writerow(["1", "张三", "18"])
#     obj.writerow(["2", "李四", "19"])
#
# # 读
# with open('1.csv', 'r', encoding='utf8') as f:
#     obj = csv.reader(f)
#     for i in obj:
#         print(i)
import xml.etree.ElementTree as ET
from xml.dom.minidom import Document

def write():
    doc = Document()
    root_tag = doc.createElement('root')
    child_tag1 = doc.createElement('child1')
    child_tag2 = doc.createElement('child2')
    child_tag3 = doc.createElement('child3')

    text1 = doc.createTextNode('text1')
    text2 = doc.createTextNode('text2')
    text3 = doc.createTextNode('text3')

    doc.appendChild(root_tag)
    root_tag.appendChild(child_tag1)
    root_tag.appendChild(child_tag2)
    root_tag.appendChild(child_tag3)

    child_tag1.appendChild(text1)
    child_tag2.appendChild(text2)
    child_tag3.appendChild(text3)

    f=open("maker.xml",'w',encoding='utf8')
    f.write(doc.toprettyxml())
    f.close()


write()


def read():
    list = []
    tree = ET.parse('maker.xml')
    root = tree.getroot()
    for e in root.iter():
        if e == root:
            continue
        list.append({e.tag: e.text})
    print(list)
    print(list[0]['child1'])


read()
