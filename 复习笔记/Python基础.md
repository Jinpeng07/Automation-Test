# Day1

## 输入输出

```
1.输出:
print("sdfsdffs")
print输出是默认换行
消除默认换行:
print("xxxx",end='')

2.输入:
msg=input("提示信息")
会阻塞,等待输入
得到的数据都是字符串
```

## 占位符

```
%d,整数，比如1,2,3,4等就是整数,没有小数点
%f,浮点，比如20.22,30.33,有小数点的,就叫浮点数
%s,字符串,比如"我是字符串",'我也是字符串'

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
#打印变量存储的地址,这地址是执行内存空间的,这个内存空间就是存储的数据
print(id(a))

变量的类型:用type(变量名)可以查出变量里存储的数据类型
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
转义字符不是普通的字符,是有特殊含义的字符,比如\n表示换行,并不会打印出\n字符串
print("我是\n程序员")
我是
程序员

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
		起始,结束,步长**都是可写可不写**,选取区间属于**左闭右开(**包头不包尾),结束不包括结束本身
		
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
string.find(str, beg, end):从字符串中查找子串所在位置, 没找到返回-1 
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

注意：
1）Python没有像其它大多数语言一样使用“{}”表示语句体，
而是通过语句缩进来判断语句体，缩进默认为4个空格。
2）可以使用比较、逻辑表示条件语句
3）可以使用in和not in表示包含关系
4）甚至可以使用布尔类型的判断
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
3、list可以使用+操作符进行拼接
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

### 移除且返回pop()

```
pop(位置) 移除列表中指定索引处的元素，默认移除的是最后一个元素，返回的是被移除的数据
```

### 移除不返回remove()

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
d={1:"hello",2:'world'}
print(d)
#通过键获取值,下面的1不是下标,是键
print(d[1])#hello
#通过get函数也可以获取键对应的值
print(d.get(1))#hello
d2={'a':"hello","b":"world"}
print(d2["a"])#hello
#获取字典中所有的键
print(list(d.keys()))
#获取字典中所有的值
print(list(d.values()))

# print(d[7])#报错
print(d.get(7))#None
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
序列为键,某个数为值(fromkeys),返回列表,元素是元组(items)
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


























































