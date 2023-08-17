# Day1

## 输入输出

```
1.输出:
print输出是默认换行
消除默认换行:print("xxxx",end='')

2.输入:
msg=input("提示信息")
会阻塞,等待输入，得到的数据都是字符串
```

## 占位符

```
%d,整数
%f,浮点
%s

a=int(input("请输入你的数字:"))
print("你输入的数字是:%d"%a)
print("你输入的有小数的是:%0.2f"%a)
print("你输入的信息是:%s"%a)
# 占位符输出多个变量
print("你的用户名是:%s,你的密码是:%s"%(name,password))
```

## help函数

```
1.功能:可以查看别的内置函数的用法
2.使用:help(内置函数的名字)
```

## 变量

```
打印变量存储的地址:print(id(a))

打印变量的类型:type(变量名)
```



# Day2

## 数据类型

```
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）

Number类型:整型和浮点型
注意:
1.如果是除法运算,总是返回一个浮点型
10/2==5.0
2.如果要取整,可以使用//
10//3==3
```

## 数据类型-字符串介绍

```
单引号或双引号包含的都是字符串
Python 没有单独的字符类型，一个字符就是长度为1的字符串
有时候,字符串中需要包含单引号或双引号,这时候怎么办?
单包双,双包单
print("我在学习'python'")
print('我在学习"python"')
```

## 获取字符串中的字符

```
#注意,下标可以是负数,-1表示最后一个字符
```

## 转义

```
反斜杠可以用来转义，使用r可以让反斜杠不发生转义
print(r'我是\n程序员')
#我是\n程序员
```

## 字符串的连接和重复

```
字符串可以用+运算符连接在一起，用*运算符重复

mystr="hello"
mystr2="world"
print(mystr+mystr2)#helloworld
print(mystr*3)#hellohellohello
```

## 字符串不能改变

```
字符串中的字符不能改变,如:mystr="hello"
mystr[0]="k"#报错
```

## 截取字符串(切片)

```
语法:str[起始:结束:步长]  
	说明:
		起始-结束是区间,步长是截取字符串时跳过的字符数量=步长-1
		起始,结束,步长都是可写可不写,选取区间属于**左闭右开(**包头不包尾),结束不包括结束本身
		
#正数(默认),那从左到右，起始默认为0，结束默认为len(str)

#负数,那么就是从右到左，起始默认为len(str)-1，结束默认为-1

#如果要切到数据,那么**切片方向和起始和结束方向一致**

mystr="abcdefg"
print(mystr[0:6:2])#ace

mystr="abcdefg"
print(mystr[2:])#从下标为2的位置切到最后

print(mystr[::-1])#gfedcba
```

## 判断字符串

```
print(a.isdigit())#为纯数字
print(a.isupper())#有大写字母且没有小写字母
print(a.islower())#有小写字母且没有大写字母
print(a.isspace())#为纯空格
print(a.isalpha())#为纯字母
print(a.isalnum())#为字母或数字
```

## 多行字符串

```
使用三引号('''或""")可以指定一个多行字符串

如果多行注释前面有变量来接,那么就变为多行字符串
mystr='''sfsfdsf
dfasfd
sdfasdfa
fdafsf
'''

print(mystr)
```

## 级联字符串

```
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string
print("this" "is" "string")#thisisstring
```

## 字符串的处理

### 获取字符串长度(len)

```
len(str):通过len函数计算字符串的长度 (重点)
```

### 获取子串出现的次数(count)

```
string.count(str, beg= 0,end=len(string)):返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
```

### 替换replace()

```
newstr=string.replace(str1, str2 [, max]):把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次  (重点)
```

### 截取split()

```
string.split(str="", num):以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取num次
```

### 获取子串的位置find()

```
string.find(str, beg=0, end):从字符串中查找子串所在位置, 没找到返回-1 
```

### 索引index()

```
string.index(str, beg=0, end):跟find()方法一样，只不过如果str不在字符串中会报一个异常
```

### 修剪字符串strip()

```
获得字符串修剪左右两侧空格,strip(要删除的字符)  

mystr="     maker      "
print(mystr.strip())#maker
mystr="xxxxxxmakerxxxx"
print(mystr.strip('x'))#maker
```

### 修饰字符串join()

```
返回通过指定字符连接序列中元素后生成的新字符串
seq=':'
mystr=("20",'54','10') 元组
mystr=["20","54","10"] 列表
print(seq.join(mystr))#20:54:10
```

### 检查字符串

```
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He'))  # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))  # True
# 字符串首字母大写
print(str1.capitalize())  # Hello, world!
# 字符串变大写
print(str1.upper())  # HELLO, WORLD!
# 字符串变小写
print(str1.lower())
# 字符串的每个单词首字母大写
print(str1.title()) #Hello,World
```

### 对齐字符串

```
# 将字符串以指定的宽度居中并在，两侧填充指定的字符
print(str1.center(20, '*'))
# 将字符串以指定的宽度靠左放置，左侧填充指定的字符
print(str1.ljust(20, '*'))
# 将字符串以指定的宽度靠右放置，左侧填充指定的字符
print(str1.rjust(20, '*'))
```



# Day3

## 类型转换

```
常用的有:
int(需要转换的数据)
float(需要转换的数据)
str(需要转换的数据)
hex(需要转换的数据) --将一个整型转换为十六进制的字符串
oct(需要转换的数据)--将一个整型转换为八进制的字符串

判断类型是否相同
type和isinstance
isinstance推荐使用,会考虑继承关系
print(type('10'))
print(type(20))
```

## 运算符

### 算术运算符

```
算术运算符:+ - * / % **
1.*,两个数相乘或返回一个被重复多次的字符串
2.**,幂,如a**b,表示返回a的b次方的数
print(3**2)#9
3.//,取相除的整数部分
```

### 比较运算符

```
== 是否相等
!= 是否不相等
> 是否大于
< 是否小于
>= 是否大于等于
<= 是否小于等于
注意:比较返回的真(True),假(False),首字母是大写的
```

### 三目运算符

```
(变量1 if 逻辑 else 变量2)
如果if里为真,返回变量1,否则返回变量2
```

### 赋值运算符

```
= 
+= 
-=
*=
/=
%=
**=
//=
```

### 位运算符

```
位运算符:位运算是运算位,是二进制的位  0000 1010
& 与   有0为0
| 或   有1为1
^ 异或 不同为1

~ 非 1为0,0为1,(~a )
a=10                                  
# 0000 1010                           
# 1111 0101 取反后得到补码                          
# 1000 1010+1  补码把所有的位数取反,然后加1得到原码          
#1000 1011 ==-11                      
print(~a)

<< 左移 高丢低补0 左边为高位,右边为低位
a=10
0000 1010
00 1010
00 101000
print(a<<2)#40

>> 右移 低丢高补0
a=10
0000 1010
0000 10
0000 0010
print(a>>2)#2
```

