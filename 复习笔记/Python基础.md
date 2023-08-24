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
2.如果重写了__init__ 时，就要继承父类的构造方法，可以在子类构造函数中使用 super 关键字或父类名
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

## python的迭代对象和迭代器

```
可迭代对象和迭代器和区别：迭代器和可迭代对象不是同个概念，区别在于是否有next函数

1.可以直接使用for循环遍历的数据类型就是迭代对象

#判断该数据类型是否为迭代对象
from collections import Iterable

print(isinstance("hello",Iterable))

2.迭代器,可以被next函数调用,并返回下一个值的对象称为迭代器(iterator)，生成器也是迭代器
#判断该数据类型是否是迭代器
from collections import Iterator
print(isinstance("hello",Iterator))#False

print(isinstance((x for x in range(6)),Iterator))#True

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

# Day12

## for ... in ... 遍历的原理      

```
1.内部调用iter函数,将要遍历的迭代器对象作为参数传入
2.等价调用了__iter__()函数生成迭代器
3.然后使用next函数去执行迭代器
'''
# print(mystr.__iter__())
# print(iter(mystr))
it=iter(mystr)
print(next(it))
```

## 生成器介绍

```
生成器本质上也是迭代器，不过它比较特殊。
以 list 容器为例，在使用该容器迭代一组数据时，必须事先将所有数据存储到容器中，才能开始迭代；而生成器却不同，它可以实现在迭代的同时生成元素。
也就是说，对于可以用某种算法推算得到的多个数据，生成器并不会一次性生成它们，而是什么时候需要，才什么时候生成。

不仅如此，生成器的创建方式也比迭代器简单很多，大体分为以下 2 步：
定义一个以 yield 关键字标识返回值的函数；
调用刚刚创建的函数，即可创建一个生成器。
```

## 生成器  

```
def mytest(n):
    i=0
    while i<n:
        yield i
        i+=1
#创建生成器
it=mytest(5)
#mytest函数返回时使用yield,而不是return,所以这类函数又叫生成器函数

也可以使用for循环遍历生成器函数
for i in it:
	print(i)
```

## 写成类方式来实现生成器

```
def myrange(n):
    index=0
    while index<n:
        yield index
        index+=1


class Maker():
    def __init__(self,n):
        self.n=n
        
    def __iter__(self):
        return myrange(self.n)

m=Maker(20)
for i in m:
    print(i)
```

## 生成器推导式  

```
class Maker():
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return (i for i in range(self.n))


m = Maker(20)
for i in m:
    print(i)
```

## 进阶使用

```
略，看不懂
```

## 装饰器介绍

```
@装饰器名称
作用： 给被装饰的对象增加额外的属性或者功能   

原理：  
1. 装饰器本质上是一个函数(可调用对象) 
2. 这个函数的参数是一个函数对象(被装饰的函数)    
3. 这个函数的返回值是一个新的函数对象（基于被装饰的函数添加了额外属性或者功能的函数）

原始语法：
@decorator
def function():
	pass

原始语法：    function = decorator(function) 原函数指向被装饰的新函数
```

##  装饰器的基本用法 

```
def Okmyfunc(myfunc):
    def OKK():
        myfunc()
        #增加额外的功能
        print("银行存款10位数")
        print("飞机,轮船多艘")
        print("知心朋友超多")
    return OKK


@Okmyfunc   #myfunc=Okmyfunc(myfunc)
def myfunc():
    print("月薪1万左右")
    print("无房子")
    print("无车")
    print("无对象")

myfunc()
```

## 案例： 统计函数的执行时间  

```
def collect_time(func):
    def total_time():
        begin = time.time()
        func()
        end = time.time()
        return end - begin
    return total_time


@collect_time
def itertest(): itertest = collect_time(itertest)
    time.sleep(2)


print(itertest())
```

## 被装饰的函数有返回值

```
同上
```

## 被装饰的函数存在参数，并且参数的个数不同   

```
import time

def funcMaker(func):
    def start_maker(*args,**kwargs):
        ret=func(*args,**kwargs)
        return ret+100
    return start_maker

@funcMaker
def myfunc1(a,b):
    time.sleep(2)
    return a+b

print(myfunc1(1,2))


@funcMaker
def myfunc2(a,b,c):
    time.sleep(2)
    return a+b+c

print(myfunc2(1,2,3))
```

## 我还是我吗？

```
def Makerfunc(func):
    def mytest():
        func()
        print("helh")
    return  mytest


@Makerfunc
def myfunc():
    print("myfunc")

print(myfunc.__name__)#没有装饰之前是myfunc,装饰之后是mytest
```

#### 闭包

```
闭包： 在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。

def f1():
    n = 999

    def f2():
        print(n)

    return f2


if __name__ == '__main__':
    result = f1()
    result()

# 输出：
# 999
```

## 带参数的装饰器

```
def logging(func)是一个装饰器，如果装饰器需要参数，需要通过闭包来实现，即在其外面再定义一个外函数def mylog(type)，将参数type作为外函数的的变量传递到内函数里面。

def mylog(type):
    def logging(func):
        def inner(*args, **kwargs):
            if type == 'debug':
                print('[DEBUG] logging')
            else:
                print('[INFO] logging')
            rv = func(*args, **kwargs)
            return rv
        return inner
    return logging


@mylog(type='debug')
def add(x, y):
    return x + y


if __name__ == '__main__':
    result = add(1, 2)
    print('result: %d' % result)
    
# 输出：
# [DEBUG] logging
# result: 3
```

# Day13

## 使用类作为装饰器 

```
import time


class Timer:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        rv = self.func(*args, **kwargs)
        end = time.time()
        print('time taken %f' % (end - start))
        return rv


@Timer
# 等价于 add = Timer(add)
def add(x, y):
    return x + y


if __name__ == '__main__':
    result = add(2, 3)
    print('result: %d' % result)

# 输出：
# time taken 0.000000
# result: 5


上述相当于把一个装饰器变成了一个 Timer 类的对象，然后 add 函数被传入进了 __init__中，保存为self.func，在后面调用 add(2,3) 的时候，实际上相当于调用了__call__这个函数，做了一个对象的调用，后面参数2和3就被传入到了__call__里面，然后依顺序运行了代码。
```

## 带参数的类装饰器

```
import time


class Timer:
    def __init__(self, prefix) -> None:
        self.prefix = prefix

    def __call__(self, func):
        print('Timer.__call__')

        def wrapper(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            print(f'{self.prefix}:{time.time() - start}')
            return ret

        return wrapper


@Timer(prefix='curr_time:')
# 等价于： add = Timer(prefix = 'curr_time:')(add)
def add(x, y):
    return x + y


if __name__ == '__main__':
    print(add(2, 3))

# 输出：
# Timer.__call__
# curr_time::0.0
# 5


上述把一个装饰器初始化为 Timer 类的对象，然后 prefix 参数被传入进了 __init__中，之后调用__call__函数返回一个闭包。之后就相当于装饰器函数了，用wrapper装饰add函数。
```

## 通过装饰器实现单例模式

```
1.定义一个全局的字典变量,用于保存单例模式下实例化出的对象,键是类名,值是对象
instances={}

def myfunc(cls):
    def mytest(*args,**kwargs):
        if cls.__name__ not in instances.keys():
            #如果这个类名不在字典的键里,那么生成对象
            instances[cls.__name__]=cls(*args,**kwargs)
        return instances[cls.__name__]
    return mytest

@myfunc    #Maker=myfunc(Maker)
class Maker():
    pass


t=Maker()
t2=Maker()
print(id(t))
print(id(t2))
```

## 通过__new__()魔术方法实现单例模式

```
class Maker():
    __instance=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            #如果__instance没有值,那么就使用object的来实例化对象
            cls.__instance=super().__new__(cls)
        return cls.__instance

t=Maker()
t2=Maker()
print(id(t))
print(id(t2))
```

## 类属性和实例属性

```
类属性： 在类名称下面定义的属性
实例属性： 在__init__魔术方法中初始化的属性，或者通过实例对象添加的属性
```

## 实例方法和实例方法和静态方法

```
实例方法：第一个参数是self, 代表当前实例对象本身
类方法: 第一个参数是cls,代表当前的类对象, 需要在方法的上面加上@clssmethod, 类方法可以通过实例对象和类对象来访问 
静态方法：不需要额外的参数，通过@staticmethod来进行装饰，静态方法可以通过类对象和实例对象来进行访问   
        #静态方法在类中是独立的,单纯的函数,只是托管在类的空间,增强代码的逻辑性,简化代码的维护
```

## 进程的概念

```
进程是什么：进程是操作系统进行资源分配的基本单位
比如，我们在操作系统上运行一个应用程序，其实对操作系统来说你就开启了一个进程

单核的CPU,同一时刻只能运维单个进程，虽然可以同时运行多个程序，但进程之间是通过轮流占用CPU来执行的
```

## 创建进程的类Process

```
Multiprocessing模块提供了一个创建进程的类 Process,所以你使用Process类之前要引入Multiprocessing模块
创建进程有以下两种方法:
1.创建一个Process类的实例，并指定目标任务函数
2.自定义一个类，并继承Process类，重写__init__()方法和run()方法


一.使用Process类的实例创建进程
#引入模块
from multiprocessing import Process
#为了获取进程pid
import os
import time
def mytest(d):
    num=0
    for i in range(d*1000000):
        num+=i
    print(f"进程的pid为{os.getpid()}")

#在该代码块内写的代码只能在本文件有,不能被别的文件引用
if __name__=="__main__":
    print("父进程PID为%s "%os.getpid())
    #创建子进程,target的值是子进程要执行的函数,args的值是函数的参数
    p1=Process(target=mytest,args=(3,)) ###args必须是可迭代对象
    t0=time.time()#记录当前时间
    #激活子进程
    p1.start()
    p1.join()#阻塞主进程,让子进程完成任务或子进程被终止
    t1 = time.time()  # 记录当前时间
    print(t1-t0)
    
    
二.使用类创建子进程
#引入模块
from multiprocessing import Process
#为了获取进程pid
import os
import time

class Maker(Process):
    def __init__(self,d):
        self.d=d
        super().__init__()

    #子进程要执行任务函数
    def run(self):
        num = 0
        for i in range(self.d * 1000000):
            num += i
        print(f"进程的pid为{os.getpid()}")



#在该代码块内写的代码只能在本文件有,不能被别的文件引用
if __name__=="__main__":
    print("父进程PID为%s "%os.getpid())
    #创建子进程,使用类
    p1=Maker(3)
    t0=time.time()#记录当前时间
    #激活子进程
    p1.start()
    p1.join()#阻塞主进程,让子进程完成任务或子进程被终止
    t1 = time.time()  # 记录当前时间
    print(t1-t0)

```

# Day14

## 创建进程

```
Process类的构造函数参数说明:
Target:表示调用对象,一般为函数,也可以是类
Args:表示调用对象的位置参数元组
Kwargs:表示调用对象的字典
Name:为进程的别名
Group:参数不使用,可忽略

Process类常用方法:
is_alive():返回进程是否是激活的
join([timeout]):阻塞进程,直到进程执行完成或超时或进程被终止
run():代表进程执行的任务函数,可被重写
start():激活进程
terminate():终止进程

Process的属性:
daemon:父进程终止后自动终止，且不能产生新进程，必须在start(之前设置 
authkey:字节码，进程的准密钥。
exitcode:退出码，进程在运行时为None，如果为-N，就表示被信号N结束。 
name:获取进程名称。 
pid:进程id

Daemon属性：
daemon = True:父进程终止后程序自动终止，且不能产生新进程，必须在start()之前设置 
不设置daemon: 父进程不等待子进程,父进程代码直接运行到尾部,但程序还在等子进程结束

```

## 进程并发控制

```
Semaphore是控制同一时刻并发的进程数

有时候如果很多进程都去访问共享资源，可能导致资源压力过大，比如100个进程都去访问数据库，那么数据库压力会很大，这个时候就可以使用控制进程，让一些进程去访问，一些进程后面再访问

from multiprocessing import Process,Semaphore,current_process
import time

def mytest(se,i):
    se.acquire()#获取许可,可以使用公共资源,其他进程不能使用
    print(time.strftime("%H:%M:%S"),current_process().name+"开始运行")
    time.sleep(i)
    print(time.strftime("%H:%M:%S"),current_process().name+"结束运行")
    se.release()#放弃许可,其他进程可以使用

if __name__=="__main__":
    #创建控制进程的对象
    se=Semaphore(2)
    #循环创建子进程
    for i in range(6):
        p=Process(target=mytest,args=(se,2))
        p.start()
```

## 进程同步-Lock

```
如果有多个进程同时运行，都去访问资源，那么可能导致混乱

这时需要使用锁(Lock)来控制同一时刻仅有一个进程在访问资源

from multiprocessing import Process,Lock
import time

def task1(lock):
    #加锁
    lock.acquire()
    n=5
    while n>1:
        print(time.strftime("%H:%M:%S")+" task1 输出信息")
        time.sleep(1)
        n-=1
    #解锁
    lock.release()

def task2(lock):
    with lock:
        n=5
        while n>1:
            print(time.strftime("%H:%M:%S")+" task2 输出信息")
            time.sleep(1)
            n-=1

def task3(lock):
    with lock:
        n=5
        while n>1:
            print(time.strftime("%H:%M:%S")+" task3 输出信息")
            time.sleep(1)
            n-=1


if __name__=="__main__":
    #创建Lock对象
    lock=Lock()
    p1=Process(target=task1,args=(lock,))
    p2=Process(target=task2,args=(lock,))
    p3=Process(target=task3,args=(lock,))

    p1.start()
    p2.start()
    p3.start()
```

## 进程之间通信-Event

```
需要使用Event来挂起进程或唤醒进程

event.isSet()： 返回event的状态值；
event.wait()：  如果event.isSet()==False将阻塞线程，event建立后默认为False；
event.set()：   设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
event.clear()： 恢复event的状态值为False。

Set能唤醒进程，并让flag为True.
Clear能让flag为false
Wait在flag为false的时候可以挂起进程，flag默认是false

import time
import multiprocessing


def light(event):
    print('此时是红灯')
    time.sleep(3)
    print('绿灯了')
    event.set()
    print(event.is_set())


def car(event, name):
    print(f'car{name}在等红灯')
    event.clear()
    event.wait()
    print(f'car{name}可以走了')


if __name__ == '__main__':
    event = multiprocessing.Event()
    l = multiprocessing.Process(target=light,args=(event,))
    l.start()
    car1 = multiprocessing.Process(target=car, args=(event,1,))
    car2 = multiprocessing.Process(target=car, args=(event,2,))
    car1.start()
    car2.start()
```

## 进程优先级队列-Queue

```
Queue 是多进程安全的队列，可以使用 Queue实现多进程之间的数据传递。
put 方法用以插入数据到队列中，put 方法还有两个可选参数:blocked 和 timeout。如果blocked为True(默认值)，并且 timeout 为正值，则该方法会阻塞timeout 指定的时间，直到该队列有剩余的空间。如果超时，则会抛出 Queue.Full 异常。如果blocked 为 False，但该 Queue 已满，则会立即抛出 Queue.Full 异常。

get 方法可以从队列读取并删除一个元素。同样，get方法有两个可选参数:blocked 和 timeout。如果 blocked 为 True 默认值)，并且 timeout 为正值，在等待时间内没有取到任何元素，则会抛出 Queue.Empty 天异常。如果 blocked 为False，那么将会有两种情况存在: Queue 有一个值可用，立即返回该值，否则队列为空，立即抛出 Queue.Empty异常。

from multiprocessing import Process,Queue
import time

#生产者
def mytest(q):
    n=1
    while True:
        q.put(f'冷饮{n}')
        print(f"{time.strftime('%H:%M:%S')}A进程 放入冷饮{n}")
        n+=1
        time.sleep(1)


#消费者
def mytest2(q):
    while True:
        print(f"{time.strftime('%H:%M:%S')}B进程 取出冷饮{q.get()}")
        time.sleep(5)

if __name__=='__main__':
    #定义队列,容量为5
    q=Queue(maxsize=5)
    p1=Process(target=mytest,args=(q,))
    p2=Process(target=mytest2,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```

## 进程池Pool

```
在使用 Python 进行系统管理的时候，特别是是同时操作多个文件目录，或者远程控制多台主机并行操作，可以节约大量的时间。当被操作对象数目不大时，可以直接利用 multiprocessing中的Process 动态生成多个进程，十几个还好，但但如果是上百个，上千个目标，手动限制进程数量又太过烦琐，此时就可以发挥进程池的功效 了。 
Pool 可以提供指定数量的进程供用户调用，当有新的请求提交到 pool 中时，如果池还没 有满，就会创建一个新的进程用于执行该请求; 如果池中的进程数量已经达到规定的最大值，该请求就会等待，直到池中有进程结束才会创建新的进程。


import multiprocessing
import time

def mytest(name):
    print(f"{time.strftime('%H:%M:%S')}:{name} 开始执行 ")
    time.sleep(3)

if __name__=='__main__':
    #创建进程池,并设定有多少个进程
    pool=multiprocessing.Pool(processes=3)
    for i in range(10):
        pool.apply_async(func=mytest,args=(i,))

    #关闭进程池
    pool.close()

    pool.join()
```

## 数据交换Pipe

```
multiprocessing.Pipe()方法返回一个管道的两个端口，如 Command1的STDOUT 和 Command2 的 STDIN，这样 Command1 的输出就作为 Command2的输入。如果反过来，让 Command2 的输出也可以作为 Command1的输入，这就是全双工管道，默认全双工管道。如果想设置半双工管道,只需要给Pipe()方法传递参数 duplex=False 就可以,即 Pipe(duplex=False)。
Pipe()方法返回的对象具有发送消息 send()方法和接收消息 recv()方法，可以调用 Command1.send(msg)发送消息，调用 Command2.recv()接收消息。如果没有消息可接收，recv()方法会一直阻塞。如果管道已经被关闭，recv()方法就会抛出异常 EOFError。

以后再看
```

# Day15

## 多线程的概念

```
线程也叫轻量级进程，是操作系统能够进行运算调度的最小单位，它被包含在进程中，是进程中的实际运作单位。
线程自身不拥有系统资源，只拥有一些在运行中必不可少的资源，但它可与同属一个进程的其他线程共享进程所拥有的全部资源
一个线程可以创建和撤销另一个线程，同一进程中的多个线程之间可以并发执行

线程有就绪，阻塞，运行三种基本状态
就绪：是指线程具备运行的所有条件，逻辑上可以运行，等待处理机
阻塞：是指线程在等待一个事件（如某个信号量），逻辑上不能运行
运行：是指线程占有处理机，正在运行

#执行密集型计算任务时,多进程更快
#总结:针对IO型任务,使用多线程更快
```

## 创建线程

```
创建线程有2种方式，一种是实例化threading.Thread类，一种是继承threading.Thread，在子类中重写run和init方法

第一种方式:
import time
import threading
def mytest(n):
    print(f"线程名称为:{threading.current_thread().name} 开始执行")
    time.sleep(3)
    print(f"线程名称为:{threading.current_thread().name} 结束执行")

if __name__=='__main__':
    t=threading.Thread(target=mytest,args=(1,))
    t2=threading.Thread(target=mytest,args=(2,))
    t3=threading.Thread(target=mytest,args=(3,))

    t.start()
    t2.start()
    t3.start()

    t.join()
    t2.join()
    t3.join()
    
第二种方式：
import time
import threading

class Maker(threading.Thread):
    def __init__(self,n):
        super().__init__()
        self.n=n

    def run(self):
        print(f"线程名称为:{threading.current_thread().name} 开始执行")
        time.sleep(3)
        print(f"线程名称为:{threading.current_thread().name} 结束执行")


if __name__=='__main__':
    t1 = Maker(1)
    t2 = Maker(2)
    t3 = Maker(3)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
```

## 多线程同步-Lock

```
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，这个时候就需要使用互斥锁

import threading

num=0
#定义锁
lock=threading.Lock()
def mytest(n):
    global num
    #加锁
    lock.acquire()
    for i in range(100000):
        num=num+n
        num=num-n
    #解锁
    lock.release()

if __name__=='__main__':
    t1=threading.Thread(target=mytest,args=(6,))
    t2=threading.Thread(target=mytest,args=(17,))
    t3=threading.Thread(target=mytest,args=(11,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    #如果不加锁,每次运行后,全局变量的值都不同
    print("num=",num)

#Lock叫原始锁，Rlock叫重入锁
lock原始锁的特点:
	1.不能在一个线程中连续加2次锁,会阻塞住
	2.一个线程给其他线程解锁
重入锁的特点
	1.一个线程可以多次加锁
	2.一个线程中的锁,只能本线程解锁
```

## 多线程同步-信号量（控制线程并发量）

```
互斥锁只能允许一个线程访问共享数据，信号量可以同时允许一定数量的线程访问共享数据

import threading
import time
#创建信号量对象,用于控制线程的并发数
sem=threading.BoundedSemaphore(5)

def mytest(n):
    sem.acquire()
    time.sleep(3)
    print(f"{time.strftime('%H:%M:%S')}:{n} 在办理业务")
    sem.release()

mylist=[]
for i in range(12):
    t=threading.Thread(target=mytest,args=(i,))
    t.start()
    mylist.append(t)

for i in mylist:
    i.join()
```

## 多线程同步-条件对象-Condition

```
条件对象condition能让一个线程A停下来，等待其他线程B，线程B满足了某个条件后通知线程A继续运行。

具体步骤：
线程首先获取一个条件变量锁，如果条件不足，则该线程等待（wait）并释放条件变量锁；如果条件满足，就继续执行线程，执行完成后可以通知(notify)其他状态为wait的线程执行。其他处于wait状态的线程接到通知后会重新判断条件以确定是否继续执行

acquire: 请求锁
release：释放锁
wait: 线程挂起，等待被唤醒（notify或notifyAll），可以设置等待超时时间
notify：唤醒等待线程，里面可以指定唤醒几个等待线程，比如设置n=3，则表示随机唤醒等待的三个线程。
notify_all: 唤醒所有的等待线程。

import threading
class Boy(threading.Thread):
    def __init__(self,cd,name):
        super().__init__()
        self.cd=cd
        self.name=name

    def run(self):
        #加锁,为后面的wait准备
        self.cd.acquire()
        print(self.name+":嫁给我吧!")
        #唤醒翠花
        self.cd.notify()
        #自己暂停,等待翠花回应
        self.cd.wait()
        print(self.name+"我单膝下跪,向最漂亮的翠花求婚,并送上砖戒")
        # 唤醒翠花
        self.cd.notify()
        self.cd.wait()
        print(self.name+"你的选择非常明智")
        self.cd.release()#释放锁

class Girl(threading.Thread):
    def __init__(self,cd,name):
        super().__init__()
        self.cd = cd
        self.name = name

    def run(self):
        #加锁
        self.cd.acquire()
        self.cd.wait()#等待二牛求婚
        print(self.name+"没有情调,太直男,不够浪漫,不答应")
        self.cd.notify()#唤醒二牛
        self.cd.wait()#等待二牛做浪漫的事情
        print(self.name+"好吧,答应你")
        self.cd.notify()  # 唤醒二牛
        self.cd.release()#释放锁

#创建条件对象
cd=threading.Condition()
boy=Boy(cd,"二牛")
girl=Girl(cd,"翠花")

#开启线程
girl.start()
boy.start()

```

## 多线程同步-事件-event

```
需要使用Event来挂起进程或唤醒进程

event.isSet()： 返回event的状态值；
event.wait()：  如果event.isSet()==False将阻塞线程，event建立后默认为False；
event.set()：   设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
event.clear()： 恢复event的状态值为False。

Set能唤醒进程，并让flag为True.
Clear能让flag为false
Wait在flag为false的时候可以挂起进程，flag默认是false

from threading import Thread,Event
import time

event=Event()

def light():
    print('红灯正亮着')
    time.sleep(3)
    event.set() #绿灯亮

def car(name):
    print('车%s正在等绿灯' %name)
    event.wait() #等灯绿 此时event为False,直到event.set()将其值设置为True,才会继续运行.
    print('车%s通行' %name)

if __name__ == '__main__':
    # 红绿灯
    light=Thread(target=light)
    light.start()

    # car1
    car1=Thread(target=car,args=(1,))
    car1.start()
    # car2
    car2=Thread(target=car,args=(2,))
    car2.start()
```

## 多线程优先级队列-queue

```
先进先出（queue）
后进先出（LifoQueue）
优先队列(PriorityQueue)
put 方法用以插入数据到队列中，put 方法还有两个可选参数:blocked 和 timeout。如果blocked为True(默认值)，并且 timeout 为正值，则该方法会阻塞timeout 指定的时间，直到该队列有剩余的空间。如果超时，则会抛出 Queue.Full 异常。如果blocked 为 False，但该 Queue 已满，则会立即抛出 Queue.Full 异常。

get 方法可以从队列读取并删除一个元素。同样，get方法有两个可选参数:blocked 和 timeout。如果 blocked 为 True 默认值)，并且 timeout 为正值，在等待时间内没有取到任何元素，则会抛出 Queue.Empty 天异常。如果 blocked 为False，那么将会有两种情况存在: Queue 有一个值可用，立即返回该值，否则队列为空，立即抛出 Queue.Empty异常。

import threading
import time
import queue

#创建队列队象
q=queue.Queue(maxsize=500)

def mytest():
    for i in range(500):
        q.put("书本-"+str(i))

    while True:
        q.put("书本")
        time.sleep(1)

def mytest02():
    while True:
        msg=q.get()
        print(msg)
        time.sleep(1)


t1=threading.Thread(target=mytest)
t2=threading.Thread(target=mytest02)

t1.start()
t2.start()
t1.join()
t2.join()
```

## 线程池-pool

```
在面向对象编程中，创建和销毁对象是很费时间的的，因为创建一个对象要获取内存资源或其他更多资源。虚拟机也将试图跟踪每一个对象，以便更能够在对象销毁后进行垃圾回收。同样的道理，多任务情况下每次都会生成一个新线程，执行任务后资源再被回收就显得非常低效，因此线程池就是解决这个问题的办法。类似的例子还有连接池、进程池等。
将任务添加到线程池中，线程池会自动指定一个空空闲的线程去执行任务，当超过线程池的最大线程数时，任务需要等待有新的空闲线程后才会被执行。

from multiprocessing.dummy import Pool as ThreadPool

import time

def mytest(n):
    print("n=",n)
    time.sleep(2)

#主线程,调用5次mytest
start=time.time()
for i in range(5):
    mytest(i)
end=time.time()
print("顺序执行的时间为:",end-start)#10.002500057220459

start2=time.time()
p=ThreadPool(processes=5)
res=p.map(mytest,range(5))
p.close()
p.join()
end2=time.time()
print("线程池的时间为:",end2-start2)#2.109921932220459
```

# Day16

## 协程介绍

```
协程，又称微线程。协程是python个中另外一种实现多任务的方式，只不过比线程更小占用更小执行单元
```

## 协程 - yield

```
略
```

## 协程 - greenlet

```
协程，又称微线程。协程是python个中另外一种实现多任务的方式，只不过比线程更小占用更小执行单元
```

## 协程 - gevent

```
greenlet 已经实现了协程，但是这个还的人工切换，太麻烦了。python还有一个比greenlet更强大的并且能够自动切换任务的模块**gevent**

其原理是当一个 greenlet 遇到IO(指的是input output 输入输出，比如网络、[文件操作](https://so.csdn.net/so/search?q=%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C&spm=1001.2101.3001.7020)等)操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO
```

## 进程，线程，协程对比

```
略
```

## 计算机网络的历史

## osi/rm的简介

```
ＯＳＩ／ＲＭ模型结构:物理层,数据链路层,网络层,传输层,会话层,表示层,应用层共7层
```

## 物理层,数据链路层,网络层(重点)

```
1.物理层:只负责传输0 1 二进制比特流
2.数据链路层:负责将数据封装成帧
帧是较小的数据,是数据表现的一种形式
3.网络层：负责路由寻址和广播
```

## 传输层,会话层,表示层,应用层(重点)

```
4.传输层：负责建立一个可靠端(发送端)到端(接收端)的连接,包括数据核对和整理
也负责端对端建立,维护,撤销

5.会话层：负责维护或拆除会话,为端系统的应用程序之间提供对话控制机制

6.表示层：完成对数据的转换
对数据格式的转化工作:
1.格式化（数据格式的标准化）
2.发送端数据：加密的形式，接收端：解密的操作
3.发送端数据：压缩的形式，接收端：解压缩的操作

7.应用层：所有的应用程序的网络在此展开,确定进程之间的通信性质,以满足用户的需求
```

## 计算机网络体系结构通信原理

```
一, 数据通信原理
	发送端自上而下传输（直到物理层），接收端自下而上传输（直到发送端发起通信的层次）
二, 对等会话原理
	发送端和接收端只有在对等层才可进行通信，不同层次传输的数据格式不一样：
	应用层、表示层和会话层以报文方式传输 -->报文:一次性要发送的数据块
	传输层以报文或者报文分段方式传输 -->报文分段:传输过程中会不断的封装成分组、包、帧来传输；报文:一次性要发送的数据块
	网络层以分组方式传输  -->分组:大多数计算机网络都不能连续的任意传输数据,所以是把网络系统上的数据分割成小块,逐块发送,这种小块就称为分组
	数据链路层以帧方式传输  ->帧--->数据比较小
物理层以比特流方式传输  ->比特流(二进制)
	发送端每经过一层（物理层除外）都要在原数据上进行协议封装，即最前面加装一个本层所使用协议的协议头；接收端每经过一层都要对原数据进行协议解封装，即去掉原数据最前面的上层协议头
```

## TCP/IP概述

```
TCP/IP（Transmission Control Protocol/Internet Protocol，传输控制协议/网际协议）是指能够在多个不同网络间实现信息传输的协议簇。TCP/IP协议不仅仅指的是TCP 和IP两个协议，而是指一个由FTP、SMTP、TCP、UDP、IP等协议构成的协议簇， 只是因为在TCP/IP协议中TCP协议和IP协议最具代表性，所以被称为TCP/IP协议。

SMTP协议又叫:简单邮件传输协议，在应用层

2.具有通信协议四个层次,分别为:网络接口层,网络互联层,传输层,应用层
```

## TCP/IP网络接口层(重点)

```
1.功能:在物理连接(网线和电脑之间)之上，实现逻辑链路(用到的协议)的连接（拨号连接）
2.网卡:有物理地址,即MAC地址 ->是计算机的身份证
3.SLIP协议:拨号连接使用的协议,缺点: 没有差错校验机制
4.数据报:网络传输的数据的基本单元，它携带了要从计算机传递到目的的计算机的信息
5.数据包:是TCP/IP协议通信传输中的数据单位，单个信息被划分为多个数据块，这些数据块被称为包。
6.路由:路由器从一个接口上接收到数据包，根据数据包的目的地址进行定向并转发到另一个接口的过程
7.ppp协议:用于拨号连接的协议,解决SLIP存在的问题,也叫点对点协议,现在一般用它
8.ARP协议:地址解析协议,作用是根据目标设备的IP地址，查询到目标设备的MAC地址，保证通信的进行
9.RARP协议:反向(逆向)地址解析协议,作用是根据目标设备的MAC地址，查询到目标设备的IP地址
```

## TCP/IP网络互联层(重点)

```
功能
在不同网络之间进行路由寻址、传递数据报
IP( Internet Protocol)协议
无连接、不可靠的协议

ICMP协议:因特网控制消息协议
是ip协议的一部分
作用是报告错误,典型应用:ping命令的执行就是icmp协议工作的过程
```

## TCP/IP传输层(重点)

```
作用:建立应用间端(发送端)到端(接收端)的连接
	面向连接：会话建立，数据传输，会话拆除(建立维护拆除)  可靠
	无连接：不保证数据的有序到达，不可靠
Tcp协议:也叫传输控制协议 (浏览器)
	面向连接
	可靠（三次握手,四次挥手）
	速度慢
UDP协议:用户数据报协议 (QQ,WX)
	无连接
	不可靠
	速度快

端口号：
我们用户在识别或者认识一个软件，是根据软件的名字识别，
而计算机系统或者网络，是通过端口号来识别软件
```

## TCP/IP应用层(重点)

```
主要负责用户和应用程序之间的通信。协调设备和软件的多样性问题；解决系统中文件传输问题。以下是常见的应用协议：
FTP：文件传输协议 (专门文件传输的协议)
HTTP：超文本传输协议 (网页)
DNS：域名系统
Telnet：远程终端协议 (远程操作需要的协议)
IMAP：Internet邮件访问协议  (针对邮箱,会删除邮件)
POP3：邮局协议版本3 (针对邮箱,不会删除邮件)
SMTP协议又叫:简单邮件传输协议
```

## TCP 传输控制协议

```
TCP是面向连接的，可靠的，基于流的传输层协议。
```

## 面试题:TCP连接的三次握手

```
客户端随机生成序列号，发送SYN给服务器端；
服务器端随机生成序列号，将客户端的序列号加1作为确认号， 发送SYN/ACK给客户端；
客户端将服务器端的序列号加1作为确认号，发送ACK给服务器端。
```

## 面试题:TCP建立连接为什么要三次握手，两次可不可以？

```
TCP是可靠的传输层协议，其可靠性是通过数据报文中的序列号来保障的。所以在建立TCP连接的过程当中主要就是为了同步序列号，而数据传输是双向的，对于双向传输的序列号都需要一个确认同步的过程，至少得经过三次数据的交互，所以需要三次握手，两次不可以 
```

## 面试题:TCP断开连接的过程（4次挥手）

```
断开TCP连接可以是由客户端发起，也可以是由服务器端发起   
假设断开连接是由客户端发起的：  
1.客户端向服务端发送FIN
2.服务端向客户端发送ACK  到这,客户端明确不能接收和发送数据给服务端
3.服务端向客户端发送FIN
4.客户端向服务端发送ACK 到这,服务端明确不能接收和发送数据给客户端
```

## 面试题:TCP断开连接的过程为什么要4次    

```
TCP协议是双工的，断开连接的时候发送的FIN只是表示单向的数据已经传输完毕了，不需要再发送数据，但是可以接收对方发过来的数据。所以要将双向通信完全关闭，需要分别发送一次FIN和返回一次ACK
```

## UDP 用户报文协议 

```
UDP是无连接的，不可靠的，基于用户报文的传输层协议
```

## TCP和UDP的区别 (重点) 

```
TCP是面向连接的，可靠的，基于流的传输层协议    
UDP是无连接的，不可靠的，基于用户报文的传输层协议    
因为TCP需要建立连接和断开连接，所以TCP的速度比UDP慢    
因为TCP需要维护系列号和确认号等控制信息，所以TCP的报文长度比UDP大 
```

# Day17

## socket(套接字) 

```
它提供了标准的Sockets API    
目的是能够实现TCP和UDP的通信
```

## TCP实现服务器端

```
1.创建套接字对象
socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.AF_INET:服务器之间通信使用ipv4
socket.SOCK_STREAM:流失socket TCP
2.绑定本地地址，地址是用元组表示，一般里面包含ip和port
socket.bind(("127.0.0.1",9000))
3.开始监听
socket.listen()
4.接受请求
socket.accept()
5.接收信息或发送信息
socket.recv()#接收
socket.sendall()#发送
6.信息传输完毕，要关闭连接
socket.close()


import socket
#1.创建套接字对象
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2.绑定本地地址
sk.bind(("127.0.0.1",9000))
#3.开始监听
sk.listen()
#4.不断的接收客户端的请求
while True:
    #接受请求,返回一个socket对象和一个客户端地址
    obj,clientAddress=sk.accept()
    print("%s:%d客户端连接成功"%clientAddress)
    while True:
        #使用accept返回的套接字对象来接收和发送数据
        msg=obj.recv(1024)
        print(msg.decode("utf8"))
        #判断客户端是否要退出
        if msg.decode("utf8")=="exit":
            obj.sendall("serverexitok".encode('utf8'))
            obj.close()
            break

        inmsg=input(">>:").strip()
        # 判断用户有没有输入信息
        if len(inmsg) == 0:
            continue
        #发送数据给客户端
        obj.sendall(inmsg.encode('utf8'))
```

## TCP实现客户端

```
1.创建套接字对象
socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.AF_INET:服务器之间通信使用ipv4
socket.SOCK_STREAM:流失socket TCP

2.连接服务器
socket.connect((ip,port))

3.接收数据或发送数据
socket.recv()
socket.send()

4.关闭连接
socket.close()


import socket

#1.创建套接字对象
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2.连接服务器
sk.connect(("127.0.0.1",9000))
#3.发送数据给服务端
while True:
    msg=input("请输入信息>>:").strip()
    #判断用户有没有输入信息
    if len(msg)==0:
        continue

    sk.sendall(msg.encode('utf8'))

    #接收服务端发送的信息
    ret=sk.recv(1024)
    print(ret.decode("utf8"))
    if ret.decode("utf8")=="serverexitok":
        break

sk.close()
```

## UDP实现服务端

```
1.创建套件字
socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.AF_INET:服务器之间通信使用ipv4
socket.SOCK_DGRAM:流失socket UDP

2.绑定本地地址
socket.bind(ip和port)

3.收数据和发数据
socket.recvfrom()
socket.sendto(信息，对方的地址)

4.关闭套接字
socket.close()
```

## UDP实现客户端 

```
1.创建套接字
socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.AF_INET:服务器之间通信使用ipv4
socket.SOCK_DGRAM:流失socket UDP

2.收数据和发数据
socket.recvfrom()
socket.sendto(信息，对方的地址)

3.关闭套接字
socket.close()
```

## 总结

```
我们可以使用socket套接字去实现TCP和UDP连接

TCP实现:
1.服务器和客户端都需要创建套接字，并写明使用的协议（IPV4）和传输方式（TCP）
2.服务器需要绑定本地地址和监听，客户端不需要，但客户端需要连接服务端
3.服务端需要接受连接请求
4.服务器和客户端都可以进行接收和发送数据
5.最后双方都需要关闭套接字

UDP实现:
1.服务器和客户端都需要创建套接字，并写明使用的协议（IPV4）和传输方式（TCP）
2.服务器需要绑定本地地址
3.发送数据都需要信息和对方的地址
4.接收数据都会接收到对方的地址
5.最后双方都需要关闭套接字
```

# Day18

## WWW:万维网

```
三项基本技术：  

1. HTML:  HyperText Markup Language 超文本标记语言-如何去构建超文本      
2. URL: Uniform Resource Locator 统一资源定位符-资源存放的位置   
3. HTTP： HyperText Transfer Protoco 超文本传输协议-如何在网络当中去传输超文本        

超文本：

1. 超出普通文本文档范畴的文档（包含：图片，音频，视频，动画....）
2. 包含超链接的文本文档      
```

## HTTP协议

```
HTTP协议用于客户端和服务器端进行通信    
通过请求和响应的交换来达成信息     
请求必须由客户端发起    
响应是由服务器端返回      
HTTP的数据传输是基于传输层的TCP协议 
```

## HTTP请求

```
HTTP报文是面向文本的，报文中的每一个字段都是一些ASCII码串，每个字段的长度是不确定的。HTTP报文传过来的都是一堆的0x ASCII码，例如" 41 63 63 65 70 74"这段十六进制ASCII码串对应的是“accept” 单词。

这些十六进制的数字经过浏览器或者专用工具比如wireshark或fiddler的翻译，可以得到HTTP的报文结构。

HTTP有两种报文：请求报文和响应报文。
```

## 报文格式  

```
格式： 

1. 请求行 

   POST http://101.91.150.147:8008/login/ HTTP/1.1
   请求方法：  POST      要做什么操作    
   URI:  http://101.91.150.147:8008/login/   要请求的资源的位置  
   HTTP协议版本:  HTTP/1.1    

2. 请求头域  headers     

   Host: 101.91.150.147:8008#接受请求的服务器地址
   Connection: keep-alive#短连接
   Content-Length: 39#数据长度
   Accept: application/json, text/plain, */* #指定客户端接收的数据类型
   language: zh-hans#支持IE11
   User-Agent: {Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) 		  Chrome/110.0.0.0 Safari/537.36 }#客户端的相关信息
   Content-Type: application/json#请求的内容类型
   Origin: http://101.91.150.147:8008 #请求来自哪个站点,只有服务器的名字
   Referer: http://101.91.150.147:8008/ #请求来自哪个页面,包含服务器名字和路径
   Accept-Encoding: gzip, deflate#可接受的内容编码
   Accept-Language: zh-CN,zh;q=0.9#客户端可以接受的语言
   Cookie: lang=zh-cn; device=desktop; theme=default; tab=my#Cookie

3. 空行 

4. 内容实体  

   {"name":"test0107","password":"123456"}
```

## HTTP请求的常用方法  

```
GET    
请求URI所对应的资源      

POST   
传输内容实体      

PUT   
通过内容实体部分传输文件内容，将文件上传到指定的位置      

DELETE   
和PUT相反，删除指定位置的文件         

PATCH   
默认是以x-www-form-urlencoded的contentType来发送信息，并且信息内容是放在request的body里。  

HEAD  
HEAD方法和GET方法一致，不返回报文的内容实体     
用于确定URI资源的有效性以及资源更新的日期时间  

OPTIONS    
用来查询针对URI资源所支持的方法   

TRACE    
追踪路径    

CONNECT       
要求用隧道协议连接代理，将内容加密后进行传输    
```

## 数据传输方式:Content-Type

```
Content-Type: application/json
{"name":"test0107","password":"123456"}

Content-Type: application/x-www-form-urlencoded   
name=test0107&password=123456
```

## 面试题： HTTP协议当中GET方法和POST方法的区别？

```
1.get方法一般是获取资源,post方法为了传输内容实体

2.get方法的参数是直接拼接到url上进行传输,post的参数主要通过内容实体传输  

3.get方法的参数只能是urlencode方式,post可以是其他Content-Type方式

4.post传递参数方式相对于get方式更加安全,因为get的参数会显示到url上

5.get参数传递的个数可能会因为浏览器的不同而有限制,post没有

6.对于资源来说.get是安全的,post不安全
```

## 面试题： HTTP协议当中POST方法和PUT方法的区别 

```
1.post是传输内容实体,put用于传输文件
```

## HTTP响应 报文格式

```
1. 响应行   

   HTTP/1.1 200 OK
   协议版本： HTTP/1.1    
   状态码：  200    
   描述信息：OK   

2. 响应头域   

   Content-Type: application/json#响应数据类型
   X-Frame-Options: DENY#表示该页面不能再iframe中展示
   Content-Length: 158#响应内容的长度
   Vary: Cookie, Origin#返回的内容添加了服务器的头部信息和Cookie
   X-Content-Type-Options: nosniff#有助于防御MIME型攻击
   Referrer-Policy: same-origin#对应同源请求会发送引用地址
   Access-Control-Allow-Credentials: true#表示是否允许发送Cookie
   Access-Control-Allow-Origin: http://101.91.150.147:8008/#指定服务器可以跨域源
   Set-Cookie: sessionid=80ztl2ghhyxk0uakjewf5u9d037xh7om; expires=Mon, 13 Mar 2023 12:13:17 GMT; HttpOnly; Max-Age=1209600; Path=/; SameSite=Lax #设置Cookie

3. 空行  

4. 内容实体

   {"code": "200", "msg": "Success Create", "data": {"name": "test0107", "openid": "290fc49f49dbe28661bb27f6ed785d31", "user_id": 251921}, "ip": "113.91.43.228"}    
```

## HTTP响应状态码

```
1XX: 提示信息，服务器端已经收到了请求，但是还需要进一步的处理  
2XX: 操作成功    
3XX: 重定向   
4XX: 客户端错误   
5XX: 服务器端错误

100 Continue   
200 OK  操作处理成功  
204 No Content   请求处理成功，但是没有内容返回   
206 Partial Content  客户端进行了范围请求，服务器按照客户端的要求返回了部分内容    
301 Moned Permanently   永久重定向   
302 Found   临时重定向    
303 Other   临时重定向,明确表示客户端应该采用GET方法来获取资源     
304 Not Modified  根据客户端请求的条件，资源并没有发生改变     
400 Bad Request   HTTP请求的语法错误   
403 Forbidden  对于资源的被服务器拒绝，服务器没有必要给出拒绝的理由   
404 Not Found   无法找到请求的资源     
500 Internal Server Error  服务器端错误   
503 Service Unavailable  服务器临时错误      
```

## HTTP协议的特点 

```
无连接
一次HTTP的请求和响应完成之后，会关闭掉TCP的连接     
由于现在的网页的内容越来越丰富，浏览一个页面，不再是简单的发起一个HTTP请求，完成业务操作需要频繁的发送HTTP请求。这就要求TCP的连接可以复用。      
通过： Connection: keep-alive (长链接) 来解决该问题 

无状态
HTTP协议对交互的场景没有记忆能力
解决HTTP无状态的问题:

cookie     
1. 服务器生成cookies信息，在HTTP响应报文的头域当中通过Set-Cookie头域来告知客户端应当保存cookie内容   
2. 浏览器接收响应，将cookie内容在本地保存      
3. 浏览器针对相同域名发起HTTP请求，会附带上保存的cookies，通过请求报文的cookies头域       

session    
session是一种记录客户状态的机制，不同的是，cookie是保存在客户端的浏览器中，session是保存在服务器上。 当浏览器访问服务器的时候，服务器把用户信息记录以某种形式记录在服务器上，这就是seesion         

token   
标识用户身份的一串字符串，服务器加密生成token,保存在客户端    
客户端的请求带上token,服务器对token解密对比即可验证身份     
```

## 面试题： cookie和session的区别

```
1. cookie是保存在客户端,session是保存到服务端
2. cookie保存在客户端,相对于session就不是那么安全
3. cookie的数量和数据有限制,数量一般不超过20个,数据不能超过4K
4. cookie是HTTP协议中的规范,session是一种机制.通常会使用cookie来存储session_id
```

## 加密算法 

```
1. 对称加密   
加密和解密采用相同的秘钥    
优点： 加密速度快   
缺点： 秘钥的传递和保存是一个问题，参与加密和解密的双方使用的秘钥一样，这样秘钥就很容易泄露   

2. 非对称加密    
加密和解密采用不同的秘钥(公钥和私钥)   
优点： 加密和解密的秘钥不一样，公钥是可以公开的，只保证私钥不被泄露即可，这样秘钥的传递就变得简单很多，从而降低了被破解的几率   
缺点： 加密速度慢   

3. 线性散列算法     
单向的不可逆的(加密之后不能够被解密) 比如，密码存储,md5加密
```

## HTTPS 

```
1. 首先客户端通过URL访问服务器建立SSL连接。
2. 服务端收到客户端请求后，会将网站支持的证书信息（证书中包含公钥）传送一份给客户端。
3. 客户端的服务器开始协商SSL连接的安全等级，也就是信息加密的等级。
4. 客户端的浏览器根据双方同意的安全等级，建立会话密钥，然后利用网站的公钥将会话密钥加密，并传送给网站。
5. 服务器利用自己的私钥解密出会话密钥。
6. 服务器利用会话密钥加密与客户端之间的通信。
```

## 面试题： HTTP和HTTPS协议的区别 

```
1. https是http的安全版本,http的明文的数据方式传输,HTTPS是用了SSL/TLS协议进行了加密传输
2. http的默认端口号是80,https的默认端口号是443
3. https需要证书,http不需要
```

# Day19

## Selenium环境配置

```
略
```

## 页面元素定位介绍(重点)

```
selenium可以识别的元素,要求属性必须唯一
1）id  用id的值
2）xpath 路径
3）css selector 标签名+class属性的值
4）link text 使用链接文字
5）patial link text  使用子元素的链接文字 
6）name 用name属性的值
7）class name 用class属性的值
8）tag name 用标签名
查找顺序是从html开始
e=dr.find_element(By.ID,'kw')-- 3.7以上版本的
e=dr.find_elements(By.ID,'kw')-- 3.7以上版本的
from selenium.webdriver.common.by import By
By.ID
By.NAME
By.LINK_TEXT
By.PARTIAL_LINK_TEXT
By.TAG_NAME
By.CLASS_NAME
By.CSS_SELECTOR
By.XPATH
```

# Day20

## 页面操作

```
1.鼠标键盘
clear()： 清除文本。
send_keys (value)： 模拟按键输入。
click()： 单击元素。例如按钮操作。

2.获取元素标签的属性值
get_attribute(属性名)： 获得属性值，可以获取自定义的属性。
get_property(属性名):获得属性值。自定义属性不能获取

3.获取元素的属性信息
• text• 获取元素标签对之间间的文本值
• size• 获取元素的尺寸大小
• id  Selenium内部的一个元素属性，用于判断两个元素是否是相同的元素。
• screenshot()方法。
• 给元素一个快照，并保存为PNG格式的图片。

4.获取元素的基本状态信息
• is_enabled()方法  用于判断元素的可用性
• is_selected()方法 用于判断复选框等元素是否处于选择状态
• is_displayed()   检查该元素是否用户可见

5.其他操作
submit()：用于提交表单。 例如， 在搜索框输入关键字之后的“回车” 操作， 就可以通过该方法模拟。
title：用于获得当前页面的标题。
current_url：用户获得当前页面的URL
```

# Day21

## 鼠标操作的其他操作

```
需要引入
from selenium.webdriver.common.action_chains import ActionChains
格式:
ActionChains(浏览器).context_click(元素).perform()

1）右键单击:context_click()
2）鼠标悬停:move_to_element()
3）双击:double_click()
4）拖动:drag_and_drop(source, target)
```

## 下拉列表的操作

```
1.下拉列表是非常常见的页面元素。是一种特殊的页面元素，定位和其他元素没区别，但是其操作不其他元素不同。
2.需要导入包
from selenium.webdriver.support.select import Select
3.选择下列列表中的元素有三种方式
• select_by_index()        #索引
• select_by_visible_text() #文本
• select_by_value()        #value属性的值
```

## 键盘操作

```
Keys类提供了键盘上几乎所有按键的方法。
• send_keys()方法可以用来模拟键盘输入。
• 还可以用它来输入键盘上的按键， 甚至是组合键， 如 Ctrl+A、 Ctrl+C 等。
• 在使用键盘按键方法前需要先导入 keys 类。
• from selenium.webdriver.common.keys import Keys
常用的键盘操作:
• send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
• send_keys(Keys.TAB) 制表键(Tab)(不常用)
• send_keys(Keys.ESCAPE) esc键（Esc）
• send_keys(Keys.ENTER) 回车键（Enter）
• send_keys(Keys.CONTROL,‘a’) 全选（Ctrl+A）
• send_keys(Keys.CONTROL,‘c’) 复制（Ctrl+C）
• send_keys(Keys.CONTROL,‘x’) 剪切（Ctrl+X）
• send_keys(Keys.CONTROL,‘v’) 粘贴（Ctrl+V）
```

## 浏览器控制

```
dr.set_window_size(宽,高)
dr.maximize_window():最大化显示
dr.minimize_window():最小化显示，在最小化情况下，也可以进行元素定位及操作

页面前进与后退
back()和forward()方法来模拟后退和前进按钮

页面刷新
driver.refresh()

针对浏览器窗口页面截图
get_screenshot_as_file(保存图片的位置)
```

## 多窗口处理

```
多窗口的意思是一个浏览器中打开了多个窗口

• 浏览器标签页的切换
    • 浏览器的标签页在应用中一般称为页面句柄（handle）。
    • 获取当前窗口句柄：driver.current_window_handle
    • 获取浏览器所有句柄：driver.window_handles
    • 切换到指定的浏览器窗口：driver.switch_to.window(handle)
    
注意:
关闭页面需要切换到页面中,获取操控页面的元素也需要切换到该页面
关闭其中某个页面后,需要重新获取当前浏览器所有的句柄
```

## 多Frame框处理

```
在一个页面中可以嵌套另外一个页面，如frame/iframe技术，这是现在很多web应用中使用的一种方式，webdriver对象只能在一个页面（外层是默认的）中定位元素，需要一种方式将driver对象从外层切换给内层使用才能对内层的对象进行处理。

webdriver中提供API：driver.switch_to.frame()

1）切入Frame
第一种方式,默认是可以给ID或者name的

    driver.switch_to.frame("login_frame")

第二种方式,可以传参iframe的元素对象

    iframeObj = driver.find_element_by_xpath('//*[@id="login_frame"]')
    driver.switch_to.frame(iframeObj)
# 切换到目标元素所在的frame
dr.switch_to.frame("iframeResult")

2）从Frame切入到主体
dr.switch_to.default_content()
```

## 警告框处理

```
警告框-alter，是一个模式框
1、driver对象不在alter上，并且我们没办法去定位这个窗口的元素
2、driver.switch_to.alert:暂时将浏览器对象driver交给alter用
3、可以对alter警告框作什么事情：
        text：返回（获取） alert/confirm/prompt 中的文字信息。
        accept()：接受现有警告框，就是点他的确定按钮
        dismiss()：放弃现有警告框，取消
        send_keys(keysToSend)：发送文本至警告框。
```

# Day22

## 页面滚动条操作

```
使用JS实现
• 左右移动：js="window.scrollTo(200,1000)"
上面的参数说明,第一个参数越大越往右边,第二个参数越大越往底部
• Js代码的执行需要用到的方法：driver.execute_script(js)
```

## 元素等待

```
1.强制等待（无条件等待）
使用方法：time.sleep(delay)

delay的单位为秒，delay设置多少秒页面就会等待多少秒（死等），这个方法很容易让线程挂掉，使程序抛异常，所以要慎用此方法。

2.显式等待（有条件等待）
当等待的条件满足后（一般用来判断需要等待的元素是否加载出来），就继续下一步操作。等不到就一直等，如果在规定的时间之内都没找到，那么就跳出Exception。

使用显示等待前需先导入显示等待所需模块和等待条件
#显式等待模块
from selenium.webdriver.support.ui import WebDriverWait
#显式等待条件
from selenium.webdriver.support import expected_conditions as EC

3.隐式等待(无条件等待，在一个时间段内等待)
一次设置，全局生效。不要当作固定等待使用，不要每次需要等待时都写一次隐式等待。
隐式等待设置了一个最长等待时间，在规定时间内网页加载完成(也就是一般情况下你看到浏览器标签栏那个小圈不再转就代表加载完成)，则执行下一步，否则一直等到时间结束，然后执行下一步。


#如果是只需等待页面中的一个元素加载就用显示等待，等待整个网页加载就用隐式等待。
```

## 自动化测试用例设计

```
一、自动化测试用例设计（熟练掌握）
1、自动化测试用例一般可以由手工测试用例转化而来，需注意

    不是所有的手工测试用例都要转为自动化测试用例
    考虑到脚本开发的成本，不要选择流程太复杂的用例，可以把流程拆分成多个用例
    选择的用例最好可以构建成场景
    选取的用例可以是你认为是重复执行、很耗时间的部分，例如字段验证
    选取的用例可以是主流程用例，即适用于冒烟测试的用例

2、自动化测试用例的设计原则（熟练掌握）

    一个用例为一个完整的场景，从用户登录系统到最终退出并关闭浏览器
    一个用例只验证一个功能点，不要试图在用户登录后把所有的功能都验证一遍
    尽可能少的编写逆向测试用例，一方面因为逆向逻辑的用例很多
    另一方面自动化测试脚本本身比较脆弱
    用例和用例之间尽量避免产生依赖。
    一条用例完成测试之后需要对测试场景进行还原，以免影响其它用例的执行

3、自动化测试用例设计实践（熟练掌握）
测试点转为测试用例的原则是什么？

    设计一条正向用例，覆盖足够多的有效等价类数据
    设计一条反向用例，需要覆盖一条无效等价类数据，其他数据一概使用正向数据

有验证码的时候，该怎么进行自动化？

    让开发暂时屏蔽验证码、将验证码改为万能码（‘aaaa’）
    懂机器学习，可以训练样本，可以达到99%以上识别成功率
    调用OCR的接口，去解析图片中验证码，然后来用
```

## 线性脚本开发

```
线性测试：以一行行的代码直接实现测试步骤，脚本相对独立，单纯的模拟用户完整的操作场景，测试用例的开发和维护成本很高，如果一个页面元素被改动了，所有线性脚本中用到这个元素的都需要更改。是最基本的
```

## 模块化驱动脚本开发

```
模块化驱动测试：把常用、公用的一些功能、业务、步骤专门提取出来，写在一个专门的模块中，以方法、类的形式实现出来，再其他的模块如果需要这些功能，直接调用即可，无需重复显示这些代码。比如可以做登录模块、退出模块、邮件发送模块、数据库处理模块、日志生成模块等
模块化驱动测试最大层度地去除了重复，提高了测试脚本的复用性和可维护性。
```

# Day23

## 数据驱动脚本开发

```
略
```

## 检查点

```
略
```

## Unittest测试框架介绍(重点)

```
web自动化：python + selenium + unittest
原理
1）TestCase：
在unittest中的一个TestCase的实例就是一个测试用例，就是一个完整的测试流程，包括测试前资源初始化(setUp)，执行测试代码(test)，以及测试后环境的还原(tearDown)。
2）TestSuite
测试套件，可以理解为：多个独立的测试用例（test case）或者多个独立的测试套件（test suite，可以理解为子套件）可以构成一个测试套件，然后传递给TestRunner进行测试执行。,内容也有run函数可以执行测试
3）TestLoader
通过unittest.TestLoader类的loadTestsFromTestCase、loadTestsFromModule、LoadTestsFromName、discover方法，可以将测试用例添加一个测试套件中。
4）TestRunner 
可以理解为测试集的运行器，可以在其基础上扩展子类TextTestRunner或者HTMLTestRunner，只不过生成的测试报告样式不同，此处讲解TextTestRunner，后续课程再扩展HTMLTestRunner。
5、TestResult
测试结果类，用来处理测试用例或测试集执行过程中的所有信息并最终输出,比如代码错误、异常、断言失败、skip等等。
```

## Unittest测试框架运行说明(重点)

```
步骤:
1.导包，unittest是自带的框架，不需要安装
2.创建一个单元测试类（其实就是类，只不过他继承了单元测试框架单元测试用例的类）
3.执行

单元测试类中的方法说明:
1.setUpClass：给当前单元测试类的所有的用例进行初始化的,是类方法
2.tearDownClass：给当前单元测试类的所有的用例进行资源释放,是类方法
3.setUp()：主要是进行测试用例的资源初始化，测试用例的前提条件写在这
4.test_xxx()：测试用例，要把测试用例的步骤写在这个方法中,注意要test开头,是规定
5.tearDown()：主要是进行测试用例的资源释放的

执行顺序说明:
1.先执行setUpClass
2.setUp()、test_xxx()、tearDown(),不管你怎么调整为，执行顺序不变
3.最后执行tearDownClass
4.每执行一个测试用例,2都要执行一遍

区别说明:
1.setUpClass和setUp()的区别：
    setUp()不需要@classmethod注解；setUpClass方法需要@classmethod注解
    setUp()实例方法，就需要创建对象再调用；setUpClass类方法，不需要对象也可以调用
    setUp()再每一个测试用例执行之前运行一次；setUpClass方法在测试执行之前只执行一次
    setup()是对一条测试用例的初始化；setUpClass()给当前单元测试类的所有的用例进行初始化的
2.tearDownClass和tearDown的区别:
	tearDown()不需要@classmethod注解；tearDownClass方法需要@classmethod注解
    tearDown()实例方法，就需要创建对象再调用；tearDownClass类方法，不需要对象也可以调用
    tearDown()再每一个测试用例执行之后运行一次；tearDownClass方法在测试执行之后只执行一次
    tearDown()是对一条测试用例的资源释放；tearDownClass给当前单元测试类的所有的用例进行资源释放

执行方式:
1.执行main()方法执行的特点:unittest.main()
2.有选择的执行测试用例
	1.通过测试集合内部函数添加测试用例
	2.通过模块添加执行用例
```

# Day24

## 执行所有的测试用例

```
1.执行main()方法执行的特点:unittest.main()
	注意:
	1.是把所有的测试用例执行了一遍
	2.执行测试用例的顺序控制不了，（按照测试用例名（方法名）的字母顺序执行的）
```

## 内部方法添加测试用例(重点) addTest(s)

```
通过内部函数添加测试用例
步骤:
1.生成测试套件(也叫测试集合)
    suite = unittest.TestSuite()
2.把测试用例添加进测试集合,两种方式添加
	1.suite.addTest(类名("用例"))
	2.suite.addTests(map(类名,["用例1","用例2",...]))
3.生成测试结果对象,然后传递到run函数中
	re = unittest.TestResult()
	suite.run(re)
```

## 通过模块方法添加测试用例(重点) TestLoader

```
通过模块方法添加测试用例
1.如果测试用例的数量比较大，使用testsuite自带的方法加用例到集合，很麻烦
可以unittest中提供的testloader模块，提供了好多帮我们把测试用例加载到测试集合中的方法
2.步骤:
	1.创建testloader的对象
	2.使用testloader的对象中的loadTestsFromName函数添加测试用例,这个api,返回测试套件
		1.可以添加整个模块的测试用例
		2.也可以添加一个单元测试类中的所有测试用例(只能添加一个单元测试类)
		3.也可以添加单元测试类中的某个测试用例(只能添加一个单元测试类中的一个测试用例)

	3.生成测试结果对象,然后传递到run函数中
		re = unittest.TestResult()
		suitt.run(re)
		
#创建loader对象
    loader=unittest.TestLoader()
    #参数为模块名,返回测试套件,执行一个模块中所有的用例
    suit=loader.loadTestsFromName("Maker2Tests")
    #执行一个模块中的某个单元测试类中的所有用例
    # suit=loader.loadTestsFromName("Maker2Tests.Maker")
    #执行一个模块中的某个单元测试类中的某个用例
    suit=loader.loadTestsFromName("Maker2Tests.Maker.test_05")

    # 生成测试结果对象, 然后传递到run函数中
    re = unittest.TestResult()
    suit.run(re)
```

## 通过路径方式添加测试用例(重点) defaultTestLoader

```
使用unittest.defaultTestLoader对象的discover方法加载用例，可以将指定路径所有符合匹配规则（pattern）的文件中的单元测试用例一次性加载
第一个参数是一个目录，这个目录下可以有单元测试用例的文件（.py）
第二个参数是填文件名,可以通配
 suitt = unittest.defaultTestLoader.discover(r"./Maker/", pattern="unit*.py")
说明: 
	1."unit*.py指的是以unit开头，以.py结尾的文件
	2..py中的单元测试用例要使用unittest框架写的测试用例

步骤:
	1.生成测试套件(也叫测试集合)
	2.使用discover方法批量添加
	3.生成测试结果对象,然后传递到run函数中
		re = unittest.TestResult()
		suitt.run(re)0
```

## 测试报告 TextTestRunner

```
在前面测试用例、测试集合执行的时候都是用testsuite()的run()方法：suitt.run(result),如果要生成text文本形式的测试执行报告,可以使用TestRunner   
将最后执行的:
re = unittest.TestResult()
suitt.run(re)
改为:
with open(r"./re.txt", "w", encoding="utf-8") as f:
  runner = unittest.TextTestRunner(f, descriptions="单元测试报告执行", verbosity=5)
  runner.run(suitt)
函数说明:
f:文件描述符
descriptions:用来标记是否输出测试用例的描述信息。布尔类型,没什么用
verbosity参数可以控制输出的错误报告的详细程度，只有3个取值：
	0 (quiet): 只显示执行的用例的总数和全局的执行结果。
	1 (default): 默认值，显示执行的用例的总数和全局的执行结果，并对每个用例的执行结果（成功T或失败F）有个标注。(测试用例中如果有和预计不同,会出现F)
	2+ (verbose): 显示执行的用例的总数和全局的执行结果，并输出每个用例的详细的执行结果。
```

## HTMLTestRunner(重点)

```
前面使用runner运行器是unittest自带的，效果不是很好，我们第三方开发的来用，可以以HTML格式展示结果。

import unittest
from HTMLTestRunner import HTMLTestRunner
import time
if __name__=='__main__':
    suit = unittest.defaultTestLoader.discover(r'./MyTestFile/', pattern="unit*.py")

    filename="./"+time.strftime("%Y-%m-%d %H_%M_%S")+"res.html"
    with open(filename,"wb") as f:
        runner=HTMLTestRunner(f,verbosity=2,title="单元测试报告",description="第一次运行结果")
        runner.run(suit)

```

## 邮件的自动化

```
通过python我们可以自动发送报告给负责人
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
1.把html发送为正文
2.把html发送为附件

import unittest
from HTMLTestRunner import HTMLTestRunner
import time
#构建邮件内容Subject
from email.mime.text import MIMEText
#构建邮件头部信息的
from email.header import Header
#构建发件人
from email.utils import formataddr
#添加附件
from email.mime.multipart import MIMEMultipart
#创建发送邮件对象
import smtplib


if __name__ == '__main__':
    loder = unittest.TestLoader()
    suite = loder.loadTestsFromName("TestClass")
    print(suite)
    filename = time.strftime("%Y-%m-%d-%H_%M_%S") + "res.html"
    with open(filename, "wb") as f:
        runner = HTMLTestRunner(f, verbosity=2, title="单元测试报告", description="第一次运行结果")
        runner.run(suite)

    #获取报告内容
    htmlreport = None
    with open(filename, 'rb') as f:
        htmlreport = f.read()

    #构建邮件
    mail = MIMEText(htmlreport, 'html', 'utf-8')
    mail['Subject'] = Header(f'邮件自动化{filename}', 'utf-8')
    mail['From'] = formataddr(['JInpeng_Wang', '1832508189@qq.com'])
    mail['to'] = '18770766249@163.com'

    #添加附件
    mp = MIMEMultipart()
    mail2 = MIMEText(htmlreport, 'base64', 'utf-8')
    mail2['Content-Type'] = "application/octet-stream"
    print(filename)
    mail2['Content-Disposition'] = f'attachment;filename={filename}'
    mp['Subject'] = Header(f'邮件自动化附件', 'utf-8')
    mp['From'] = formataddr(['JInpeng_Wang', '1832508189@qq.com'])
    mp['to'] = '18770766249@163.com'
    mp.attach(mail2)

    ##构建SMTP对象
    smpt = smtplib.SMTP()
    smpt.connect("smtp.qq.com")
    smpt.login('1832508189@qq.com', 'wlcydcooamluceah')
    smpt.sendmail('1832508189@qq.com', '18770766249@163.com', mail.as_string())
    smpt.sendmail('1832508189@qq.com', '18770766249@163.com', mp.as_string())
    smpt.quit()
```

## DDT

```
ddt是“Data-Driven Tests”的缩写，是unittest中实现数据驱动的主要方式之一，它主要包括如下的装饰器

@ddt
标记测试类，支持DDT数据驱动

@data
标记测试用例，传递参数

@unpack
当@data中的参数是元组、列表时，用于分割序列中的元素

@file_data
标记测试用例，传递文件，支持yaml和json文件


test_data=['hello','world']

@ddt.ddt#代表下面这个单元测试支持ddt驱动
class Testmaker(unittest.TestCase):

    @ddt.data(1,2)
    def test_ddt(self,v):#这个用例会执行2遍
        print("test_ddt")
        print(v)#1 2

    @ddt.data((1,2,3),[3,4,5])
    @ddt.unpack
    def test_ddt2(self,v1,v2,v3):#data参数中的序列有多少个数,那么这里的参数个数就必须是多少个
        print("test_ddt2")
        print(v1)
        print(v2)

    @ddt.data(test_data)#参数是列表时
    @ddt.unpack
    def test_ddt3(self,v1,v2):
        print("test_ddt3")
        print(v1)
        print(v2)

    @ddt.file_data("mydata.yaml")#参数是文件名
    def test_ddt4(self,txt):#执行了4次,因为mydata.yaml中有4个数据
        print("test_ddt4")
        print(txt)
        
if __name__=='__main__':
    unittest.main()
```

# Day25



