### 逻辑运算符

```
and 逻辑与 有假为假
or 逻辑或 有真为真
not 逻辑非 真变假,假变真

从右向左运算，如果右边得出结果则不计算左边
```

### 成员运算符

```
成员运算符:某个值是否是某个序列的成员
in:如果值在某个序列中就返回True,反之就返回False
not in:如果值在某个序列中就返回False,反之就返回True
```

### 身份运算符

```
is:判断两个标识符是否引用同一个对象(同一块空间),如果是返回True,反之返回False
is not:判断两个标识符不是引用同一个对象(同一块空间),如果是返回False,反之返回True
```

### 运算符优先级

```
略
```



# Day4

## if~else

```
0表示假,非0表示真,空字符串为假,非空字符串为真
```

## if-elif-else

```
注意：
1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块
3、在Python中没有switch – case语句
```

## while

```
1.格式:
while 条件语句:
	代码块
	
2.while 循环使用 else 语句
while 条件语句:
	代码块
else:
	代码块
注意:当while的代码块中有break跳出循环,那么else中的代码块不会执行
```

## for

```
格式:
for 元素 in 迭代数据类型:
	代码块

解释:迭代数据类型(字符串,列表等)
```

## range()函数

```
格式:
for i in range(开始[,结束,步长]):
	print(i)

类似切片，（开始，结束，步长），左闭右开
#打印1-100,生成的数列是1-100,不包含101
for i in range(1,101):
    print(i)
    
#这里的10表示结束,生成的数列的0-9
for i in range(10):
    print(i)

#生成1,3,5,7,9的数列
for i in range(1,10,2):
    print(i)
    
#生成10,8,6,4的数列
for i in range(10,2,-2):
    print(i)
```

## break,continue

```
break:退出循环,嵌套的循环中一个break只能跳出一个循环
while 1:
    print("外循环")
    while 1:
        print("内循环")
        break#只能跳出一个循环

continue:退出本次循环
```

## for使用else子句

```
类似while，break之后不再执行else子句的代码块
```

## pass

```
Python中pass是空语句，是为了保持程序结构的完整性
pass 不做任何事情，一般用做占位语句
```

## 列表 list

```
1.列表是一种数据类型,也是一个容器,里面可以装数据
2.列表的创建:
格式一:
列表名=[数据1,数据2,数据3,.....]
比如:mylist=[1,2,3,4,5,6] #在创建列表时就定义好了内存空间的大小,后期通过下标不能越位操作
格式二:
列表名=[]  #这种定义方式,定义的列表是没有空间的,不能通过下标来存储数据

注意，
1、list写在方括号之间，元素用逗号隔开
2、和字符串一样，list可以被索引和切片
#切片
print(mylist[0:3])
3、list可以使用 + 操作符进行拼接
4、list中的元素是可以改变的
5.列表中的元素可以是不同的数据类型
```

## 列表的操作

### 追加append()

```
append 追加，在列表的末尾添加新的对象
当空列表要添加数据时,可以使用append来添加数据

print(mylist2)#[200,300]
mylist2.append("hello")
print(mylist2)#[200,300,"hello"]
```

### 添加序列extend()

```
extend(seq)   把一个序列seq的内容添加到列表中

mylist=[1,2]
mylist.extend("hello")
print(mylist)#[1, 2, 'h', 'e', 'l', 'l', 'o']
mylist.extend([10,20,30,40])
print(mylist)#[1, 2, 'h', 'e', 'l', 'l', 'o', 10, 20, 30, 40]

#拆解字符串
mystr="world"
mylist2=[]
mylist2.extend(mystr)
print(mylist2)#['w', 'o', 'r', 'l', 'd']
```

### 插入insert()

```
insert(位置,元素) 在指定的索引处插入一个元素

mylist=[1,2,3,4]
mylist.insert(8,100)#如果位置越位,那么就在最后添加元素

print(mylist)#[1, 2, 3, 4, 100]
mylist.insert(0,200)
print(mylist)#[200, 1, 2, 3, 4, 100]
```

### 移除且返回pop(index)

```
pop(位置) 移除列表中指定索引处的元素，默认移除的是最后一个元素，返回的是被移除的数据
```

### 移除不返回remove(item)

```
remove(元素)  移除指定元素在列表中匹配到的第一个元素【从左往右】
```

### 清空clear()

```
clear()  清除列表中的所有的元素
```

### 获取列表信息

```
获取列表信息
	1、len(列表名) 获取列表的长度
	2、max(列表名) 获取列表中最大的值,只能都是相同类型元素的列表
	3、min(列表名)  获取列表中最小的值,只能都是相同类型元素的列表
	4、index(元素值) 获取指定元素值所对应的索引
	5、count(元素值) 查找指定元素在列表中出现的次数
```

### 排序

```
排序
	1.reverse() 将列表中的元素倒序输出
	2.sort() 排序,默认为升序排序,只能都是相同类型元素的列表
				 降序排序加上reverse = True
	
#案例:将属于list1 = ["a1","a2","a3","a4","a5","a6","a7"]，但不属于list2 = ["a1","a3","a4","a6"]的所有的元素组成一个新的列表list3。
list1 = ["a1","a2","a3","a4","a5","a6","a7"]
list2 = ["a1","a3","a4","a6"]
list3=[]
#第一种方法:
# for i in list1:
#     for j in list2:
#         if i==j:
#             break
#     else:
#         list3.append(i)
#
# print(list3)
#第二种方法:
for i in list1:
    if i not in list2:
        list3.append(i)
        
print(list3)
```

### 随机数

```
1.产生n--m范围内的一个随机数:  random.randint(n,m)

2.产生0到1之间的浮点数:  random.random()

3.产生n---m之间的浮点数:  random.uniform(1.1,5.4)

4.产生从n---m间隔为k的整数: random.randrange(n,m,k)

5.从序列中随机选取一个元素:  random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

6.在一些特殊的情况下可能对序列进行一次打乱操作: random.shuffle([1,3,5,6,7])
```

### 冒泡排序

```
略
```

### 二维列表的创建

```
列表名 = [[值1,值2,...],[值1,值2,...],[值1,值2,...]...]
#列表里面的元素是列表
```



# Day5

## 元组

```
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号()里，元素之间用逗号隔开
元组中的元素类型也可以不相同

1.定义元组
tup1=(1,2,3,'a','b')
tup2=1,2,3

2.只有0个或1个元素时的特殊语法
tup3=()
tup4=(1,)

3.访问元组和访问列表类似(可以切片)
print(tup1[0])
print(tup1[2:4])

4.元组里的元素不能修改,但元素是列表时,可以修改列表里的内容
tu=(1,2,3,[100,200,300])
tu[3][0]=1000
print(tu)#(1, 2, 3, [1000, 200, 300])
tu[3].append(2000)
print(tu)#(1, 2, 3, [1000, 200, 300, 2000])

5.元组的删除(删除元组,不是删除元组里的元素)
del 元组名

6.元组的操作
len,max,min,count,index也适用于元组
tup=(1,2,3,3,3,7,8,2)
print(len(tup))#8
print(max(tup))#8
print(min(tup))#1
print(tup.count(3))#3
print(tup.index(8))#6

列表和元组相互转换
tup=(1,2,3)
mylist=list(tup)
print(mylist)

mylist2=[3,4,5]
tup2=tuple(mylist2)
print(tup2)

7.变量带*
元组同时赋值给多个变量,其中一个变量带星,那么其他不带星的变量获取元组的元素,
其余的给这个带星的变量,这个带星的变量就变为列表
#注意:1,2,3,4,5这连一起是元组
a,*b,c=1,2,3,4,5
print(a)#1
print(b)#[2,3,4]
print(c)#5

元组的特点
1.不可改变(不支持增删改)
2.有序(支持下标查询)

注意
1、与字符串一样，元组的元素不能修改
2、元组也可以被索引和切片，方法一样
3、注意构造包含0或1个元素的元组的特殊语法规则
4、元组也可以使用+操作符进行拼接
tup=('a','b','c')
tup2=(1,2,3)
print(tup+tup2)
```

## 集合

```
集合:
	1.集合（set）是一个无序不重复元素的序列(意思是有重复的会自动删除,每次打印元素的位置不一定)
	2.基本功能是进行成员关系测试和删除重复元素
	3.可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
	4.因为set存储的是无序集合，所以我们没法通过索引来访问。访问 set中的某个元素实际上就是判断一个元素是否在set中。
	
1.创建集合
set1={'a','1',1,'c',66,'d'}
print(set1)
set2=set()#定义空集合

2.删除重复的元素

3.成员关系测试(检测某个成员是否在集合中)
print(88 in set1)

作用:
mylist=[1,2,2,1,3,4,2,1,2,3,3,44,4]
set2=set(mylist)#先把有重复的列表转换为集合
mylist=list(set2)#再把集合转换为列表
print(mylist)#[1, 2, 3, 4, 44]

4.集合常用操作
	1.添加元素
	2.删除元素
	3.删除整个集合
	4.获取集合的长度
	5.不支持改元素
```

### 集合操作-添加元素

```
格式:
集合.add(元素)
# 整体加入，不能加列表，可以加元组
set1=set()#空集合
set1.add(100)
print(set1)#{100}
set1.add((1,2,3)) # 可以加元组
print(set1)#{(1,2,3)}
# set1.add([10,20])#报错
set1.add("hello")
print(set1)#{'hello', 100, (1, 2, 3)}

格式:
集合.update(元素)
# 将字符串，列表，元组拆分后加入set
set1=set()
set1.update("hello")
print(set1)#{'l', 'e', 'o', 'h'}
set1.update([10,20,30])
print(set1)#{'e', 'o', 10, 'h', 20, 30, 'l'}
set1.update((100,200,300))
print(set1)#{'l', 100, 200, 'o', 10, 300, 'e', 20, 'h', 30}

集合可以存储集合
set1={10,20,30}
set2={1,2,3}
# set1.add(set2)#报错
set1.update(set2)
print(set1)#{1, 2, 3, 20, 10, 30}

区别:
add不能添加列表,update可以
update是将字符串中的拆分成字符进行追加
add，是当做整体追加在集合中
```

### 集合操作-删除元素及删除整个集合

```
格式:
集合.remove(元素)  # 元素如果不存在会引发KeyError
集合.discard(元素)  # 元素如果不存在不发生任何事
集合.pop()  # 集合元素是字符串类型时删除随机元素。 集合元素是其他数据类型时，删除左边第一个元素
del 集合名 #删除整个集合

set1={12,1,3,4}
set1.remove(12)
print(set1)#{1, 3, 4}

set1.discard(3)
print(set1)#{1, 4}

set1.pop()
print(set1)#{4}

del set1
print(set1)#报错
```

### 集合操作-获取集合的长度

```
格式:
len(集合名)
set1={1,2,3,4}
pritn(len(set1))#4


#案例:有集合,保留1个元素,其他的删除,假如元素个数不确定
import random
set1=set()
for i in range(20):
    n=random.randint(1,100)
    set1.add(n)

print(set1)

for i in range(len(set1)-1):
    set1.pop()

print(set1)
```

### 集合的集运算(

```
集合的交集,并集,差集,对称差集的运算
{1,2,3,4}交集{4,5,6,7} ->4   交集(&)
{1,2,3,4}并集{4,5,6,7} ->1,2,3,4,5,6,7  并集(|)
{1,2,3,4}差集{4,5,6,7} ->1,2,3  差集(-)
{1,2,3,4}对称差集{4,5,6,7}->1,2,3,5,6,7 4同时出现在两个集合中,不选它 对称差集(^)
```



# Day6

## 字典

### 字典的访问

```
#通过键获取值,未找到key报错

#通过get函数也可以获取键对应的值，未找到返回None

#获取字典中所有的键
print(list(d.keys()))
#获取字典中所有的值
print(list(d.values()))

# print(d[key])#报错
# print(d.get(key))#None
```

### 字典的增删改

```
1.添加:
#通过[]来增加键值对
d={}
d[1]="hello"
print(d)#{1: 'hello'}
d[2]="world"
print(d)#{1: 'hello', 2: 'world'}
#update()方法
vv={3:'aaa',4:'bbbb',5:'ccccc'}
d.update(vv)
print(d)#{1: 'hello', 2: 'world', 3: 'aaa', 4: 'bbbb', 5: 'ccccc'}

2.修改
当字典中有这个键,那么增加就变为修改
d={1:"hello",2:'world'}
d[1]="helloaaaa"
print(d)#{1: 'helloaaaa', 2: 'world'}

3.删除
#注意：删除指定的key，则对应的value也会随着被删除
print(d1.pop(3))	#返回删除的key对应的value
d1.popitem()		#随机返回并删除字典中的一对键和值(一般删除末尾对)
print(d1)
del d1[1]	        #删除元素
#del d1	            #删除字典
#d1.clear()		    #清空字典
```

### 字典的遍历

```
dict1 = {"name":"jbb","sex":"man","age":18}

dict.copy() 返回一个字典的深拷贝
dict.fromkeys(seq, value) 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
dict1.get(key, None) 返回指定键的值，如果值不在字典中返回default值
dict1.keys() 以列表返回一个字典所有的键
dict1.values() 以列表返回字典中的所有值
dict1.items() 以列表返回可遍历的(键, 值) 元组数组
#把字典转换为列表,列表中的元素是元组形式的键值对
print(list(dk.items()))#[(1, 100), (2, 100), (3, 100), (4, 100), (5, 100), (6, 100), (7, 100), (8, 100), (9, 100)]
```

## 数据类型总结

```
数字型
int、float
特点:
1.除法时,总是返回浮点数
2.可以使用//来取整


字符串
1.单引号或双引号包含的都叫字符串
2.单包双,双包单
3.字符串中的字符不能改变

列表
1.列表是用[]包含的数据
2.列表里的元素可以是不同数据类型的
3.可以通过下标来获取或添加数据,但不能越位
4.追加元素(append),添加序列(extend),插入数据(insert),删除(pop,remove),清空(clear),倒序(reverse),排序(sort),长度(len),最大(max),最小(min),获取下标(index),出现次数(count)


元组
1.元组是用()包含的数据
2.元组里的元素可以是不同数据类型的
3.元组里的元素不可以改变
4.定义一个元素的元组:tup(元素,)
5.可以删除元组,但不能删除元组里的元素
6.操作api,长度(len),最大(max),最小(min),获取下标(index),出现次数(count)
7.当元组赋值给若干个变量时,变量的个数没有元组里元素个数多的话,带*的变量,会接收剩下的数据,这时,带*变量就是列表


集合
1.集合是用{}包含的数据
2.集合是个无序且不重复的,不能通过下标来访问
3.作用:清除重复数据,或判断成员
4.操作api:添加(add,update),删除(remove,pop,discard),删除集合(del),长度(len)
5.集运算:交集(&),并集(|),差集(-),对称差集(^)


字典
1.字典是用{}包含的数据,但数据是个键值对
2.字典是个无效的,也就是说不能通过下标来访问
3.访问:字典[键]->值   
4.获取所有键(keys),获取所有值(values)
5.字典的操作:增加([],update),删(pop,popitem,del),清空(clear),删除字典(del),拷贝(copy),
返回列表,元素是元组(items)
```

## 函数的定义

```
1.什么是函数
函数是组织好的,可重复使用的,用来实现单一或相关功能的代码块
2.函数有内建函数和用户自定义函数
3.定义函数的格式:
def 函数名():
	代码块
调用函数:
	函数名()
```

## 参数类型

```
参数类型有,必需参数,关键字参数,默认参数,不定长参数

1.必需参数
形参有多少个,实参必须有多少个
def add(a,b):
    return a+b

# add(10)#报错
add(10,20)

2.关键字参数
使用关键字参数允许函数调用的时候实参的顺序和形参的顺序可以不一致，可以使用关键字进行自动的匹配
def Mymsg(name,age,sex,height):
    print("name=",name)
    print("age=",age)
    print("sex=",sex)
    print("height=",height)
#如果调用时,使用了关键字参数,那么后面的参数都要用关键字参数
Mymsg("maker",sex="男",age=18,height="180cm")

3.默认参数
如果形参有值,那么实参可传可不传,不传,默认使用形参的值,如果传,那么使用实参的值
如果形参有默认值,那么这个形参后面的参数都必须有默认值
def myadd(a,b=20):
    return a+b
print(myadd(20))#40
print(myadd(20,50))#70

4.不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数。
把参数打包成元组给函数调用,如果在函数调用时没有指定参数，它就是一个空元组
def mytest(*arr):
    print(arr)#(1,2,3,4,5)
mytest(1,2,3,4,5)

def mytest02(**arr):
    print(arr)##{'name': 'maker', 'age': 18}
mytest02(name="maker",age=18)
```

## 参数传递方式

```
1.不可变类型：如 整数、字符串、元组。如fun(a)，传递的只是a的值，没有影响a对象本身
2.可变类型：如 列表，字典。如 fun(list)，则是将 list 真正的传过去，修改后fun函数外部的la也会受影响

1.实参传人函数中,实参不会改变
#形参的a和实参的a不是同一个
def mytest(a):#a=10
    a=20

a=10
mytest(a)#mytest(10)
print(a)

2.实参传入函数中,实参会改变
def mytest(mylist):#接收的也是空间地址
    print(id(mylist))
    mylist.append(100)

mylist=[1,2,3]
print(id(mylist))
mytest(mylist)#传递的是空间地址
print(mylist)
```

## return语句

```
作用：表示一个函数执行完毕之后得到的结果返回给调用者
return后面没有什么的语句返回None

return 1,2,3,4#元组
```

## 作用域

```
作用域:就是你定义的变量有效果的范围
变量有全局变量,有局部变量

#在for循环,if语句,while里的定义的是全局变量
for i in range(10):
    b=20
print(b)

if True:
    c=30
print(c)

while c<31:
    d=30
    c+=1
print(d)

当全局变量和局部变量同名时
a=10
def mytest():
    #如果想要在函数内修改全局变量,那么可以使用global来声明
    global a
    a=30
    #如果要使用全局的a,那么可以使用传参
print(a)#10
mytest()
print(a)#30
```



# Day7

## Lambda

```
lambda可以创建小型匿名函数
lambda函数能接收任何数量的参数但只能返回一个表达式的值
格式:
lambda 参数:函数体

注意：
lambda定义的是单行函数，如果需要复杂的函数，应该定义普通函数
lambda参数列表可以包含多个参数，如 lambda x, y: x + y
lambda中的表达式不能含有命令，而且只限一条表达式

作用：
对于单行函数，使用lambda可以省去定义函数的过程，让代码更加精简。
在非多次调用的函数的情况下，lambda表达式即用既得，提高性能
可以做为函数的参数使用(重点)

def func(a,b,f):
    n=f(a,b)
    n+=10
    print(n)

func(20,30,lambda x,y:x+y)
```

## 函数-文档字符串

```
函数的文档字符串是用来说明函数的功能
如:
def add(a,b):
	'''这个函数是用来返回2个数相加的结果'''
	return a+b
print(add.__doc__)
```

## 模块导入(重点)(难点)

```
将整个模块(somemodule)导入，格式为： import 模块名
从某个模块中导入某个函数,格式为： from 模块名 import 函数名
从某个模块中导入多个函数,格式为： from 模块名 import 函数名1, 函数名2, 函数名3
将某个模块中的全部函数导入，格式为： from 模块名 import *
```

## 包

```
包将有联系的模块组织到一起,就是放在同一文件夹下,并在这个文件夹下创建一个__init__.py的文件,这个文件夹就叫包
作用:控制模块的导入

__init__.py内容:
#这里没有写mytest03,也就是说,mytest03不能被别人导入
#from mypage import *模式下,mytest03不能使用
__all__=['mytest01','mytest02']
```

## 文件读写介绍(重点)

```
1.打开文件
2.文件读写
3.关闭文件

格式:
f=open('文件名','打开方式')#打开文件
f.read()或f.write()#文件读写
f.close()#关闭文件
```

## 打开文件(重点)

```
r 只读方式打开文件,从文件开头开始读,默认方式
w 只写方式打开文件,如果文件存在,就覆盖,如果不存在就创建文件
a 打开文件进行追加,写的内容会从原内容的最后开始添加,如果文件不存在,会创建文件
rb 二进制格式只读方式打开文件,从文件开头开始读,读出的是二进制
wb 二进制格式只写方式打开文件,如果文件存在,就覆盖,如果不存在就创建文件
ab 二进制格式打开文件进行追加,写的内容会从原内容的最后开始添加,如果文件不存在,会创建文件
r+ 读写模式打开文件,从文件开头开始读写
w+ 读写模式打开文件,从文件开头开始读写,如果文件存在,就覆盖,如果不存在就创建文件
a+ 读写模式打开文件,从原文件的尾部开始,如果文件存在,就覆盖,如果不存在就创建文件
rb+ 二进制格式读写模式打开文件,从文件开头开始读写
wb+ 二进制格式读写模式打开文件,从文件开头开始读写,如果文件存在,就覆盖,如果不存在就创建文件
ab+ 二进制格式读写模式打开文件,从原文件的尾部开始,如果文件存在,就覆盖,如果不存在就创建文件
```

## 写文件(重点)

```
说明:
write("字符串")
writelines(字符串序列)
f.writelines(["world","hello","nihao"])

格式一:
#打开文件
f=open("1.txt",'w')
#写文件
f.write("hello")
#关闭
f.close()

格式二:
with open("2.txt",'w') as f:
    f.write("nihao")
    #当离开with模块时,文件会自动关闭

#中文乱码问题 encoding='utf8'
with open('file/3.txt','w',encoding='utf8') as f2:
    f2.write('中文')
    f2.close()
```

## 读文件(重点)

```
注意:如果读的数据有中文,也要加encoding='utf8'
格式一:
# mystr=f.read()#读所有行,返回的是字符串
# mystr=f.readline()#读首行,返回的是字符串
# mystr=f.readlines()#读所有行,返回的是列表,元素有\n
mystr=f.read().splitlines()#读所有行,返回的是列表,不带\n
```

## 读写图片,音频,视频(重点)

```
读写图片,音频,视频要用二进制方式打开文件

#案例,请设计一个通用的,可以复制后缀为.jpg,.png,.mp3,.mp4格式的函数
# def copy_file(old_file_name, new_file_name, ):
#     with open(old_file_name, 'rb') as f:
#         temp = f.read()
#     with open(new_file_name, 'wb') as f:
#         f.write(temp)
#
#
# if __name__ == '__main__':
#     copy_file('with.txt', 'with2.txt')
```

## CSV文件读写(重点)

```
#引入csv模块
import csv
#写
with open("1.csv",'w',encoding='utf8',newline='') as f:
    #####需要把f转换为csv对象#####
    obj=csv.writer(f)
    obj.writerow(["id","name","age"])
    obj.writerow(["1","张三","18"])
    obj.writerow(["2","李四","19"])
    
#读
with open('1.csv','r',encoding='utf8') as f:
    obj=csv.reader(f)
    for i in obj:
        print(i)
```

## XML文件读写

```
XML：可扩展标记语言，标准通用标记语言的子集，是一种用于标记电子文件使其具有结构性的标记语言
要引入import xml.etree.ElementTree as ET

if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。

import xml.etree.ElementTree as ET
from xml.dom.minidom import Document
def WriteXml():
    #生成一个xml对象
    doc=Document()
    #生成标签队,并把标签队添加到doc对象中
    peo=doc.createElement('dict')
    doc.appendChild(peo)

    #生成标签队key,放到dict标签对内
    mykey=doc.createElement('key')
    peo.appendChild(mykey)

    # 生成内容,并把内容添加到key标签队之间
    mytext=doc.createTextNode('string1')
    mykey.appendChild(mytext)

    # 生成标签队string,放到dict标签对内
    mystring = doc.createElement('string')
    peo.appendChild(mystring)

    # 生成内容,并把内容添加到key标签队之间
    mytext2 = doc.createTextNode('Maker')
    mystring.appendChild(mytext2)


    f=open("maker.xml",'w',encoding='utf8')
    f.write(doc.toprettyxml(indent=''))
    f.close()


WriteXml()

def ReadXml():
    mylist=[]
    #打开xml文件,tree代码整个文件
    tree=ET.parse('maker.xml')
    #获取根节点
    root=tree.getroot()
    ## 遍历所有节点，包括root
    ## for e in root.iter():
    for i in root.iter('string'):#遍历string节点
        #获取节点之间的内容,并存储到列表
        mylist.append(i.text)

    print(mylist)

ReadXml()
```



# Day08

## xls格式文件写

```
1.使用xlwt模块,下载pip install xlwt
2.步骤:
workbook=xlwt.Workbook(encoding='utf8')#创建文件对象
worksheet=workbook.add_sheet("页面名字")
worksheet.write(0,0,label="hello")#0,0表示单元格的坐标,表示最左上角的单元格
workbook.save("文件名.xls")
```

## xls格式文件读

```
import xlrd
def funcRxls():
    #打开xls文件
    f=xlrd.open_workbook("1.xls")
    #获取页面对象
    sheet=f.sheets()[0]
    for i in range(0,sheet.nrows):
        rows=sheet.row_values(i)#获取这行内容,以列表形式返回
        print(rows)
```

## xlsx格式文件写(重点)

```
1.需要下载:pip install openpyxl
注意:openpyxl只能操作xlsx格式的文件,不能操作xls格式文件

一.简单写
from openpyxl import Workbook
def mytest01():
    #创建工作表对象
    wb=Workbook()
    #获取默认的页面
    mysheet=wb.active
    mysheet['C1']=666
    wb.save("1.xlsx")

二,添加页面
def mytest01():
    #创建工作表对象
    wb=Workbook()
    #获取默认的页面
    mysheet=wb.active
    mysheet['C1']=666
    #创建页面,追加方式
    wb.create_sheet("mysheet")
    #创建页面并指定位置
    wb.create_sheet("mysheet2",0)
    wb.save("1.xlsx")

三.页面操作
def mytest01():
    wb=Workbook()
    wb.create_sheet('mysheet')
    print(wb.sheetnames)
    #通过页面名获取页面
    # st=wb["mysheet"]
    st=wb.get_sheet_by_name("mysheet")
    st['B1']=1111
    print(st.max_row)#最大的行
    print(st.max_column)#最大的列
    wb.remove(st)#删除页面
    wb.save("1.xlsx")

四.单元格操作
def mytest01():
    wb=Workbook()
    wb.create_sheet('mysheet')
    print(wb.sheetnames)
    #通过页面名获取页面
    # st=wb["mysheet"]
    st=wb.get_sheet_by_name("mysheet")
    st['B1']=1111
    #通过行和列数添加内容到单元格
    st.cell(1,2,"hello")
    #写入多个单元格,追加形式,一行中多个单元格
    st.append([4,5,6])
    st.append([10, 20, 30])
    #写公式
    st['A4']="=sum(A2:A3)"
    wb.save("1.xlsx")
```

## xlsx格式文件读(重点)

```
xlsx读还是openpyxl模块,但要引入这个模块的load_workbook

#打开文件
wb=load_workbook('1.xlsx')
#获取表格中所有的页面名
mylist=wb.sheetnames
print(mylist)
#获取页表
wh=wb[mylist[1]]
#获取单元格的内容
print(wh['B1'].value)
print(wh.cell(1,2).value)
#遍历页面中所有的内容
for row in wh.rows:
    for i in row:
        print(i.value)
```

## Json介绍

```
略
```

## JSON 数据的写入(重点)

```
json.dump	dict数据写入json文件中
json.dumps	dict转换为字符串

#字典
data={"id:":"33445566",'姓名:':"maker","地址:":"深圳"}
with open("data.json",'w',encoding='utf8') as f:
    json.dump(data,f,ensure_ascii=False,indent=4)
    
#把字典转换为字符串
mystr=json.dumps(data,ensure_ascii=False,indent=4)
print(mystr)
print(type(mystr))
```

## JSON 数据的读取(重点)

```
json.load	打开json文件，并把json字符串转换为python的dict数据
json.loads	将json字符串转换为字典

import json
with open("data.json","r",encoding='utf8') as f:
    d=json.load(f)

print(d)
print(type(d))

#注意,这里要单包双,不能双包单
mystr='{"ID":1,"name":"maker"}'
d2=json.loads(mystr)
print(d2)
print(type(d2))
```

## Json与类对象(后期讲完面向对象后讲)

```
略
```

## Yaml文件格式介绍(重点)

```
yaml是一种类似于xml以及json这种键值对类型的文件，不过它的数据展示更加直观，更容易被识别和解析出来。而它和python这种脚本特征的语言具有很强的交互性
Yaml格式文件通常用来编写项目配置，也可用于数据存储

YAML 语法
支持的数据类型：字典、列表、字符串、布尔值、整数、浮点数、Null、时间等
基本语法规则：

1、大小写敏感

2、使用缩进表示层级关系

3、相同层级的元素左侧对齐

4、键值对用冒号 “:” 结构表示，冒号与值之间需用空格分隔

5、数组前加有 “-” 符号，符号与值之间需用空格分隔

6、None值可用null 和 ~ 表示

7、多组数据之间使用3横杠---分割

8、# 表示注释，但不能在一段代码的行末尾加 #注释，否则会报错

9.不要使用tab键作为缩进，有时可能出错

python没有自带的处理yaml文件的库，需要下载第三方库PyYAML
pip install pyyaml
```

## Yaml文件写(重点)

```
单组数据写入使用yaml.dump()方法，加入allow_unicode=True参数防止写入的中文乱码
多组数据写入使用yaml.dump_all()方法

单组
import yaml
mydata={
    "id": 1,
    "地区": "深圳",
    "data": [{
        "id": 1,
        "名字": "南山区"
        },
        {
         "id": 2,
        "名字": "福田区"
        },
        {
        "id": 3,
        "名字": "光明区"
        }]
}
with open("1.yaml",'w',encoding='utf8') as f:
    yaml.dump(data=mydata,stream=f,allow_unicode=True)

多组
import yaml
mydata={
    "id": 1,
    "地区": "深圳",
    "data": [{
        "id": 1,
        "名字": "南山区"
        },
        {
         "id": 2,
        "名字": "福田区"
        },
        {
        "id": 3,
        "名字": "光明区"
        }]
}

mydata2={
    "id": 2,
    "地区": "深圳",
    "data": [{
        "id": 1,
        "名字": "南山区"
        },
        {
         "id": 2,
        "名字": "福田区"
        },
        {
        "id": 3,
        "名字": "光明区"
        }]
}
with open("1.yaml",'w',encoding='utf8') as f:
    yaml.dump_all(documents=[mydata,mydata2],stream=f,allow_unicode=True)
```

## Yaml文件读(重点)

```
读取数据使用load函数
读取多组数据使用，yaml.load_all()方法，返回结果为一个生成器，需要使用for循环语句获取每组数据

result = yaml.load(f.read(), Loader=yaml.FullLoader)
Loader=yaml.FullLoader参数不写的话对结果不会有影响，但运行时会出现警告信息。

#单组
import yaml

with open("1.yaml",'r',encoding='utf8') as f:
    res=yaml.load(f.read(),Loader=yaml.FullLoader)

print(res)
print(type(res))

#多组
import yaml

with open("1.yaml",'r',encoding='utf8') as f:
    res=yaml.load_all(f.read(),Loader=yaml.FullLoader)
    print(res)
    for i in res:
        print(i)
```



# Day09

## 面向对象

```
略


名称说明:
类中定义的变量:类属性
对象自身定义的变量:对象属性
成员变量包含类变量和实例变量
全局变量和局部变量是相对于作用域来说的.
```

## self介绍(重点,难点)

```
self,是对象本身
```

## 构造函数(重点,难点)

```
1.构造函数是给对象的实例变量赋初始值
2.当一个对象被创建的时候，第一个被自动调用的函数
3.语法:
__init__(参数列表):
	函数体
4.构造函数的参数在定义对象时传递,如:m=Maker(实参) ->实参传递到__init__(形参)
5.如果没有显示定义构造函数,那么系统默认提供一个无参的构造函数,这个无参的构造函数是空函数体
手动添加了有参的构造函数之后，系统将不再提供无参的构造函数
```

## 析构函数

```
1.当删除一个对象时,python解释器也会调用一个函数,做清理工作,这个函数就叫析构函数
2.格式:
  __del__(self):
3.time模块中的sleep(时间)可以暂停代码运行
4.删除对象用del
5.当1个变量保存了对象的引用,此时对象引用计数器就加1,
  当使用del删除变量指向的对象时,引用计数器就减1,当减到0时,就调用析构函数
6.作用:通常是销毁/删除临时的变量，主要对那些长期占用内存的临时变量进行销毁.有些程序是不结束的或运行很久的
```



# Day10

## 魔法方法(了解)

```
魔法方法:很魔幻
格式:__xxxx__(self)
__add__ 加法(两个对象相加时调用)
__lt__  小于(两个对象比较时调用)
__str__ 字符串(打印对象时调用)

class Maker():
    def __add__(self,other):#self=m,other=m2
        print(self.age)
        print(other.kk)
        print("当2个对象相加时,我会被调用")
        return self.age+other.kk

m=Maker()
m.age=20
m2=Maker()
m2.kk=30
print(m+m2)#两个对象相加
```

## 面向对象的三大特征介绍

```
略
```

## 封装(重点)

```
1.封装的概念:把属性和方法封装在一起,并赋予权限
2.作用:保证内部的高内聚性和与外部的低耦合性
3.私有成员:
	1.外部不能直接访问,内部可以直接访问
	2.在属性或方法名前面加2个下划线就表示该成员是私有的
	
class Maker():
    __age=10,#私有类属性

    def getAge(self):
        return self.__age

    def setAge(self,age):
        #判断修改的年龄是否合法
        if age>=1 and age<=140:
            self.__age=age

m=Maker()
# print(m.age)#当类属性为私有时,类外面不能直接操作类属性
# m.age=1000
print(m.getAge())
m.setAge(30)
print(m.getAge())
```

## 继承介绍(重点)

```
1.类与类之间才能继承
2.作用:简化代码,代码复用
3.名词解释:父类(基类,超类),子类(派生类)
4.子类的小括号中写了哪个类,就表示继承了谁(认谁做爹了)
5.子类拥有父类的所有属性和方法(私有的除外)
6.继承有单继承和多继承
7.object是所有类的父类，如果一个类没有显式指明它的父类，则默认为object
```

## 单继承(重点)

```
单继承,就是子类继承一个父类(儿子只有一个爹)，不能继承父类私有成员

#父类
class Father():
    m="1千万",
    __mytype="小三",

    def mytest01(self):
        print("有钱")

    def mytest02(self):
        print("有房")

    def mytest03(self):
        print("有颜值")

#子类
class Son(Father):
    def myfunc(self):
        print(self.m)
        # print(self.__mytype)#报错,不能继承父类私有成员

s=Son()
s.mytest01()
s.mytest02()
s.mytest03()
print(s.m)
# print(s.__type)
s.myfunc()
```

## 多继承

```
多继承,就是子类有多个父类(儿子有多个爹)
继承规则：Python允许多继承。调用顺序：从左到右，先深度再广度
不建议使用多继承,多继承会增加代码的复杂性
```

## 继承构造函数和析构函数问题(重点)

```
1.子类不写构造函数,那么会默认调用从父类继承过来的构造函数
2.如果重写了__init__ 时，要继承父类的构造方法，可以在子类构造函数中使用 super 关键字或父类名
3.析构和构造一样

class Father():
    def __init__(self,name):
        print("我是Father的构造函数")


class Son(Father):
    def __init__(self):
        # # super(Son,self).__init__("kk")#调用从父类继承的构造函数
        # Father.__init__(self,"kk")#调用从父类继承的构造函数
        print("我是Son的构造函数")


s=Son()
#注意,当子类没有写自己的构造函数,那么就要调用从父类继承过来的构造函数,要注意父类的构造函数是否有参数
```

## 子类调用父类同名方法

```
1.当子类的函数和父类的函数同名时,在子类的同名函数中使用super()关键字

class Father():
    def mytest(self):
        print("Father")

class Son(Father):
    def mytest(self):
        super().mytest()#调用父类的mytest函数
        print("Son")

s=Son()
#当父类和子类有同名函数时,子类对象,先调用自己的函数
s.mytest()
```

## 重写

```
简单，略
```

## 多态(重点)

```
简单，略
继承+重写方法
```

## 错误和异常

```
错误：通常是指代码中的语法错误，一般初级程序员很常见或者说很容易犯。
异常:即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期间检测到的错误被称为异常
pycharm中错误常有箭头指示出来,异常没有
```

## 异常的捕获

```
1.捕获异常的格式:
try:
    print(1 / 0)
except Exception as e:
    print(e)
else
说明:Exception常规错误的基类,把异常的基本信息存储到e中

2.异常处理-except分支else:没有异常执行else下面的代码

3.finally语句:有没有异常都要执行这下面的代码
def mytest(a,b):
    return a/b

try:
    mytest(10,0)
except Exception as e:
    print(e)
    # raise #抛出异常给上一级，不处理
else:
    print("没有异常就执行这")
finally:
    print("有没有异常都要执行这里的代码")

4.抛出异常:
	1.raise关键字

5.异常要处理,不管是谁
def mytest(a,b):
    return a/b
def myfunc():
    try:
        mytest(10,0)
    except Exception as e:
        # print(e)
        raise #抛出异常
    else:
        print("没有异常就执行这")
    finally:
        print("有没有异常都要执行这里的代码")

#这里处理myfunc函数抛出的异常
try:
    myfunc()
except Exception as ee:
    print(ee)

6.自定义异常:
要继承Exception常规错误的基类
class ShowInputOut(Exception):
    def __init__(self,len,flag):
        super().__init__()
        self.len=len
        self.flag=flag
        
def main():
    try:
        s=input("请输入-->")
        if len(s)<3:
            raise ShowInputOut(len(s),3)
    except ShowInputOut as e:
        print("你输入长度为%d,长度必须大于%d"%(e.len,e.flag))
    else:
        print("没有发生异常")

main()
```

## OS模块(重点)

```
from sys import argv,path  #  导入特定的成员
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


import os

path = os.getcwd() # 获取当前执行文件的绝对路径,文件夹的路径
path = os.path.abspath('.') # 获取当前执行文件的绝对路径,文件夹的路径, 同上
path = os.path.abspath('..') # 获取当前文件夹的父文件夹路径
path = os.path.abspath('test10.py') # 获取当前文件的路径
path = os.path.abspath(__file__) # 获取当前文件的路径, 同上

#获取当前路径下所有文件名
mylist=os.listdir(os.getcwd())
print(mylist)
#修改文件名
os.rename(os.getcwd()+'/1.txt',os.getcwd()+'/2.txt')

案例:批量修改文件名
import os
funFlag = 1 # 1表示添加标志,2表示删除标志
folderName = './renameDir/'
#获取指定路径下所有文件的名字
dirList = os.listdir(folderName)
#遍历输出所有文件的名字
for name in dirList:
	print(name)
	if funFlag==1:
		newName='[山哥出品]-'+name
	elif funFlag==2:
		num=len('[山哥出品]-')
		newName=name[num:]
	print(newName)
	os.rename(folderName+name,folderName+newName)
```



# Day11

## python连接数据库

```
1.python连接mysql数据库需要下载pymysql模块
2.步骤:
	1.连接数据库
	2.创建游标对象
	3.通过游标对象操作数据库
	4.关闭数据库
	
db=pymysql.connect(host='127.0.0.1',port=3306,user="root",passwd='123456',db="mysql",charset='utf8')

#查看数据库系统的版本
cur.execute('select version()')
#获取查询的结果
data=cur.fetchall()
print("数据库系统的版本为:",data)#数据库系统的版本为: (('5.6.25-log',),)

#创建数据库
cur.execute('drop database if exists mytestcn')#如果有这个名字的数据库就删除
cur.execute('create database mytestcn')#创建数据库

#查看所在的数据库名字
cur.execute("select database()")
#获取查询的结果
data=cur.fetchall()
print("所在的数据库名字为:",data)#所在的数据库名字为: (('mysql',),)

#切换数据库,切换到mytestcn数据库中
cur.execute('use mytestcn')

#查看所在的数据库名字
cur.execute("select database()")
#获取查询的结果
data=cur.fetchall()
print("所在的数据库名字为:",data)#所在的数据库名字为: (('mytestcn',),)

#创建表格
#表格要存储(用户名,密码,手机号码,邮箱)
#创建表格的sql语句
sql="create table usertable(" \
    "name varchar(20),passwd varchar(20)," \
    "iph varchar(20),email varchar(20))"

cur.execute(sql)

#往表格添加数据(增)
sql="insert into usertable values('李四','123456','13833445566','2342423@qq.com')"
cur.execute(sql)
db.commit()

#改表格中的数据(改)
sql="update usertable set iph='138888888' where name='李四'"
cur.execute(sql)
db.commit()

#查看表格的内容
sql="select * from usertable"
cur.execute(sql)
data=cur.fetchall()
print(data)

#删除数据库(删)
sql="delete from usertable where name='李四'"
cur.execute(sql)
db.commit()

#关闭数据库
db.close()
```

## 迭代器的介绍

```
一、什么是迭代器
迭代是python中访问集合元素的一种非常强大的一种方式。迭代器是一个可以记住遍历位置的对象，因此不会像列表那样一次性全部生成，而是可以等到用的时候才生成，因此节省了大量的内存资源。迭代器对象从集合中的第一个元素开始访问，直到所有的元素被访问完。迭代器有两个方法：iter（）和next（）方法。

二、可迭代的对象
类似于list、tuple、str 等类型的数据可以使用for …… in…… 的循环遍历语法从其中依次拿到数据并进行使用，我们把这个过程称为遍历，也称迭代。python中可迭代的对象有list（列表）、tuple（元组）、dirt（字典）、str（字符串）等。

从字面来理解，迭代器指的就是支持迭代的容器，更确切的说，是支持迭代的容器类对象，这里的容器可以是列表、元组等这些 Python 提供的基础容器，也可以是自定义的容器类对象，只要该容器支持迭代即可。

三.Python 迭代器的好处
使用迭代器的好处是可以节省资源。
代码减少。
代码冗余得到极大解决。
降低代码复杂度。
它为编码带来了更多的稳定性。

一、迭代器：
#任何实现了__iter__()和__next__()方法的对象都是迭代器。
其中，__iter__返回迭代器自身，__next__返回容器中的下一个元素值。

二、生成器：
具有yield关键字的函数都是生成器。
yield可以理解为特殊的return，该函数不会释放局部变量。
生成器自动实现了__iter__()和__next()__()方法，也就是说生成器也是迭代器。
调用生成器函数，将返回生成器对象，该生成器对象具有迭代器的所有功能。
```

## 生成迭代器-方法1

```
1.iter（可迭代数据类型）:生成一个迭代器对象
2.next（）:返回迭代器中的数据, 并且移动到下一个迭代

#生成迭代器对象
obj_iter=iter([1,2,3,4,5,6,7,8,9])
print(next(obj_iter))

#next获取不到数据时,会报StopIteration异常
# for i in range(10):
#     print(next(obj_iter))
```

## 生成迭代器-方法2

```
1.使用函数,在函数中使用循环,结合yield函数,yield可以理解为特殊的return，该函数不会释放局部变量
2.yield函数就是在循环中,把数据放到一个迭代对象中,只不过是被调用了才放入

# def mytest():
#     for i in range(10):
#         yield i #相当于返回i且把i保存到迭代器对象中
#
# #生成迭代对象
# res=mytest()
#
# print(next(res))
# print(next(res))


#生成迭代对象
res=(i for i in [1,2,3,4])

print(next(res))
print(next(res))
for i in res:
    print(i)
#一共输出1234， 因为前面已经迭代过2次了
```

## 自定义迭代器对象

```
class MyNumbersIterator:
    def __iter__(self):
        self.a = 1
        return self  # 返回迭代器自身
 
    def __next__(self):
        x = self.a
        self.a += 1
        return x
 
 
myclass = MyNumbersIterator()
myiter = iter(myclass)  # 通过调用myclass.__iter__()返回迭代器。

 
print(next(myiter))  # 输出 1
print(next(myiter))  # 输出 2
print(next(myiter))  # 输出 3
print(next(myiter))  # 输出 4
print(next(myiter))  # 输出 5
```

## 自定义生成器

```
import sys
 
def fibonacci(n):  # 生成器函数 - 斐波那契，返回n个斐波那契数
    a, b, counter = 0, 1, 1
    while counter <= n:  # 生成n个
        yield a #保存a到迭代器对象，往后继续执行代码
        a, b = b, a + b  # 返回一个斐波那契数，更新a,b，然后循环计算后面一个
        counter += 1
 
 
f = fibonacci(10)  # f 是一个生成器对象，但它同时具有迭代器的所有功能，因为其自动实现了迭代器协议
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
```







